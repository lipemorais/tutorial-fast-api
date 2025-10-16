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

### 2. Explore a documentação organizada

Acesse: http://localhost:8000/docs

**Observe a organização perfeita:**
- 🏠 **raiz** - Rota principal
- 📚 **livros** - Todas as operações de livros agrupadas
- ✍️ **autores** - Todas as operações de autores agrupadas
- Cada grupo pode ser expandido/recolhido
- Navegação muito mais clara!

## Testando a API Completa

### 1. Testando Livros (CRUD Completo)

#### Criar livro
1. Expanda a seção **livros**
2. Clique em `POST /livros/`
3. **"Try it out"**
4. Use este exemplo:
   ```json
   {
     "titulo": "Python Fluente",
     "autor": "Luciano Ramalho",
     "ano": 2015,
     "paginas": 792
   }
   ```
5. **"Execute"** → Sucesso! ✅

**Crie mais livros:**
- "Fluent Python 2nd Edition" - Luciano Ramalho - 2022 - 1000 páginas
- "Python Cookbook" - David Beazley - 2013 - 706 páginas

#### Listar todos os livros

**No navegador:** http://localhost:8000/livros/

**Ou no `/docs`:**
1. `GET /livros/` → **"Try it out"** → **"Execute"**
2. Veja todos os livros que você criou!

#### Filtrar livros disponíveis

**No navegador:** http://localhost:8000/livros/?disponivel=true

**Ou no `/docs`:**
1. `GET /livros/` → **"Try it out"**
2. Marque o checkbox `disponivel` como `true`
3. **"Execute"** → Veja apenas livros disponíveis

#### Obter livro específico

**No navegador:** http://localhost:8000/livros/1

**Ou no `/docs`:**
1. `GET /livros/{id}` → **"Try it out"**
2. Digite ID: **1**
3. **"Execute"**

#### Atualizar livro
1. `PUT /livros/{id}` → **"Try it out"**
2. ID: **1**
3. Edite para 2ª edição:
   ```json
   {
     "titulo": "Python Fluente - 2ª Edição",
     "autor": "Luciano Ramalho",
     "ano": 2022,
     "paginas": 1000
   }
   ```
4. **"Execute"** → Atualizado! ✅

#### Deletar livro
1. `DELETE /livros/{id}` → **"Try it out"**
2. ID: **3**
3. **"Execute"** → Deletado! ✅
4. Liste todos novamente - livro sumiu!

### 2. Testando Autores

#### Criar autor
1. Expanda a seção **autores**
2. `POST /autores/` → **"Try it out"**
3. Use este exemplo:
   ```json
   {
     "nome": "Luciano Ramalho",
     "email": "luciano@example.com",
     "biografia": "Programador Python há mais de 20 anos, palestrante e autor técnico"
   }
   ```
4. **"Execute"** → Criado! ✅

**Crie mais autores:**
- David Beazley - david@example.com - "Expert em Python e sistemas"
- Brett Slatkin - brett@example.com - "Software Engineer no Google"

#### Listar e obter autores

**No navegador:**
- http://localhost:8000/autores/ - Lista todos
- http://localhost:8000/autores/1 - Autor específico

**Ou no `/docs`:**
1. `GET /autores/` → Veja todos
2. `GET /autores/{id}` → Veja um específico

### 3. Observe a organização

**Veja como é fácil navegar:**
- Todas as rotas de livros estão juntas
- Todas as rotas de autores estão juntas
- Cada seção tem cor diferente
- Documentação clara e organizada

Imagine adicionar mais recursos (empréstimos, avaliações, etc.) - cada um teria sua própria seção!

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

## Experimente (e teste no /docs!)

1. **Adicione um novo recurso "empréstimos":**
   ```python
   router_emprestimos = APIRouter(
       prefix="/emprestimos",
       tags=["empréstimos"]
   )

   @router_emprestimos.post("/")
   def criar_emprestimo(livro_id: int, usuario: str):
       ...
   ```
   - Inclua no app: `app.include_router(router_emprestimos)`
   - Veja a nova seção aparecer no `/docs`!
   - Teste criando empréstimos

2. **Separe os routers em arquivos:**
   ```
   📁 routers/
     - livros.py    # Move router_livros para cá
     - autores.py   # Move router_autores para cá
   ```
   - Importe em main.py: `from routers.livros import router_livros`
   - Documentação continua funcionando perfeitamente!

3. **Adicione metadados às tags:**
   ```python
   app = FastAPI(
       openapi_tags=[
           {"name": "livros", "description": "Operações com livros"},
           {"name": "autores", "description": "Gerenciamento de autores"},
       ]
   )
   ```
   - Veja as descrições aparecerem no `/docs`

4. **Adicione parâmetros comuns:**
   ```python
   @router_livros.get("/")
   def listar_livros(
       skip: int = 0,
       limit: int = 10,
       disponivel: bool = None
   ):
       ...
   ```
   - Teste diferentes combinações de paginação no `/docs`

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
