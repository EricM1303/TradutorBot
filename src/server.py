from main import chain
from fastapi import FastAPI
import uvicorn
from langserve import add_routes

app = FastAPI(tittle="Minha IA", description="Traduza o texto que você quiser para qualquer idioma.") 

add_routes(app, chain, path="/tradutor") # Rota para acessar o servidor

