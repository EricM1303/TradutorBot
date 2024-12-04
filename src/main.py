from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
chave_api = os.getenv("API_KEY") # Importa a chave do .env

modelo = ChatGroq(model="llama3-8b-8192")
parser = StrOutputParser()