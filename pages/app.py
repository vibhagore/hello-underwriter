import streamlit as st
import pickle
from streamlit.hello.utils import show_code
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
import os

def underwriter(openai_api_key) -> None:
      
    st.header("Chat with Virtual Underwriter")
    # upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type='pdf')
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        st.write(pdf_reader)
        
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
            )
        chunks = text_splitter.split_text(text=text)

        #embeddings
        if os.path.exists(f"{store_name}.pkl"):
            with open(f"{store_name}.pkl", "rb") as f:
                VectorStore = pickle.load(f)
            # st.write('Embeddings Loaded from the Disk')s
        else:
            embeddings = OpenAIEmbeddings(openai_api_key=textAPIKey)
            # call like this: openai = OpenAIEmbeddings(openai_api_key="my-api-key")
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            store_name = pdf.name[:4]
            with open(f"{store_name}.pkl", "wb") as f:
                pickle.dump(VectorStore, f)

        st.write(chunks)
      
# Sidebar contents
with st.sidebar:
   
    st.title('🤗💬 LLM Chat with the Virtual Underwriter App')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
 
    ''')
    #add_vertical_space(5)
    st.write('Made with ❤️ by [Prompt Engineer](https://youtube.com/@engineerprompt)')

    st.header("Get the API Key")
    openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
   
    underwriter(openai_api_key)

#show_code(underwriter)
