# Etapa 05: Organizando o Código

"""
Este é um exemplo de como organizar uma aplicação FastAPI maior.

Estrutura:
- main.py: Arquivo principal, configura a aplicação
- models.py: Modelos Pydantic (validação de dados)
- routers.py: Rotas organizadas por recurso
"""

from fastapi import FastAPI
from routers import router_livros, router_autores

# Criando a aplicação principal
app = FastAPI(
    title="API de Biblioteca",
    description="API para gerenciar livros e autores de uma biblioteca",
    version="2.0.0",
    contact={
        "name": "Python Brasil 2025",
        "url": "https://pythonbrasil.org.br"
    }
)


# ===== ROTA RAIZ =====
# Esta fica no arquivo principal pois é única

@app.get("/", tags=["raiz"])
def raiz():
    """Informações sobre a API"""
    return {
        "nome": "API de Biblioteca",
        "versão": "2.0.0",
        "recursos": {
            "livros": "/livros",
            "autores": "/autores"
        },
        "documentacao": "/docs"
    }


# ===== INCLUINDO OS ROUTERS =====
# Aqui "montamos" as rotas organizadas nos routers

app.include_router(router_livros)
app.include_router(router_autores)


# ===== COMO FUNCIONA =====
#
# APIRouter permite organizar rotas por recurso/domínio:
#
# router_livros:
#   - prefix="/livros" -> todas as rotas começam com /livros
#   - tags=["livros"] -> agrupa na documentação
#   - Contém: GET, POST, PUT, DELETE para livros
#
# router_autores:
#   - prefix="/autores" -> todas as rotas começam com /autores
#   - tags=["autores"] -> agrupa na documentação
#   - Contém: GET, POST, PUT, DELETE para autores
#
# Quando fazemos app.include_router(router_livros), todas as rotas
# do router são adicionadas ao app principal.
#
# ===== VANTAGENS DESSA ORGANIZAÇÃO =====
#
# 1. Separação de responsabilidades
#    - models.py: estrutura dos dados
#    - routers.py: lógica das rotas
#    - main.py: configuração da aplicação
#
# 2. Código mais fácil de manter
#    - Cada arquivo tem um propósito claro
#    - Mais fácil encontrar e modificar código
#
# 3. Escalabilidade
#    - Para adicionar um novo recurso, basta criar um novo router
#    - Não precisamos mexer no código existente
#
# 4. Organização na documentação
#    - As tags agrupam rotas relacionadas no /docs
#    - Documentação mais clara e navegável
#
# ===== PRÓXIMOS PASSOS =====
#
# Em uma aplicação real, você poderia ter:
#
# 📁 minha_api/
#   📁 routers/
#     - livros.py
#     - autores.py
#     - usuarios.py
#   📁 models/
#     - livros.py
#     - autores.py
#     - usuarios.py
#   📁 database/
#     - connection.py
#     - crud.py
#   📁 tests/
#     - test_livros.py
#     - test_autores.py
#   - main.py
#   - config.py
#
# Para rodar: uvicorn main:app --reload
#
# Acesse:
# - http://localhost:8000/docs (documentação)
# - http://localhost:8000/livros (listar livros)
# - http://localhost:8000/autores (listar autores)
