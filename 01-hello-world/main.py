# Etapa 01: Hello World - Sua primeira API com FastAPI

# Importando o FastAPI
from fastapi import FastAPI

# Criando uma instância do FastAPI
# Esta será a base da nossa aplicação
app = FastAPI()


# Criando nossa primeira rota
# O decorador @app.get("/") diz: "quando alguém acessar a raiz da API, execute esta função"
@app.get("/")
def raiz():
    """Rota raiz - retorna uma mensagem de boas-vindas"""
    return {"mensagem": "Olá, Python Brasil 2025! 🐍"}


# Para rodar esta API, execute no terminal:
# uvicorn main:app --reload
#
# Depois acesse no navegador:
# http://localhost:8000
#
# Para ver a documentação automática:
# http://localhost:8000/docs
