"""
Project: VeritAI - Your Personal Oracle
Author: Murilo Krominski
Description: This Streamlit-based chatbot application allows users to upload or link content from various sources (Website, PDF, YouTube) 
and interact with a chatbot that provides responses based on the loaded content. Built with love to offer a bilingual experience.
"""

# Importando a biblioteca `os` para manipulação de variáveis de ambiente e `ChatGroq` para utilizar o modelo de chatbot
import os  # Biblioteca para manipulação de variáveis de ambiente e sistema
from langchain_groq import ChatGroq  # Importando ChatGroq para interagir com o modelo de chatbot Groq
from langchain.prompts import ChatPromptTemplate  # Importando ChatPromptTemplate para criar templates de prompts
from langchain_community.document_loaders import WebBaseLoader  # Loader para carregar conteúdo de sites
from langchain_community.document_loaders import YoutubeLoader  # Loader para carregar conteúdo de vídeos do YouTube
from langchain_community.document_loaders import PyPDFLoader  # Loader para carregar conteúdo de arquivos PDF
from IPython.display import display  # Exibição do widget de upload
from ipywidgets import FileUpload  # Widget de upload de arquivos
import tempfile  # Importa a biblioteca para criar arquivos temporários
import streamlit as st  # Biblioteca para criar aplicativos web interativos



# Definindo a chave da API necessária para acessar o serviço do ChatGroq
api_key = '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'

# Configurando a variável de ambiente para armazenar a chave da API do serviço de linguagem Groq
os.environ['GROQ_API_KEY'] = api_key  # Atribui a chave da API à variável de ambiente 'GROQ_API_KEY'

# Inicializando o objeto `ChatGroq` com um modelo de linguagem específico (neste caso, 'llama-3.1-70b-versatile')
chat = ChatGroq(model='llama-3.1-70b-versatile')  # Cria um objeto ChatGroq configurado com o modelo de linguagem desejado

# Definindo a função `resposta_bot`, que gera uma resposta do bot a partir de mensagens e de um documento informativo
def resposta_bot(mensagens, documento):
    # Definindo a mensagem inicial do sistema (mensagem que instrui o modelo sobre o papel e comportamento esperado)
    mensagem_system = '''Você é um assistente amigável chamado Bem-vindo ao VeritAI, criado por Murilo Krominski.
    Você utiliza as seguintes informações para formular as suas respostas: {informacoes}'''

    # Inicializando as mensagens do modelo com uma tupla representando a mensagem do sistema
    mensagens_modelo = [('system', mensagem_system)]

    # Adicionando as mensagens de entrada fornecidas pelo usuário na lista de mensagens do modelo
    mensagens_modelo += mensagens  # Combina as mensagens do usuário com a mensagem do sistema

    # Criando um prompt template a partir das mensagens, que servirá para organizar a entrada do modelo
    template = ChatPromptTemplate.from_messages(mensagens_modelo)  # Cria o template de prompt a partir das mensagens

    # Criando a cadeia de mensagens que será processada pelo modelo, passando as mensagens através do `ChatGroq`
    chain = template | chat  # Define o fluxo de mensagens do template para o modelo de chatbot

    # Invocando o modelo para obter a resposta, fornecendo o documento como contexto (parâmetro `informacoes`)
    return chain.invoke({'informacoes': documento}).content  # Retorna o conteúdo da resposta gerada pelo modelo

# Definindo a função `carrega_site` para carregar conteúdo de um site
def carrega_site():
    url_site = input('Digite a url do site: ')  # Solicita ao usuário a URL do site a ser carregado
    loader = WebBaseLoader(url_site)  # Inicializa o loader para o site
    lista_documentos = loader.load()  # Carrega o conteúdo do site em uma lista de documentos
    documento = ''  # Inicializa a variável que conterá todo o conteúdo do site
    for doc in lista_documentos:
        documento = documento + doc.page_content  # Concatena o conteúdo de cada página em `documento`
    return documento  # Retorna o conteúdo completo do site





# Definindo a função `carrega_pdf` para carregar conteúdo de um arquivo PDF via upload
def carrega_pdf():
  caminho = '/content/drive/MyDrive/curso_ia_python/arquivos/RoteiroViagemEgito.pdf'
  loader = PyPDFLoader(caminho)
  lista_documentos = loader.load()
  documento = ''
  for doc in lista_documentos:
    documento = documento + doc.page_content
  return documento

def carrega_pdf():
    uploaded_file = st.file_uploader("Faça o upload de um arquivo PDF", type="pdf")
    if uploaded_file is not None:
        # Inicializa o loader para o PDF
        loader = PyPDFLoader(uploaded_file)
        lista_documentos = loader.load()
        documento = ''
        for doc in lista_documentos:
            documento += doc.page_content
        return documento
    else:
        st.write("Por favor, faça o upload de um arquivo PDF.")  # Mensagem para o usuário
        return None  # Indica que não há documento carregado



# Definindo a função `carrega_youtube` para carregar conteúdo de um vídeo do YouTube
def carrega_youtube():
    url_youtube = input('Digite a url do vídeo: ')  # Solicita ao usuário a URL do vídeo
    loader = YoutubeLoader.from_youtube_url(url_youtube, language=['pt'])  # Inicializa o loader para o vídeo do YouTube
    lista_documentos = loader.load()  # Carrega o conteúdo do vídeo em uma lista de documentos
    documento = ''  # Inicializa a variável que conterá todo o conteúdo do vídeo
    for doc in lista_documentos:
        documento = documento + doc.page_content  # Concatena o conteúdo de cada segmento do vídeo em `documento`
    return documento  # Retorna o conteúdo completo do vídeo

# Exibindo uma mensagem de boas-vindas ao usuário
print('Bem-vindo ao VeritAI')

# Mensagem de seleção para o usuário escolher uma fonte de conteúdo
texto_selecao = '''Digite 1 se você quiser conversar com um site
Digite 2 se você quiser conversar com um pdf
Digite 3 se você quiser conversar com um vídeo de youtube '''

# Loop para obter a seleção do usuário e carregar o conteúdo correspondente
while True:
    selecao = input(texto_selecao)  # Solicita a seleção do usuário
    if selecao == '1':
        documento = carrega_site()  # Chama `carrega_site` se a seleção for '1'
        break
    if selecao == '2':
        documento = carrega_pdf()  # Chama `carrega_pdf` se a seleção for '2'
        break
    if selecao == '3':
        documento = carrega_youtube()  # Chama `carrega_youtube` se a seleção for '3'
        break
    print('Digite um valor entre 1 e 3')  # Mensagem de erro se o valor estiver fora do esperado

# Inicializando a lista de mensagens trocadas entre usuário e assistente
mensagens = []
while True:
    pergunta = input('Pergunta do Usuario(envie X para sair): ')  # Recebe a pergunta do usuário
    if pergunta.lower() == 'x':  # Verifica se o usuário deseja encerrar a conversa
        break  # Sai do loop se a entrada for 'x'
    mensagens.append(('user', pergunta))  # Adiciona a pergunta do usuário às mensagens
    resposta = resposta_bot(mensagens, documento)  # Gera a resposta do bot usando `resposta_bot`
    mensagens.append(('assistant', resposta))  # Adiciona a resposta do bot às mensagens
    print(f'Bot: {resposta}')  # Exibe a resposta do bot para o usuário

# Mensagem de encerramento ao sair do loop
print('Muito obrigado por usar o VeritAI')