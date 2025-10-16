# Etapa 04: Validação Avançada com Pydantic

from fastapi import FastAPI, HTTPException
from models import Usuario, Produto, RespostaPadrao

app = FastAPI(
    title="API com Validações Avançadas",
    description="Demonstração de validações Pydantic no FastAPI",
    version="1.0.0"
)

# "Banco de dados" em memória
usuarios = []
produtos = []


# ===== ROTAS DE USUÁRIOS =====

@app.get("/")
def raiz():
    """Informações sobre a API"""
    return {
        "mensagem": "API com validações avançadas",
        "recursos": {
            "usuarios": "/usuarios",
            "produtos": "/produtos"
        },
        "docs": "/docs"
    }


@app.post("/usuarios", response_model=RespostaPadrao)
def criar_usuario(usuario: Usuario):
    """
    Cria um novo usuário com validações:
    - Nome: 2-100 caracteres, sem números
    - Email: deve ser válido
    - Idade: 18-120 anos
    - Site: deve começar com http:// ou https://
    - Bio: máximo 500 caracteres, sem palavras proibidas
    """
    # Verifica se email já existe
    for u in usuarios:
        if u["email"] == usuario.email:
            raise HTTPException(
                status_code=400,
                detail="Email já cadastrado"
            )

    usuario_dict = usuario.model_dump()
    usuarios.append(usuario_dict)

    return RespostaPadrao(
        sucesso=True,
        mensagem="Usuário criado com sucesso!",
        dados=usuario_dict
    )


@app.get("/usuarios")
def listar_usuarios():
    """Lista todos os usuários"""
    return {
        "total": len(usuarios),
        "usuarios": usuarios
    }


# ===== ROTAS DE PRODUTOS =====

@app.post("/produtos", response_model=RespostaPadrao)
def criar_produto(produto: Produto):
    """
    Cria um novo produto com validações:
    - Nome: 3-100 caracteres, com pelo menos uma letra/número
    - Descrição: 10-1000 caracteres
    - Preço: maior que 0, máximo 1 milhão
    - Estoque: não pode ser negativo
    - Data de criação: gerada automaticamente
    """
    produto_dict = produto.model_dump()

    # Gera ID sequencial
    produto_dict["id"] = len(produtos) + 1

    produtos.append(produto_dict)

    return RespostaPadrao(
        sucesso=True,
        mensagem="Produto criado com sucesso!",
        dados=produto_dict
    )


@app.get("/produtos")
def listar_produtos(apenas_ativos: bool = True):
    """
    Lista produtos

    - **apenas_ativos**: se True, retorna apenas produtos ativos
    """
    if apenas_ativos:
        produtos_filtrados = [p for p in produtos if p.get("ativo", True)]
    else:
        produtos_filtrados = produtos

    return {
        "total": len(produtos_filtrados),
        "produtos": produtos_filtrados
    }


@app.get("/produtos/{produto_id}")
def obter_produto(produto_id: int):
    """Obtém um produto específico"""
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto

    raise HTTPException(
        status_code=404,
        detail="Produto não encontrado"
    )


# Para rodar: uvicorn main:app --reload
#
# Teste as validações em http://localhost:8000/docs
#
# Exemplos de dados inválidos para testar:
#
# Usuário com nome contendo números:
# {"nome": "João123", "email": "joao@example.com", "idade": 25}
#
# Usuário menor de idade:
# {"nome": "Ana Silva", "email": "ana@example.com", "idade": 17}
#
# Email inválido:
# {"nome": "Pedro Costa", "email": "pedro.email", "idade": 30}
#
# Site sem http/https:
# {"nome": "Maria", "email": "maria@example.com", "idade": 28, "site": "maria.com"}
#
# Produto com preço negativo:
# {"nome": "Teste", "descricao": "Produto de teste aqui", "preco": -10, "categoria": "Teste"}
#
# Produto com descrição muito curta:
# {"nome": "Teste", "descricao": "Curto", "preco": 100, "categoria": "Teste"}
