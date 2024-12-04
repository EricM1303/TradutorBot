from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser # Serve para iterar de forma mais efetiva sob JSON da resposta
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
chave_api = os.getenv("API_KEY") # Importa a chave do .env

modelo = ChatGroq(model="llama3-8b-8192")
parser = StrOutputParser()

template_mensagem = ChatPromptTemplate.from_messages([
    ("system", "Traduza o texto a seguir para {idioma}, ele pode ser do tipo UTF-8 também, e caso não digite um idioma existente, retorne uma mensagem de 'idioma inválido'."), 
    ("user", "{texto}"),
])

chain = template_mensagem | modelo | parser # Fará com que os códigos sejam rodados do input (Ínicio do código) até o output (Final do código).