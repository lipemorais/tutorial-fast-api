# Rotas organizadas por recurso

from fastapi import APIRouter, HTTPException
from models import Livro, Autor, RespostaPadrao

# ===== ROUTER DE LIVROS =====
# APIRouter permite agrupar rotas relacionadas
# Depois, incluímos este router no app principal

router_livros = APIRouter(
    prefix="/livros",  # Todas as rotas começam com /livros
    tags=["livros"]    # Agrupa na documentação
)

# "Banco de dados" em memória
livros_db = []
livros_id_counter = 1


@router_livros.get("/")
def listar_livros(disponivel: bool | None = None):
    """
    Lista todos os livros

    - **disponivel**: Filtra por disponibilidade (opcional)
    """
    if disponivel is None:
        return {"total": len(livros_db), "livros": livros_db}

    livros_filtrados = [l for l in livros_db if l["disponivel"] == disponivel]
    return {"total": len(livros_filtrados), "livros": livros_filtrados}


@router_livros.get("/{livro_id}")
def obter_livro(livro_id: int):
    """Obtém um livro específico pelo ID"""
    for livro in livros_db:
        if livro["id"] == livro_id:
            return livro

    raise HTTPException(status_code=404, detail="Livro não encontrado")


@router_livros.post("/", response_model=RespostaPadrao)
def criar_livro(livro: Livro):
    """Cria um novo livro"""
    global livros_id_counter

    livro_dict = livro.model_dump()
    livro_dict["id"] = livros_id_counter
    livros_id_counter += 1

    livros_db.append(livro_dict)

    return RespostaPadrao(
        sucesso=True,
        mensagem="Livro criado com sucesso!",
        dados=livro_dict
    )


@router_livros.put("/{livro_id}", response_model=RespostaPadrao)
def atualizar_livro(livro_id: int, livro: Livro):
    """Atualiza um livro existente"""
    for i, l in enumerate(livros_db):
        if l["id"] == livro_id:
            livro_dict = livro.model_dump()
            livro_dict["id"] = livro_id
            livros_db[i] = livro_dict

            return RespostaPadrao(
                sucesso=True,
                mensagem="Livro atualizado com sucesso!",
                dados=livro_dict
            )

    raise HTTPException(status_code=404, detail="Livro não encontrado")


@router_livros.delete("/{livro_id}", response_model=RespostaPadrao)
def deletar_livro(livro_id: int):
    """Remove um livro"""
    for i, l in enumerate(livros_db):
        if l["id"] == livro_id:
            livro_removido = livros_db.pop(i)
            return RespostaPadrao(
                sucesso=True,
                mensagem="Livro removido com sucesso!",
                dados=livro_removido
            )

    raise HTTPException(status_code=404, detail="Livro não encontrado")


# ===== ROUTER DE AUTORES =====

router_autores = APIRouter(
    prefix="/autores",
    tags=["autores"]
)

# "Banco de dados" em memória
autores_db = []
autores_id_counter = 1


@router_autores.get("/")
def listar_autores():
    """Lista todos os autores"""
    return {"total": len(autores_db), "autores": autores_db}


@router_autores.get("/{autor_id}")
def obter_autor(autor_id: int):
    """Obtém um autor específico pelo ID"""
    for autor in autores_db:
        if autor["id"] == autor_id:
            return autor

    raise HTTPException(status_code=404, detail="Autor não encontrado")


@router_autores.post("/", response_model=RespostaPadrao)
def criar_autor(autor: Autor):
    """Cria um novo autor"""
    global autores_id_counter

    # Verifica se email já existe
    for a in autores_db:
        if a["email"] == autor.email:
            raise HTTPException(
                status_code=400,
                detail="Email já cadastrado"
            )

    autor_dict = autor.model_dump()
    autor_dict["id"] = autores_id_counter
    autores_id_counter += 1

    autores_db.append(autor_dict)

    return RespostaPadrao(
        sucesso=True,
        mensagem="Autor criado com sucesso!",
        dados=autor_dict
    )


@router_autores.put("/{autor_id}", response_model=RespostaPadrao)
def atualizar_autor(autor_id: int, autor: Autor):
    """Atualiza um autor existente"""
    for i, a in enumerate(autores_db):
        if a["id"] == autor_id:
            autor_dict = autor.model_dump()
            autor_dict["id"] = autor_id
            autores_db[i] = autor_dict

            return RespostaPadrao(
                sucesso=True,
                mensagem="Autor atualizado com sucesso!",
                dados=autor_dict
            )

    raise HTTPException(status_code=404, detail="Autor não encontrado")


@router_autores.delete("/{autor_id}", response_model=RespostaPadrao)
def deletar_autor(autor_id: int):
    """Remove um autor"""
    for i, a in enumerate(autores_db):
        if a["id"] == autor_id:
            autor_removido = autores_db.pop(i)
            return RespostaPadrao(
                sucesso=True,
                mensagem="Autor removido com sucesso!",
                dados=autor_removido
            )

    raise HTTPException(status_code=404, detail="Autor não encontrado")
