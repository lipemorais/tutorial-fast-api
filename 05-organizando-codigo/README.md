# Etapa 05: Organizando o Código

Parabéns por chegar até aqui! Nesta última etapa, você vai aprender a organizar seu código de forma profissional, preparando sua aplicação para crescer.

## Objetivo

Aprender a:
- Separar código em múltiplos arquivos
- Usar `APIRouter` para organizar rotas
- Estruturar projetos FastAPI escaláveis
- Organizar a documentação com tags

## Conceitos

### Por que organizar?

Até agora, todo o código estava em um único arquivo `main.py`. Isso funciona para tutoriais e projetos pequenos, mas fica difícil de manter quando a aplicação cresce.

**Problemas de ter tudo em um arquivo:**
- Difícil encontrar código específico
- Arquivo muito longo e difícil de navegar
- Difícil trabalhar em equipe (conflitos de merge)
- Difícil testar partes específicas

### APIRouter - A solução do FastAPI

`APIRouter` permite criar grupos de rotas que podem ser organizados em arquivos separados:

```python
from fastapi import APIRouter

router = APIRouter(
    prefix="/livros",  # Todas as rotas começam com /livros
    tags=["livros"]    # Agrupa na documentação
)

@router.get("/")  # Se torna /livros/
def listar_livros():
    ...
```

## Estrutura do Projeto

```
05-organizando-codigo/
├── main.py       # Configuração principal e rotas raiz
├── models.py     # Modelos Pydantic (validação)
└── routers.py    # Rotas organizadas por recurso
```

### 1. models.py - Modelos de Dados

Contém todos os modelos Pydantic:
- `Livro` - Modelo de livro com validações
- `Autor` - Modelo de autor
- `RespostaPadrao` - Modelo de resposta

**Por que separar:**
- Modelos podem ser reutilizados em múltiplos routers
- Facilita encontrar e modificar estruturas de dados
- Permite testar validações independentemente

### 2. routers.py - Rotas Organizadas

Contém dois routers:
- `router_livros` - Todas as operações com livros
- `router_autores` - Todas as operações com autores

Cada router tem CRUD completo:
- GET (listar e obter)
- POST (criar)
- PUT (atualizar)
- DELETE (remover)

**Por que separar:**
- Cada recurso tem seu próprio conjunto de rotas
- Fácil adicionar novos recursos sem afetar existentes
- Código relacionado fica junto

### 3. main.py - Aplicação Principal

Arquivo principal que:
- Cria a aplicação FastAPI
- Define configurações globais
- Inclui os routers
- Define rotas únicas (como raiz)

**Por que manter:**
- Ponto de entrada único da aplicação
- Configurações centralizadas
- Fácil ver todos os recursos disponíveis

## Como executar

### 1. Execute o servidor (a partir da raiz do projeto)

```bash
uv run fastapi dev 05-organizando-codigo/main.py
```

### 2. Explore a documentação

http://localhost:8000/docs

**Observe:**
- As rotas estão agrupadas por tags (raiz, livros, autores)
- Cada grupo pode ser expandido/recolhido
- Navegação muito mais organizada!

## Fluxo Completo de Teste

### Testando Livros

```bash
# Criar livro
curl -X POST http://localhost:8000/livros/ \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Python Fluente",
    "autor": "Luciano Ramalho",
    "ano": 2015,
    "paginas": 792
  }'

# Listar livros
curl http://localhost:8000/livros/

# Obter livro específico
curl http://localhost:8000/livros/1

# Atualizar livro
curl -X PUT http://localhost:8000/livros/1 \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Python Fluente - 2ª Edição",
    "autor": "Luciano Ramalho",
    "ano": 2022,
    "paginas": 1000
  }'

# Filtrar por disponibilidade
curl http://localhost:8000/livros/?disponivel=true

# Deletar livro
curl -X DELETE http://localhost:8000/livros/1
```

### Testando Autores

```bash
# Criar autor
curl -X POST http://localhost:8000/autores/ \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Luciano Ramalho",
    "email": "luciano@example.com",
    "biografia": "Programador Python há mais de 20 anos"
  }'

# Listar autores
curl http://localhost:8000/autores/

# Obter autor específico
curl http://localhost:8000/autores/1
```

