import streamlit as st
from streamlit.hello.utils import show_code


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
 
 
def underwriter() -> None:
    st.header("Chat with Underwriter - PDF ")
   
 
underwriter()

#show_code(underwriter)
