# Etapa 01: Hello World

Bem-vindo à primeira etapa do tutorial! Aqui você vai criar sua primeira API em apenas 5 linhas de código.

## Objetivo

Aprender a:
- Criar uma aplicação FastAPI básica
- Definir uma rota GET simples
- Executar o servidor de desenvolvimento
- Acessar a documentação automática

## O que é uma API?

API (Application Programming Interface) é um jeito de diferentes programas conversarem entre si. Uma API REST usa HTTP (o mesmo protocolo da web) para enviar e receber dados, geralmente em formato JSON.

## O que é FastAPI?

FastAPI é um framework Python moderno para criar APIs de forma rápida e fácil. Ele:
- Valida dados automaticamente
- Gera documentação automática
- É muito rápido (daí o nome!)
- Usa tipagem Python moderna

## O Código

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz():
    return {"mensagem": "Olá, Python Brasil 2025! 🐍"}
```

### Explicando linha por linha

1. **`from fastapi import FastAPI`** - Importa a classe principal do FastAPI
2. **`app = FastAPI()`** - Cria uma instância da aplicação (nosso servidor)
3. **`@app.get("/")`** - Decorador que define uma rota GET no caminho raiz "/"
4. **`def raiz():`** - Função que será executada quando alguém acessar essa rota
5. **`return {...}`** - Retorna um dicionário Python que será convertido para JSON automaticamente

## Como executar

### 1. Execute o servidor (a partir da raiz do projeto)

```bash
uv run fastapi dev 01-hello-world/main.py
```

O que significa cada parte:
- `uv run` - executa o comando usando o ambiente virtual do projeto
- `fastapi dev` - comando do FastAPI CLI para desenvolvimento
- `main.py` - arquivo Python que contém sua aplicação
- O modo `dev` já inclui auto-reload automático quando você modificar o código

### 2. Acesse a API

Abra seu navegador em: http://localhost:8000

Você deve ver:
```json
{
  "mensagem": "Olá, Python Brasil 2025! 🐍"
}
```

### 3. Explore a documentação automática (Swagger UI)

**Essa é a mágica do FastAPI!** Acesse: http://localhost:8000/docs

A documentação foi gerada automaticamente sem você escrever uma linha de documentação! 🎉

#### Como usar a documentação interativa:

1. **Veja sua rota listada:**
   - Você verá uma seção com `GET /` (sua rota raiz)
   - Clique nela para expandir

2. **Teste a rota:**
   - Clique no botão **"Try it out"**
   - Clique em **"Execute"**
   - Veja a resposta aparecer na tela!

3. **O que você verá:**
   - **Request URL**: O endereço que foi chamado
   - **Response body**: O JSON que a API retornou
   - **Response headers**: Informações técnicas da resposta
   - **Status code**: `200` significa sucesso!

#### Documentação alternativa (ReDoc)

Se quiser um formato diferente: http://localhost:8000/redoc

## Experimente

Modifique o código e teste usando a documentação interativa (`/docs`):

1. **Mude a mensagem:**
   - Altere a mensagem retornada para algo seu
   - Salve o arquivo (o servidor recarrega automaticamente!)
   - Atualize a página `/docs` e teste novamente

2. **Adicione mais campos:**
   ```python
   return {
       "mensagem": "Olá!",
       "autor": "Seu Nome",
       "ano": 2025
   }
   ```
   - Veja como o JSON retornado muda no `/docs`

3. **Crie uma segunda rota:**
   ```python
   @app.get("/sobre")
   def sobre():
       return {"nome": "Seu Nome", "idade": 25}
   ```
   - Veja a nova rota aparecer automaticamente no `/docs`
   - Teste ela clicando em "Try it out"!

## Próxima Etapa

Na próxima etapa você vai aprender a criar rotas mais dinâmicas, recebendo parâmetros!

➡️ [Etapa 02: Rotas GET](../02-rotas-get/)

## Referências

- [FastAPI - First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [Uvicorn](https://www.uvicorn.org)