## Entendendo o Código

### Como APIRouter Funciona

**1. Criar o router (routers.py):**
```python
router_livros = APIRouter(
    prefix="/livros",
    tags=["livros"]
)

@router_livros.get("/")  # Rota final: /livros/
def listar_livros():
    ...

@router_livros.get("/{id}")  # Rota final: /livros/{id}
def obter_livro(id: int):
    ...
```

**2. Incluir no app (main.py):**
```python
app.include_router(router_livros)
```

Pronto! Todas as rotas do router estão disponíveis no app.

### Benefícios das Tags

Tags organizam a documentação:

```python
router_livros = APIRouter(tags=["livros"])
router_autores = APIRouter(tags=["autores"])
```

No `/docs`, você verá seções separadas:
- **livros** - todas as rotas de livros
- **autores** - todas as rotas de autores

## Padrões de Organização

### Projeto Pequeno (este tutorial)
```
📁 projeto/
  - main.py
  - models.py
  - routers.py
```

### Projeto Médio
```
📁 projeto/
  📁 routers/
    - livros.py
    - autores.py
    - usuarios.py
  📁 models/
    - livros.py
    - autores.py
  - main.py
  - database.py
```

### Projeto Grande
```
📁 projeto/
  📁 app/
    📁 routers/
      - __init__.py
      - livros.py
      - autores.py
    📁 models/
      - __init__.py
      - livros.py
      - autores.py
    📁 schemas/
      - livros.py
      - autores.py
    📁 database/
      - connection.py
      - crud.py
    📁 core/
      - config.py
      - security.py
    - main.py
  📁 tests/
    - test_livros.py
    - test_autores.py
  - requirements.txt
  - README.md
```

## Experimente

1. **Adicione um novo recurso** - Crie um router para "empréstimos"
2. **Separe os routers** - Coloque cada router em um arquivo diferente (routers/livros.py, routers/autores.py)
3. **Adicione dependências** - Crie uma função de autenticação e use em rotas específicas
4. **Adicione middleware** - Registre logs de todas as requisições

## Próximos Passos

Você completou o tutorial básico! Agora você pode:

### 1. Adicionar Banco de Dados
```bash
# SQLAlchemy para banco de dados
uv pip install sqlalchemy

# Alembic para migrations
uv pip install alembic
```

### 2. Adicionar Autenticação
```bash
# OAuth2 com JWT
uv pip install python-jose[cryptography] passlib[bcrypt]
```

### 3. Testes Automatizados
```bash
# pytest para testes
uv pip install pytest httpx
```

### 4. Deploy em Produção
- Railway (https://railway.app)
- Render (https://render.com)
- Fly.io (https://fly.io)
- AWS/GCP/Azure

## Diferenças da Etapa Anterior

- ✅ Código separado em múltiplos arquivos
- ✅ APIRouter para organizar rotas
- ✅ Tags para organizar documentação
- ✅ Estrutura escalável
- ✅ Separação clara de responsabilidades
- ✅ Pronto para crescer!

## Conclusão

Você aprendeu os fundamentos do FastAPI:
- ✅ Criar rotas GET e POST
- ✅ Validar dados com Pydantic
- ✅ Usar documentação automática
- ✅ Organizar código profissionalmente

Agora você tem a base para construir suas próprias APIs!

## Recursos para Continuar Aprendendo

- [FastAPI - Tutorial Completo](https://fastapi.tiangolo.com/tutorial/)
- [Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)
- [Security](https://fastapi.tiangolo.com/tutorial/security/)
- [Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [Deployment](https://fastapi.tiangolo.com/deployment/)

---

**Parabéns por completar o tutorial!** 🎉

Se você gostou de FastAPI, considere:
- ⭐ Dar star no [repositório do FastAPI](https://github.com/tiangolo/fastapi)
- 📖 Ler a documentação completa
- 🚀 Construir seu próprio projeto
- 🤝 Contribuir com a comunidade Python
