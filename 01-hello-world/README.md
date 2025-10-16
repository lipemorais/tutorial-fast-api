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

### 1. Entre na pasta desta etapa

```bash
cd 01-hello-world
```

### 2. Execute o servidor

```bash
fastapi dev main.py
```

O que significa cada parte:
- `fastapi dev` - comando do FastAPI CLI para desenvolvimento
- `main.py` - arquivo Python que contém sua aplicação
- O modo `dev` já inclui auto-reload automático quando você modificar o código

### 3. Acesse a API

Abra seu navegador em: http://localhost:8000

Você deve ver:
```json
{
  "mensagem": "Olá, Python Brasil 2025! 🐍"
}
```

### 4. Explore a documentação automática

FastAPI gera documentação interativa automaticamente! Acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

Na página `/docs` você pode:
- Ver todas as rotas disponíveis
- Testar as rotas diretamente pelo navegador
- Ver a estrutura dos dados

## Testando com curl

Se preferir linha de comando:

```bash
curl http://localhost:8000
```

## Experimente

Modifique o código para:
1. Mudar a mensagem retornada
2. Adicionar mais campos no dicionário (ex: `"autor": "Seu Nome"`)
3. Criar uma segunda rota em `@app.get("/sobre")` com informações sobre você

## Próxima Etapa

Na próxima etapa você vai aprender a criar rotas mais dinâmicas, recebendo parâmetros!

➡️ [Etapa 02: Rotas GET](../02-rotas-get/)

## Referências

- [FastAPI - First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [Uvicorn](https://www.uvicorn.org)
