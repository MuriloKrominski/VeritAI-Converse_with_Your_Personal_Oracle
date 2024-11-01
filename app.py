"""
Project: VeritAI - Your Personal Oracle
Author: Murilo Krominski
Description: This Streamlit-based chatbot application allows users to upload or link content from various sources (Website, PDF, YouTube) 
and interact with a chatbot that provides responses based on the loaded content. Built with love to offer a bilingual experience.
"""

import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader, YoutubeLoader, PyPDFLoader
from dotenv import load_dotenv
import streamlit as st
import tempfile

# Load environment variables from .env file
load_dotenv()

# Store the API key in session state to maintain it across interactions
if 'api_key' not in st.session_state:
    st.session_state.api_key = os.getenv('GROQ_API_KEY')

# If no API key, prompt user to enter it and click a button to continue
if not st.session_state.api_key:
    st.error("API key not found! Please enter your GROQ_API_KEY.")
    api_key = st.text_input("Enter your GROQ_API_KEY:", type="password")
    
    if st.button("Continuar"):
        if api_key:
            st.session_state.api_key = api_key  # Save the API key in session state
            st.success("API key set successfully!")
            st.write("If you don’t have an API key, please create your own at https://console.groq.com/keys.")
        else:
            st.error("Please enter a valid API key to continue.")
else:
    # Set the API key as an environment variable for usage in the ChatGroq model
    os.environ['GROQ_API_KEY'] = st.session_state.api_key

    # Initialize the chatbot model with the provided API key
    chat = ChatGroq(model='llama-3.1-70b-versatile')

    # Language selection handling
    if 'language' not in st.session_state:
        language = st.selectbox("Select your language / Selecione seu idioma:", ["Choose...", "1 - English", "2 - Português"])
        if language == "1 - English":
            st.session_state.language = "en"
        elif language == "2 - Português":
            st.session_state.language = "pt"
        elif language == "Choose...":
            st.stop()  # Stop script if no language is selected

    # Set UI labels based on the selected language
    if st.session_state.language == "en":
        # English labels
        st.title("VeritAI: Your Personal Oracle")
        source_label = "Choose the information source:"
        website_prompt = "Enter the website URL:"
        pdf_prompt = "Upload your PDF"
        youtube_prompt = "Enter the YouTube video URL:"
        load_button_label = "Load"
        question_label = "Type your message:"
        send_button_label = "Send"
        loaded_msg = "Content loaded successfully!"
    elif st.session_state.language == "pt":
        # Portuguese labels
        st.title("VeritAI: Seu Oráculo Pessoal")
        source_label = "Escolha a fonte de informação:"
        website_prompt = "Digite a URL do site:"
        pdf_prompt = "Faça o upload do seu PDF"
        youtube_prompt = "Digite a URL do vídeo do YouTube:"
        load_button_label = "Carregar"
        question_label = "Digite sua mensagem:"
        send_button_label

        = "Enviar"
        loaded_msg = "Conteúdo carregado com sucesso!"
    else:
        st.stop()  # Stop script if language is not selected yet

    # Function to generate the chatbot's response
    def get_bot_response(messages, document):
        system_message = '''You are a friendly assistant named VeritAI, created by Murilo Krominski.
        You use the following information to formulate your responses: {information}'''

        template_messages = [('system', system_message)]
        template_messages += messages
        template = ChatPromptTemplate.from_messages(template_messages)

        chain = template | chat
        try:
            response = chain.invoke({'information': document}).content
            return response
        except Exception as e:
            st.error("Ocorreu um erro ao obter a resposta do bot.")
            st.write(e)
            return None

    # Initialize storage for document and messages in session state
    if 'document' not in st.session_state:
        st.session_state.document = ""
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Load content functions
    def load_website_content(url):
        loader = WebBaseLoader(url)
        documents = loader.load()
        content = ''.join([doc.page_content for doc in documents])
        return content

    def load_pdf_content(pdf_file):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
            tmp_pdf.write(pdf_file.read())
            tmp_pdf_path = tmp_pdf.name
        loader = PyPDFLoader(tmp_pdf_path)
        documents = loader.load()
        content = ''.join([doc.page_content for doc in documents])
        return content

    def load_youtube_content(url):
        loader = YoutubeLoader.from_youtube_url(url, language=['en'])
        documents = loader.load()
        content = ''.join([doc.page_content for doc in documents])
        return content

    # Source selection
    source = st.selectbox(source_label, ["Website", "PDF", "YouTube"])

    # Load the information source based on user selection
    if source == "Website":
        website_url = st.text_input(website_prompt)
        if st.button(load_button_label) and website_url:
            st.session_state.document = load_website_content(website_url)
            st.write(loaded_msg)
    elif source == "PDF":
        pdf_file = st.file_uploader(pdf_prompt, type="pdf")
        if st.button(load_button_label) and pdf_file:
            st.session_state.document = load_pdf_content(pdf_file)
            st.write(loaded_msg)
    elif source == "YouTube":
        youtube_url = st.text_input(youtube_prompt)
        if st.button(load_button_label) and youtube_url:
            st.session_state.document = load_youtube_content(youtube_url)
            st.write(loaded_msg)

    # Chat interaction - only if a document is loaded
    if st.session_state.document:
        # Display chat history
        for role, message in st.session_state.messages:
            if role == 'user':
                st.write(f"**Usuário:** {message}")
            elif role == 'assistant':
                st.write(f"**VeritAI:** {message}")

        # Input for new message with a unique key to avoid resetting issues
        user_input = st.text_input(question_label, key="user_input")

        # Process the input only if the send button is clicked
        if st.button(send_button_label) and user_input:
            # Add user's question to messages
            st.session_state.messages.append(('user', user_input))
            
            # Get the chatbot's response
            response = get_bot_response(st.session_state.messages, st.session_state.document)
            
            # Add bot's response to messages
            if response:
                st.session_state.messages.append(('assistant', response))
                
            # Do not attempt to reset the input field directly

    # Final message
    st.write("Thank you for using VeritAI!" if st.session_state.language == "en" else "Muito obrigado por usar o VeritAI!")
    st.markdown('[Made with love by Murilo Krominski 💖](https://murilokrominski.github.io/autor.htm)', unsafe_allow_html=True)
