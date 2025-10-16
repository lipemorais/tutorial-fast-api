# Etapa 03: Rotas POST

Agora vamos além de apenas ler dados! Nesta etapa você vai aprender a receber e processar dados enviados pelo cliente.

## Objetivo

Aprender a:
- Criar rotas POST para receber dados
- Usar Pydantic para validar dados automaticamente
- Implementar operações CRUD (Create, Read, Update, Delete)
- Trabalhar com request body (corpo da requisição)

## Conceitos

### Métodos HTTP

Cada método tem um propósito:

- **GET** - Ler/buscar dados (não modifica nada)
- **POST** - Criar novos recursos
- **PUT** - Atualizar recurso completo
- **PATCH** - Atualizar parte de um recurso
- **DELETE** - Remover um recurso

### O que é Pydantic?

Pydantic é uma biblioteca Python que usa type hints para:
- Validar dados automaticamente
- Converter tipos quando possível
- Gerar documentação automática
- Fornecer mensagens de erro claras

## O Código

### 1. Definindo o Modelo com Pydantic

```python
from pydantic import BaseModel

class Tarefa(BaseModel):
    titulo: str              # Obrigatório
    descricao: str           # Obrigatório
    concluida: bool = False  # Opcional, padrão False
```

Este modelo define a estrutura que esperamos receber. O FastAPI vai:
- Validar que `titulo` e `descricao` são strings
- Validar que `concluida` é booleano
- Usar `False` se `concluida` não for enviado
- Rejeitar requisições que não seguem essa estrutura

### 2. Rota POST - Criar Tarefa

```python
@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    # tarefa já vem validado!
    nova_tarefa = tarefa.model_dump()  # Converte para dict
    # ... processa ...
    return {"mensagem": "Criado!", "tarefa": nova_tarefa}
```

**Observe:**
- `tarefa: Tarefa` - FastAPI automaticamente valida o JSON recebido
- Se os dados forem inválidos, FastAPI retorna erro 422 automaticamente
- `model_dump()` converte o modelo Pydantic para dicionário Python

### 3. Rota PUT - Atualizar Tarefa

```python
@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: Tarefa):
    # Combina path parameter (tarefa_id) com body (tarefa_atualizada)
    ...
```

### 4. Rota DELETE - Remover Tarefa

```python
@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
    # Remove a tarefa da lista
    ...
```

## Como executar

### 1. Execute o servidor (a partir da raiz do projeto)

```bash
uv run fastapi dev 03-rotas-post/main.py
```

### 2. Testando as rotas usando a documentação interativa

Acesse: http://localhost:8000/docs

Agora você verá rotas de **todos os métodos HTTP**: GET, POST, PUT e DELETE!

#### 1. POST /tarefas - Criar uma tarefa

1. Clique na rota `POST /tarefas` (ela tem cor diferente, geralmente verde)
2. Clique em **"Try it out"**
3. Você verá um JSON de exemplo. Edite-o:
   ```json
   {
     "titulo": "Aprender FastAPI",
     "descricao": "Completar todas as etapas do tutorial",
     "concluida": false
   }
   ```
4. Clique em **"Execute"**
5. Veja a resposta com status `201 Created` e a tarefa criada com ID!

**Crie mais tarefas:**
- "Estudar Pydantic" - "Aprender validação de dados"
- "Fazer exercícios" - "Praticar o que aprendi"

#### 2. GET /tarefas - Listar todas as tarefas

**No navegador:** http://localhost:8000/tarefas

**Ou no `/docs`:**
1. Expanda `GET /tarefas`
2. **"Try it out"** → **"Execute"**
3. Veja todas as tarefas que você criou!

#### 3. GET /tarefas/{tarefa_id} - Obter tarefa específica

**No navegador:** http://localhost:8000/tarefas/1

**Ou no `/docs`:**
1. Expanda `GET /tarefas/{tarefa_id}`
2. **"Try it out"**
3. Digite o ID: **1**
4. **"Execute"**
5. Veja apenas a tarefa com ID 1

#### 4. PUT /tarefas/{tarefa_id} - Atualizar uma tarefa

1. Expanda `PUT /tarefas/{tarefa_id}` (geralmente cor laranja)
2. **"Try it out"**
3. Digite o ID da tarefa que quer atualizar: **1**
4. Edite o JSON, marcando como concluída:
   ```json
   {
     "titulo": "Aprender FastAPI",
     "descricao": "Completar todas as etapas do tutorial",
     "concluida": true
   }
   ```
