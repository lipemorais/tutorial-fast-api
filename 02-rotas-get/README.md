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

### 1. Entre na pasta

```bash
cd 02-rotas-get
```

### 2. Execute o servidor

```bash
fastapi dev main.py
```

### 3. Teste as rotas

**No navegador:**
- http://localhost:8000/
- http://localhost:8000/livros
- http://localhost:8000/livros/1
- http://localhost:8000/livros/buscar/titulo?q=python
- http://localhost:8000/livros/filtrar/ano?ano_min=2015

**Com curl:**

```bash
# Listar todos
curl http://localhost:8000/livros

# Buscar por ID
curl http://localhost:8000/livros/1

# Buscar por título
curl "http://localhost:8000/livros/buscar/titulo?q=python"

# Filtrar por ano
curl "http://localhost:8000/livros/filtrar/ano?ano_min=2015&ano_max=2020"
```

**Dica:** As aspas no curl são necessárias quando a URL tem caracteres especiais como `?` e `&`.

### 4. Explore a documentação

Acesse http://localhost:8000/docs

Na documentação você pode:
- Ver todos os parâmetros de cada rota
- Ver os tipos esperados
- Testar cada rota clicando em "Try it out"
- Ver exemplos de resposta

## Testando validação automática

FastAPI valida automaticamente os tipos. Experimente:

**Acessar com ID inválido:**
```
http://localhost:8000/livros/abc
```

Você receberá um erro detalhado explicando que esperava um número inteiro!

**Acessar com ano inválido:**
```
http://localhost:8000/livros/filtrar/ano?ano_min=xyz
```

Novamente, erro de validação automático.

## Experimente

1. **Adicione mais livros** à lista inicial
2. **Crie uma nova rota** `/livros/autor/{nome}` que busca por autor
3. **Adicione paginação**: parâmetros `limite` e `pagina` para retornar livros em páginas
4. **Combine filtros**: crie uma rota que permita buscar por título E ano ao mesmo tempo

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
