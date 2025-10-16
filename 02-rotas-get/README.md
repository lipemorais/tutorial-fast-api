# Etapa 02: Rotas GET

Nesta etapa você vai aprender a criar rotas GET mais dinâmicas, recebendo parâmetros de diferentes formas.

## Objetivo

Aprender a:
- Criar múltiplas rotas GET
- Receber path parameters (parâmetros na URL)
- Receber query parameters (parâmetros após o ?)
- Trabalhar com valores padrão
- Usar tipagem Python para validação automática

## Conceitos

### Path Parameters vs Query Parameters

**Path Parameters** - Fazem parte da URL:
```
/livros/1
       ↑ ID do livro
```

**Query Parameters** - Vêm após o `?`:
```
/livros/buscar?q=python&ano=2020
               ↑ parâmetros
```

### Quando usar cada um?

- **Path Parameters**: Para identificar um recurso específico (ex: ID)
- **Query Parameters**: Para filtros, buscas, paginação, opções

## O Código

Criamos uma API simples de livros com 5 rotas:

### 1. Rota raiz - Informações da API

```python
@app.get("/")
def raiz():
    return {
        "mensagem": "Bem-vindo à API de Livros!",
        "endpoints": {...}
    }
```

### 2. Listar todos os livros

```python
@app.get("/livros")
def listar_livros():
    return {"total": len(livros), "livros": livros}
```

### 3. Obter livro por ID (Path Parameter)

```python
@app.get("/livros/{livro_id}")
def obter_livro(livro_id: int):
    # O {livro_id} da rota vira o parâmetro livro_id da função
    # O tipo int faz validação automática!
    ...
```

**Como funciona a tipagem:**
- Se você acessar `/livros/1` → funciona (1 é um número)
- Se você acessar `/livros/abc` → FastAPI retorna erro automaticamente!

### 4. Buscar por título (Query Parameter)

```python
@app.get("/livros/buscar/titulo")
def buscar_por_titulo(q: str = ""):
    # q vem de ?q=termo_busca
    # O = "" define um valor padrão
    ...
```

**Exemplo de uso:**
```
/livros/buscar/titulo?q=python
```

### 5. Filtrar por ano (Múltiplos Query Parameters)

```python
@app.get("/livros/filtrar/ano")
def filtrar_por_ano(ano_min: int = 2000, ano_max: int = 2024):
    # Múltiplos parâmetros com valores padrão
    ...
```

**Exemplo de uso:**
```
/livros/filtrar/ano?ano_min=2015&ano_max=2020
```

Se não passar os parâmetros, usa os padrões (2000 e 2024).

## Como executar

### 1. Execute o servidor (a partir da raiz do projeto)

```bash
uv run fastapi dev 02-rotas-get/main.py
```

### 2. Teste as rotas

Como todas as rotas deste capítulo são GET, você pode testá-las de duas formas:

#### Opção 1: Direto no navegador

**Rotas simples no navegador:**
- http://localhost:8000/ - Informações da API
- http://localhost:8000/livros - Lista todos os livros
- http://localhost:8000/livros/1 - Livro com ID 1
- http://localhost:8000/livros/buscar/titulo?q=python - Busca por "python"
- http://localhost:8000/livros/filtrar/ano?ano_min=2015&ano_max=2020 - Filtra por ano

💡 **Dica:** Basta colar essas URLs no navegador e apertar Enter!

#### Opção 2: Documentação interativa (recomendado)

Acesse: http://localhost:8000/docs

Agora você verá **5 rotas** listadas! Vamos testar cada uma usando a interface:

#### 1. GET / - Informações da API
- Clique na rota `GET /`
- Clique em **"Try it out"**
- Clique em **"Execute"**
- Veja as informações sobre todos os endpoints disponíveis

#### 2. GET /livros - Listar todos os livros
- Expanda `GET /livros`
- Clique em **"Try it out"**
- Clique em **"Execute"**
- Veja a lista com 3 livros pré-cadastrados

#### 3. GET /livros/{livro_id} - Obter livro específico (Path Parameter)
- Expanda `GET /livros/{livro_id}`
- Clique em **"Try it out"**
- No campo `livro_id`, digite: **1**
- Clique em **"Execute"**
- Veja os detalhes do livro com ID 1

**Experimente:**
- Teste com `livro_id = 2` e depois `3`
- Teste com `livro_id = 99` - veja a mensagem de "não encontrado"
- Teste com `livro_id = abc` - veja o erro de validação automático!

#### 4. GET /livros/buscar/titulo - Buscar por título (Query Parameter)
- Expanda `GET /livros/buscar/titulo`
- Clique em **"Try it out"**
- No campo `q`, digite: **python**
- Clique em **"Execute"**
- Veja apenas livros que contêm "python" no título

**Experimente:**
- Busque por "web"
- Busque por "java" (não encontrará nada)
- Deixe vazio e veja todos os livros

#### 5. GET /livros/filtrar/ano - Filtrar por ano (Múltiplos Query Parameters)
- Expanda `GET /livros/filtrar/ano`
- Clique em **"Try it out"**
- Em `ano_min`, digite: **2015**
- Em `ano_max`, digite: **2020**
- Clique em **"Execute"**
- Veja apenas livros publicados entre 2015 e 2020

**Experimente:**
- Teste com `ano_min = 2020` e `ano_max = 2024`
- Deixe os valores padrão e veja o que acontece

### 3. Testando validação automática

O FastAPI valida automaticamente os tipos! Vamos ver isso na prática usando o `/docs`:

#### Teste 1: ID inválido
- Vá em `GET /livros/{livro_id}`
- Em `livro_id`, tente digitar: **abc**
- Clique em **"Execute"**
- Você verá um erro `422 Unprocessable Entity` explicando que esperava um número inteiro!

#### Teste 2: Ano inválido
- Vá em `GET /livros/filtrar/ano`
- Em `ano_min`, tente digitar: **xyz**
- Clique em **"Execute"**
- Novamente, erro de validação automático!

**Observe:** O FastAPI não deixa nem chegar na sua função se os dados estiverem errados. Ele valida tudo automaticamente! 🛡️

## Experimente (e teste no /docs!)

1. **Adicione mais livros** à lista inicial
   - Adicione 2-3 livros novos
   - Teste no `/docs` se aparecem na listagem

2. **Crie uma nova rota** `/livros/autor/{nome}` que busca por autor
   ```python
   @app.get("/livros/autor/{nome}")
   def buscar_por_autor(nome: str):
       # Seu código aqui
       ...
   ```
   - Veja a nova rota aparecer automaticamente no `/docs`
   - Teste buscando por "Luciano Ramalho"

3. **Adicione paginação**: parâmetros `limite` e `pagina`
   ```python
   @app.get("/livros/paginado")
   def listar_paginado(pagina: int = 1, limite: int = 10):
       # Seu código aqui
       ...
   ```
   - Teste diferentes valores de página e limite no `/docs`

4. **Combine filtros**: busque por título E ano juntos
   - Use query parameters múltiplos
   - Teste no `/docs` com diferentes combinações

## Diferenças da Etapa Anterior

- ✅ Múltiplas rotas ao invés de apenas uma
- ✅ Path parameters com tipagem
- ✅ Query parameters com valores padrão
- ✅ Validação automática de tipos
- ✅ Metadados da API (title, description, version)
- ✅ Documentação nas funções (aparecem no /docs)

## Próxima Etapa

Até agora só **lemos** dados. Na próxima etapa vamos aprender a **receber e criar** dados usando POST!

➡️ [Etapa 03: Rotas POST](../03-rotas-post/)

## Referências

- [FastAPI - Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [FastAPI - Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
