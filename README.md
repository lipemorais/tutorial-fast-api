# Tutorial FastAPI - Python Brasil 2025

Bem-vindo ao tutorial **"Começando com FastAPI: construa sua primeira API em Python"**!

Este é um tutorial prático e introdutório onde você vai aprender a criar sua primeira API REST usando FastAPI, um dos frameworks mais modernos e rápidos para desenvolvimento de APIs em Python.

## Sobre o Tutorial

**Duração:** 3h30
**Nível:** Iniciante
**Pré-requisitos:** Conhecimento básico de Python (funções, dicionários, listas)

## O que você vai aprender

- Criar seus primeiros endpoints (GET, POST)
- Validar dados de entrada com Pydantic
- Usar a documentação automática gerada pelo FastAPI
- Testar sua API localmente
- Organizar seu código de forma profissional

## Estrutura do Tutorial

Este tutorial está organizado em 5 etapas progressivas:

1. **[01-hello-world](./01-hello-world/)** - Sua primeira API em 5 linhas de código
2. **[02-rotas-get](./02-rotas-get/)** - Criando rotas GET com parâmetros
3. **[03-rotas-post](./03-rotas-post/)** - Recebendo dados com POST
4. **[04-validacao-pydantic](./04-validacao-pydantic/)** - Validação automática de dados
5. **[05-organizando-codigo](./05-organizando-codigo/)** - Estruturando seu projeto

Cada etapa contém:
- `README.md` com explicações detalhadas
- Código comentado e funcional
- Exemplos de uso

## Setup Inicial

### 1. Instalar o uv (gerenciador de pacotes Python)

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clonar ou baixar este repositório

```bash
git clone <url-do-repositorio>
cd tutorial-fast-api
```

### 3. Criar ambiente virtual e instalar dependências

```bash
uv sync
```

Depois ative o ambiente virtual:
```bash
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

> **Dica:** Você também pode usar `uv run <comando>` para executar comandos sem precisar ativar o ambiente virtual manualmente.

## Como usar este tutorial

1. Comece pela pasta `01-hello-world`
2. Leia o `README.md` de cada etapa
3. Execute o código
4. Experimente modificá-lo
5. Passe para a próxima etapa quando se sentir confortável

## Testando as APIs

Durante o tutorial, você vai aprender a testar suas APIs de três formas:

1. **Navegador** - Para rotas GET simples
2. **Documentação automática** - Swagger UI em `http://localhost:8000/docs`
3. **Linha de comando** - Com curl ou httpie (scripts incluídos em `scripts/`)

## Recursos Adicionais

- [Documentação oficial do FastAPI](https://fastapi.tiangolo.com)
- [Documentação do Pydantic](https://docs.pydantic.dev)
- [Tutorial de Python](https://docs.python.org/pt-br/3/tutorial/)

## Suporte

Se você encontrar algum problema ou tiver dúvidas:
- Abra uma issue neste repositório
- Pergunte durante o tutorial na Python Brasil 2025

## Próximos Passos

Após completar este tutorial, você pode explorar:
- Conexão com banco de dados (SQLAlchemy)
- Autenticação e autorização (OAuth2, JWT)
- Deploy em produção (Railway, Render, Fly.io)
- Testes automatizados (pytest)
- Async/await para operações concorrentes

---

**Bom aprendizado!** 🚀🐍