5. **"Execute"**
6. Veja a tarefa atualizada!
7. Liste todas novamente para confirmar a mudança

#### 5. DELETE /tarefas/{tarefa_id} - Deletar uma tarefa

1. Expanda `DELETE /tarefas/{tarefa_id}` (geralmente cor vermelha)
2. **"Try it out"**
3. Digite o ID: **1**
4. **"Execute"**
5. Veja a mensagem de sucesso
6. Liste todas novamente - a tarefa sumiu!

### 3. Testando a Validação do Pydantic

O poder do Pydantic está na validação automática! Vamos testar no `/docs`:

#### Teste 1: Tipo inválido no título

1. Vá em `POST /tarefas`
2. **"Try it out"**
3. Tente enviar:
   ```json
   {
     "titulo": 123,
     "descricao": "teste"
   }
   ```
4. **"Execute"**
5. Erro `422`! O FastAPI diz que `titulo` deve ser string!

#### Teste 2: Campo obrigatório faltando

1. Tente enviar:
   ```json
   {
     "titulo": "Só título"
   }
   ```
2. **"Execute"**
3. Erro! `descricao` é obrigatório!

#### Teste 3: Tipo errado no booleano

1. Tente enviar:
   ```json
   {
     "titulo": "Teste",
     "descricao": "Descrição",
     "concluida": "sim"
   }
   ```
2. **"Execute"**
3. Erro! `concluida` deve ser `true` ou `false`, não uma string!

**Observe:** A validação acontece ANTES da sua função ser chamada. O Pydantic protege seu código! 🛡️

### 4. Fluxo Completo de Teste (Pratique!)

Faça esse exercício completo usando apenas o `/docs`:

1. **Crie 3 tarefas:**
   - "Estudar Python" - "Revisar decoradores"
   - "Ler documentação" - "FastAPI docs"
   - "Fazer projeto" - "API de lista de tarefas"

2. **Liste todas** - Confirme que as 3 foram criadas

3. **Marque a primeira como concluída:**
   - Use `PUT /tarefas/1`
   - Mude `concluida` para `true`

4. **Obtenha apenas a tarefa 2:**
   - Use `GET /tarefas/2`

5. **Delete a tarefa 3:**
   - Use `DELETE /tarefas/3`

6. **Liste todas novamente** - Devem sobrar apenas as tarefas 1 e 2

**Observe:** Toda essa interação aconteceu apenas clicando em botões no navegador! 🎉

## Experimente (e teste no /docs!)

1. **Adicione um campo `prioridade`** ao modelo Tarefa:
   ```python
   class Tarefa(BaseModel):
       titulo: str
       descricao: str
       concluida: bool = False
       prioridade: str = "média"  # Nova!
   ```
   - Crie uma tarefa com prioridade "alta"
   - Veja o campo aparecer na documentação

2. **Crie uma rota especial** `PATCH /tarefas/{id}/concluir`:
   ```python
   @app.patch("/tarefas/{tarefa_id}/concluir")
   def marcar_concluida(tarefa_id: int):
       # Apenas marca como concluída, sem precisar enviar tudo
       ...
   ```
   - Teste no `/docs` - veja como é mais simples!

3. **Adicione validação**: título mínimo de 3 caracteres:
   ```python
   from pydantic import Field

   titulo: str = Field(min_length=3)
   ```
   - Tente criar tarefa com título "ab"
   - Veja o erro de validação no `/docs`

4. **Campo com valor padrão dinâmico**:
   ```python
   from datetime import datetime

   data_criacao: datetime = Field(default_factory=datetime.now)
   ```
   - Crie tarefas e veja a data/hora sendo preenchida automaticamente

## Diferenças da Etapa Anterior

- ✅ Rotas POST/PUT/DELETE além de GET
- ✅ Recebendo dados do cliente (request body)
- ✅ Validação automática com Pydantic
- ✅ Operações CRUD completas
- ✅ Mensagens de erro automáticas e claras

## Próxima Etapa

Na próxima etapa vamos explorar validações mais avançadas do Pydantic!

➡️ [Etapa 04: Validação Pydantic](../04-validacao-pydantic/)

## Referências

- [FastAPI - Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [Pydantic - Models](https://docs.pydantic.dev/latest/concepts/models/)
- [HTTP Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
