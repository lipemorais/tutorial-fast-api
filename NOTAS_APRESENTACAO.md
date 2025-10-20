# Notas para Apresentação - Tutorial FastAPI Python Brasil 2025

**Duração:** 3h30 (210 minutos)
**Data:** 23/10/2025, 09:00–12:30
**Local:** Impacta - Sala 206

---

## Checklist Pré-Tutorial

### Dia Anterior
- [ ] Testar todas as etapas do tutorial
- [ ] Verificar se as dependências estão atualizadas
- [ ] Revisar este documento

### 1 Hora Antes
- [ ] Chegar na sala e testar equipamento
- [ ] Testar projetor/tela
- [ ] Testar conexão com internet
- [ ] Abrir todos os terminais e abas necessárias
- [ ] Colocar fonte grande no terminal (legibilidade)
- [ ] Desligar notificações do sistema

### Terminais/Abas Pré-Abertos
1. Terminal para rodar fastapi
2. Navegador com abas:
   - http://localhost:8000/docs (Swagger)
   - http://localhost:8000/redoc
   - https://fastapi.tiangolo.com (documentação oficial)
3. Editor de código com o projeto aberto

---

## Estrutura da Apresentação (210 min)

### 🎯 Abertura (10 min) - 09:00-09:10
**Objetivos:**
- Apresentar-se brevemente
- Nivelar expectativas
- Fazer participantes se sentirem à vontade

**Roteiro:**
1. Apresentação pessoal (2 min)
   - Seu nome e experiência com Python/FastAPI
   - Por que você gosta de FastAPI

2. Visão geral do tutorial (3 min)
   - "Vamos construir APIs do zero"
   - "Foco 100% prático"
   - "Vocês vão sair daqui com uma API funcionando"

3. Verificar pré-requisitos (5 min)
   - Perguntar: "Quem já programa em Python?"
   - Perguntar: "Quem já trabalhou com APIs?"
   - Ajudar quem precisar instalar uv

**Frase de abertura sugerida:**
> "Bom dia! Eu sou o Felipe e nas próximas 3h30 vamos aprender a criar APIs com FastAPI. A ideia é ser bem prático - você vai codar comigo, testar, quebrar, consertar. No final, vocês vão ter uma API completa rodando na máquina de vocês!"

---

### 📖 Introdução Teórica (10 min) - 09:10-09:20
**Objetivos:**
- Contextualizar o que é API
- Explicar por que FastAPI

**Tópicos:**
1. O que é uma API? (3 min)
   - "Forma de programas conversarem"
   - Analogia: "Como um garçom entre você e a cozinha"
   - Exemplo real: app de clima consultando API de meteorologia

2. O que é REST? (2 min)
   - Usa HTTP (como sites)
   - Métodos: GET (ler), POST (criar), PUT (atualizar), DELETE (remover)
   - Retorna JSON (formato de dados)

3. Por que FastAPI? (5 min)
   - Rápido (performance)
   - Fácil de aprender
   - Validação automática
   - Documentação automática (esse é o GRANDE diferencial!)
   - Usado por empresas reais (Microsoft, Uber, Netflix)

**Slides/Demo:**
- Mostrar exemplo de JSON no navegador
- Mostrar rapidamente como é a doc automática

---

### ⚙️ Setup do Ambiente (15 min) - 09:20-09:35
**Objetivos:**
- Todo mundo com ambiente funcionando
- Instalar dependências

