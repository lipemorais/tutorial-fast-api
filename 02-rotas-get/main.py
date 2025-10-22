# Etapa 02: Rotas GET - Trabalhando com parâmetros

from fastapi import FastAPI

app = FastAPI(
    title="API de Livros",
    description="Uma API simples para gerenciar uma lista de livros",
    version="1.0.0"
)

# Simulando um banco de dados em memória
# Em uma aplicação real, isso viria de um banco de dados
livros = [
    {"id": 1, "titulo": "Python Fluente", "autor": "Luciano Ramalho", "ano": 2015},
    {"id": 2, "titulo": "Pense em Python", "autor": "Allen Downey", "ano": 2016},
    {"id": 3, "titulo": "Automatize tarefas maçantes", "autor": "Al Sweigart", "ano": 2019},
]


@app.get("/")
def raiz():
    """Rota raiz - informações sobre a API"""
    return {
        "mensagem": "Bem-vindo à API de Livros!",
        "endpoints": {
            "livros": "/livros",
            "livro_por_id": "/livros/1",
            "buscar": "/livros/buscar/titulo?q=fluente",
        }
    }


@app.get("/livros")
def listar_livros():
    """Lista todos os livros disponíveis"""
    return {"total": len(livros), "livros": livros}


@app.get("/livros/{livro_id}")
def obter_livro(livro_id: int):
    """
    Obtém um livro específico pelo ID

    - **livro_id**: ID do livro (número inteiro)

    Este é um exemplo de Path Parameter - o parâmetro faz parte da URL
    """
    # Busca o livro na lista
    for livro in livros:
        if livro["id"] == livro_id:
            return livro

    # Se não encontrar, retorna erro
    return {"erro": "Livro não encontrado"}


@app.get("/livros/buscar/titulo")
def buscar_por_titulo(q: str = ""):
    """
    Busca livros por título

    - **q**: termo de busca (query parameter)

    Exemplo: /livros/buscar/titulo?q=python

    Este é um exemplo de Query Parameter - o parâmetro vem após o ?
    """
    if not q:
        return {"erro": "Por favor, forneça um termo de busca usando ?q=termo"}

    # Busca livros que contenham o termo no título (case-insensitive)
    resultados = [
        livro for livro in livros
        if q.lower() in livro["titulo"].lower()
    ]

    return {
        "termo_buscado": q,
        "total_encontrado": len(resultados),
        "livros": resultados
    }


@app.get("/livros/filtrar/ano")
def filtrar_por_ano(ano_min: int = 2000, ano_max: int = 2024):
    """
    Filtra livros por intervalo de anos

    - **ano_min**: ano mínimo (padrão: 2000)
    - **ano_max**: ano máximo (padrão: 2024)

    Exemplo: /livros/filtrar/ano?ano_min=2015&ano_max=2020

    Este exemplo mostra múltiplos query parameters com valores padrão
    """
    resultados = [
        livro for livro in livros
        if ano_min <= livro["ano"] <= ano_max
    ]

    return {
        "filtro": {"ano_min": ano_min, "ano_max": ano_max},
        "total_encontrado": len(resultados),
        "livros": resultados
    }


# Para rodar: uvicorn main:app --reload
#
# Experimente no navegador:
# - http://localhost:8000/livros
# - http://localhost:8000/livros/1
# - http://localhost:8000/livros/buscar/titulo?q=python
# - http://localhost:8000/livros/filtrar/ano?ano_min=2015
#
# Documentação automática:
# - http://localhost:8000/docs
