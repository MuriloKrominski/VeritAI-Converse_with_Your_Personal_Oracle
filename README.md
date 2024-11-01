# VeritAI - Seu Oráculo Pessoal - Por Murilo Krominski
# VeritAI - Your Personal Oracle - By Murilo Krominski

VeritAI é um assistente virtual baseado em inteligência artificial que permite aos usuários carregar conteúdos de diferentes fontes (como sites, arquivos PDF e vídeos do YouTube) e interagir com um chatbot que gera respostas baseadas nas informações carregadas. A aplicação oferece suporte em dois idiomas: inglês e português, proporcionando uma experiência personalizada para cada usuário.

VeritAI is an AI-based virtual assistant that allows users to load content from different sources (such as websites, PDF files, and YouTube videos) and interact with a chatbot that generates responses based on the loaded information. The application supports both English and Portuguese, providing a personalized experience for each user.

## 🎯 Funcionalidades / Features

- **Suporte a Multilinguagem / Multilanguage Support**: Permite ao usuário escolher entre inglês e português no início. / Allows users to choose between English and Portuguese at startup.
- **Carregamento de Conteúdo / Content Loading**: Carrega informações a partir de / Loads information from:
  - Websites
  - Arquivos PDF / PDF files
  - Vídeos do YouTube / YouTube videos
- **Interação com Chatbot / Chatbot Interaction**: O usuário pode fazer perguntas e receber respostas do chatbot com base nas informações carregadas. / Users can ask questions and receive responses from the chatbot based on the loaded information.

## 🚀 Tecnologias Utilizadas / Technologies Used

- **[LangChain](https://github.com/hwchase17/langchain)**: Framework para gerenciamento de prompts e integração com modelos de linguagem. / Framework for prompt management and integration with language models.
- **LangChain-Groq**: Conexão do LangChain com a API da Groq para acesso a modelos de linguagem. / Connects LangChain to the Groq API to access language models.
- **LangChain-Community**: Ferramentas adicionais para carregamento de documentos de sites, PDFs e YouTube. / Additional tools for loading documents from websites, PDFs, and YouTube.
- **Streamlit**: Interface interativa para o usuário. / Interactive user interface.
- **python-dotenv**: Gerenciamento seguro de variáveis de ambiente. / Secure environment variable management.

## 📁 Estrutura do Projeto / Project Structure

```
meu_projeto/
├── app.py             # Arquivo principal da aplicação em Streamlit / Main application file in Streamlit
├── .env               # Contém a chave de API (não incluído no GitHub) / Contains the API key (not included in GitHub)
├── .env.example       # Exemplo de .env, sem a chave real, para compartilhar / Example .env without the real key for sharing
├── .gitignore         # Instruções para o Git ignorar o arquivo .env / Instructions for Git to ignore the .env file
└── requirements.txt   # Dependências do projeto / Project dependencies
```

## 📋 Pré-requisitos / Prerequisites

1. **Python 3.7+** instalado / installed.
2. **Chave de API da Groq** para acessar o modelo de linguagem. Obtenha uma chave em [Groq API Console](https://console.groq.com/keys).  
   **Groq API Key** to access the language model. Get a key at [Groq API Console](https://console.groq.com/keys).

## ⚙️ Configuração e Execução do Projeto / Project Setup and Execution

### 1. Clone o Repositório / Clone the Repository

```bash
git clone https://github.com/MuriloKrominski/VeritAI-Converse_with_Your_Personal_Oracle.git
cd VeritAI-Converse_with_Your_Personal_Oracle
```

### 2. Instale as Dependências / Install Dependencies

Use o comando abaixo para instalar todas as dependências listadas no `requirements.txt`:  
Use the command below to install all dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Configure as Variáveis de Ambiente / Set Up Environment Variables

Para rodar o projeto, você precisa criar um arquivo `.env` com sua própria chave de API.  
To run the project, you need to create a `.env` file with your own API key.

1. Copie o arquivo `.env.example` para `.env`:  
   Copy the `.env.example` file to `.env`:

   ```bash
   cp .env.example .env
   ```

2. Abra o arquivo `.env` e substitua `your_api_key_here` pela sua chave de API GROQ real.  
   Open the `.env` file and replace `your_api_key_here` with your actual GROQ API key.

   ```plaintext
   GROQ_API_KEY='sua_chave_de_api_aqui'
   GROQ_API_KEY='your_actual_api_key_here'
   ```

### 4. Inicie a Aplicação / Start the Application

No diretório do projeto, execute o seguinte comando para iniciar a aplicação:  
In the project directory, run the following command to start the application:

```bash
streamlit run app.py
```

Acesse a aplicação no navegador através do endereço exibido pelo Streamlit (geralmente `http://localhost:8501`).  
Access the application in your browser at the address displayed by Streamlit (usually `http://localhost:8501`).

## 🌐 Como Usar / How to Use

1. Escolha seu idioma no início (inglês ou português).  
   Choose your language at the beginning (English or Portuguese).
2. Selecione a fonte de informação para carregar:  
   Select the information source to load:
   - URL de um site / Website URL
   - Arquivo PDF / PDF file
   - URL de um vídeo do YouTube / YouTube video URL
3. Faça perguntas ao chatbot, que responderá com base nas informações carregadas.  
   Ask questions to the chatbot, which will respond based on the loaded information.

## 🎉 Agradecimento / Acknowledgments

Se você gostou deste projeto, considere dar uma estrela! [VeritAI no GitHub](https://murilokrominski.github.io)  
If you enjoyed this project, please consider giving it a star! [VeritAI on GitHub](https://murilokrominski.github.io)

---

Feito com ❤️ por **Murilo Krominski**.  
Made with ❤️ by **Murilo Krominski**.