**Roteiro:**
1. Instalar uv (se necessário) (5 min)
   ```bash
   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
   - Compartilhar o comando no chat/slides
   - Circular pela sala ajudando

2. Clonar/baixar o repositório (3 min)
   ```bash
   git clone <url-do-repositorio>
   # OU baixar o ZIP e extrair
   ```
   - Fornecer a URL do repositório

3. Entrar na pasta do projeto (1 min)
   ```bash
   cd tutorial-fast-api
   ```

4. Instalar dependências com uv sync (6 min)
   ```bash
   uv sync
   ```
   - Isso cria o ambiente virtual E instala as dependências automaticamente
   - Não precisa ativar manualmente, use `uv run` para executar comandos

**Dica:** Enquanto instala, explicar:
- `uv`: gerenciador de pacotes Python moderno e rápido
- `uv sync`: cria ambiente virtual + instala dependências do pyproject.toml
- FastAPI já vem instalado com todas as dependências necessárias


---

### 🚀 Etapa 01: Hello World (20 min) - 09:35-09:55
**Objetivos:**
- Primeira API funcionando
- Entender o básico
- Ver documentação automática

**Roteiro:**
1. Criar arquivo main.py (5 min)
   - Codar junto, linha por linha
   - Explicar cada linha
   ```python
   from fastapi import FastAPI

   app = FastAPI()

   @app.get("/")
   def raiz():
       return {"mensagem": "Olá Python Brasil!"}
   ```

2. Rodar servidor (3 min)
   ```bash
   uv run fastapi dev 01-hello-world/main.py
   ```
   - Explicar cada parte do comando:
     - `uv run`: executa usando o ambiente virtual do projeto
     - `fastapi dev`: comando do FastAPI CLI para desenvolvimento
     - `01-hello-world/main.py`: arquivo da aplicação
     - Modo `dev` já inclui auto-reload automático

3. Testar no navegador (2 min)
   - Abrir http://localhost:8000
   - Mostrar o JSON retornado

4. **MOMENTO WOW:** Documentação automática (10 min)
   - Abrir http://localhost:8000/docs
   - Explorar a interface
   - Testar a rota pelo Swagger
   - Mostrar http://localhost:8000/redoc também
   - Enfatizar: "Não escrevemos NADA de documentação!"

**Checkpoint:** Perguntar se todos conseguiram ver a resposta no navegador

---

### 📊 Etapa 02: Rotas GET (20 min) - 09:55-10:15
**Objetivos:**
- Múltiplas rotas
- Path parameters
- Query parameters

**Roteiro:**
1. Criar lista de livros (3 min)
   - Explicar que é simulação de banco de dados

2. Rota para listar todos (3 min)
   ```python
   @app.get("/livros")
   def listar_livros():
       return livros
   ```

3. Path parameter (7 min)
   ```python
   @app.get("/livros/{livro_id}")
   def obter_livro(livro_id: int):
       ...
   ```
   - Enfatizar a tipagem (`: int`)
   - Testar com ID válido
   - **Mostrar validação:** testar com `/livros/abc`
   - "Olha o erro que o FastAPI dá automaticamente!"

4. Query parameter (7 min)
   ```python
   @app.get("/livros/buscar")
   def buscar(q: str):
       ...
   ```
   - Explicar diferença entre path e query
   - Testar: `/livros/buscar?q=python`

**Exercício rápido (se der tempo):**
- "Criem uma rota que retorna o livro mais recente"

---

### ☕ PAUSA (10 min) - 10:15-10:25
- Ir ao banheiro
- Beber água
- Ajudar quem ficou para trás

**Durante a pausa:** Preparar código da próxima etapa

---

### 📝 Etapa 03: Rotas POST (20 min) - 10:25-10:45
**Objetivos:**
- Receber dados do cliente
- Introduzir Pydantic
- CRUD completo

**Roteiro:**
1. Introduzir Pydantic (5 min)
   ```python
   from pydantic import BaseModel

   class Tarefa(BaseModel):
       titulo: str
       descricao: str
       concluida: bool = False
   ```
   - "Pydantic define a estrutura dos dados"
   - "FastAPI valida automaticamente!"

2. Rota POST (8 min)
   ```python
   @app.post("/tarefas")
   def criar_tarefa(tarefa: Tarefa):
       ...
   ```
   - Criar tarefa pelo /docs
   - Mostrar validação automática

3. PUT e DELETE (7 min)
   - Implementar rapidamente
   - Focar em mostrar funcionando

**Momento importante:**
- "Vejam: não escrevemos nenhum código de validação!"
- "FastAPI + Pydantic fazem tudo por nós"

---

### ✅ Etapa 04: Validação Pydantic (20 min) - 10:45-11:05
**Objetivos:**
- Validações avançadas
- Field()
- Validadores customizados

**Roteiro:**
1. Field() com restrições (8 min)
   ```python
   nome: str = Field(min_length=2, max_length=100)
   idade: int = Field(ge=18, le=120)
   ```
   - Mostrar cada tipo de validação
   - Testar valores inválidos

2. EmailStr (3 min)
   ```python
   from pydantic import EmailStr
   email: EmailStr
   ```
   - Testar email inválido

3. Validador customizado (9 min)
   ```python
   @field_validator('nome')
   @classmethod
   def nome_sem_numeros(cls, valor):
       if any(char.isdigit() for char in valor):
           raise ValueError('Nome não pode ter números')
       return valor
   ```
   - Testar validação

**Enfatizar:**
- "Com Pydantic, seus dados chegam sempre válidos"
- "Menos bugs em produção!"

---

### 🏗️ Etapa 05: Organizando Código (20 min) - 11:05-11:25
**Objetivos:**
- Separar código em arquivos
- APIRouter
- Estrutura profissional

**Roteiro:**
1. Problema de ter tudo em um arquivo (3 min)
   - "Imagina 50 rotas no mesmo arquivo"
   - "Difícil de manter"

2. Criar models.py (5 min)
   - Mover modelos Pydantic

3. Criar routers.py (7 min)
   - Explicar APIRouter
   ```python
   router = APIRouter(prefix="/livros", tags=["livros"])
   ```
   - Criar algumas rotas

4. Incluir no main.py (5 min)
   ```python
   app.include_router(router_livros)
   ```
   - Mostrar que funciona igual
   - Mostrar tags na documentação

**Checkpoint:**
- "Agora vocês sabem estruturar uma API de verdade!"

---

### 🎯 Recapitulação e Próximos Passos (10 min) - 11:25-11:35
**Objetivos:**
- Consolidar aprendizado
- Inspirar a continuar

**Roteiro:**
1. Revisão do que foi visto (5 min)
   - GET, POST, PUT, DELETE ✅
   - Pydantic e validação ✅
   - Documentação automática ✅
   - Organização de código ✅

2. Próximos passos (5 min)
   - Banco de dados (SQLAlchemy)
   - Autenticação (OAuth2, JWT)
   - Testes (pytest)
   - Deploy (Railway, Render)
   - Compartilhar recursos

**Frase de encerramento:**
> "Vocês agora têm a base para criar qualquer API! O resto é praticar e ir adicionando funcionalidades conforme precisarem."

---

### ❓ Perguntas e Respostas (55 min) - 11:35-12:30
- Responder dúvidas
- Ajudar individualmente
- Circular pela sala
- Trocar contatos/redes sociais

---

## 💡 Dicas Gerais de Apresentação

### Durante o Tutorial

**Ritmo:**
- Fale devagar e pausadamente
- Dê tempo para as pessoas digitarem
- Pause depois de conceitos importantes

**Interação:**
- Pergunte constantemente: "Deu certo aí?"
- Incentive perguntas: "Sem pergunta boba!"
- Use nomes dos participantes quando possível

**Problemas Técnicos:**
- Tenha paciência
- Use tempo de instalação para explicar conceitos
- Tenha código de backup pronto

**Energia:**
- Mostre entusiasmo pelo FastAPI
- Comemore quando algo funciona
- "Olha que legal isso!"

### Frases Úteis

**Para ganhar tempo:**
- "Enquanto instala, deixa eu explicar..."
- "Quem já terminou pode ajudar o colega do lado"

**Para verificar entendimento:**
- "Faz sentido até aqui?"
- "Alguém com dúvida nessa parte?"

**Para motivar:**
- "Vocês estão indo muito bem!"
- "Isso que vocês fizeram, muita gente acha difícil"
- "Em poucas linhas, olha o que conseguimos!"

### Gestão de Tempo

**Se estiver atrasado:**
- Pule exemplos extras
- Mostre código pronto ao invés de digitar
- Foque no essencial

**Se estiver adiantado:**
- Exercícios extras
- Perguntas e discussões
- Aprofunde em tópicos de interesse

### Emergências

**Internet cair:**
- Toda documentação deve estar offline
- Exemplos funcionam sem internet
- Use tempo para Q&A

**Projetor parar:**
- Continue no terminal, pessoas podem acompanhar
- Use mais tempo individual

**Sua máquina travar:**
- Tenha backup em outra máquina/USB
- Use máquina de participante (último caso)

---

## 📦 Materiais de Apoio

### Para Compartilhar com Participantes

1. **Link do repositório GitHub**
   - Código completo
   - READMEs de cada etapa

2. **Recursos adicionais:**
   - Documentação FastAPI: https://fastapi.tiangolo.com
   - Tutorial oficial: https://fastapi.tiangolo.com/tutorial/
   - Pydantic docs: https://docs.pydantic.dev

3. **Comunidade:**
   - Discord FastAPI (se houver)
   - Grupo Python Brasil no Telegram
   - Suas redes sociais para contato

### Pós-Tutorial

- Compartilhar slides (se tiver)
- Disponibilizar gravação (se houver)
- Pedir feedback

---

## ✨ Lembrete Final

**Você está bem preparado!**

- O material está completo e testado
- Os participantes querem aprender
- Erros acontecem e tudo bem
- O importante é a jornada de aprendizado

**Respire fundo e divirta-se! 🚀**

Você está compartilhando conhecimento valioso com a comunidade Python brasileira. Isso é incrível!

---

**Boa sorte na Python Brasil 2025!** 🐍🇧🇷
