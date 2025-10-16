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

### 1. Entre na pasta

```bash
cd 03-rotas-post
```

### 2. Execute o servidor

```bash
fastapi dev main.py
```

### 3. Testando rotas POST

**Opção 1: Documentação Interativa (MAIS FÁCIL)**

1. Acesse http://localhost:8000/docs
2. Clique na rota `POST /tarefas`
3. Clique em "Try it out"
4. Edite o JSON de exemplo:
```json
{
  "titulo": "Aprender FastAPI",
  "descricao": "Completar todas as etapas do tutorial",
  "concluida": false
}
```
5. Clique em "Execute"

**Opção 2: curl (Linha de comando)**

```bash
# Criar tarefa
curl -X POST http://localhost:8000/tarefas \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Estudar Python",
    "descricao": "Revisar decoradores",
    "concluida": false
  }'

# Listar tarefas
curl http://localhost:8000/tarefas

# Obter tarefa específica
curl http://localhost:8000/tarefas/1

# Atualizar tarefa
curl -X PUT http://localhost:8000/tarefas/1 \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Estudar Python",
    "descricao": "Revisar decoradores e geradores",
    "concluida": true
  }'

# Deletar tarefa
curl -X DELETE http://localhost:8000/tarefas/1
```

**Opção 3: httpie (Mais amigável que curl)**

```bash
# Criar tarefa
http POST localhost:8000/tarefas \
  titulo="Estudar FastAPI" \
  descricao="Tutorial Python Brasil" \
  concluida:=false

# Listar
http GET localhost:8000/tarefas

# Atualizar
http PUT localhost:8000/tarefas/1 \
  titulo="Estudar FastAPI" \
  descricao="Tutorial completo" \
  concluida:=true

# Deletar
http DELETE localhost:8000/tarefas/1
```

## Testando a Validação

O poder do Pydantic está na validação automática! Experimente:

### 1. Enviar dados inválidos

```bash
curl -X POST http://localhost:8000/tarefas \
  -H "Content-Type: application/json" \
  -d '{"titulo": 123, "descricao": "teste"}'
```

Você receberá um erro claro dizendo que `titulo` deve ser string!

### 2. Omitir campo obrigatório

```bash
curl -X POST http://localhost:8000/tarefas \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Só título"}'
```

Erro: `descricao` é obrigatório!

### 3. Tipo errado em booleano

```bash
curl -X POST http://localhost:8000/tarefas \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Teste",
    "descricao": "Descrição",
    "concluida": "sim"
  }'
```

Erro: `concluida` deve ser booleano (true/false)!

## Fluxo Completo de Teste

```bash
# 1. Criar algumas tarefas
curl -X POST http://localhost:8000/tarefas \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Tarefa 1","descricao":"Primeira tarefa"}'

curl -X POST http://localhost:8000/tarefas \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Tarefa 2","descricao":"Segunda tarefa"}'

# 2. Listar todas
curl http://localhost:8000/tarefas

# 3. Marcar primeira como concluída
curl -X PUT http://localhost:8000/tarefas/1 \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Tarefa 1","descricao":"Primeira tarefa","concluida":true}'

# 4. Deletar segunda
curl -X DELETE http://localhost:8000/tarefas/2

# 5. Verificar resultado
curl http://localhost:8000/tarefas
```

## Experimente

1. **Adicione um campo `prioridade`** (baixa, média, alta) ao modelo Tarefa
2. **Crie uma rota** `PATCH /tarefas/{id}/concluir` que marca uma tarefa como concluída sem precisar enviar todos os campos
3. **Adicione validação**: o título deve ter pelo menos 3 caracteres
4. **Adicione um campo opcional** `data_criacao` que é preenchido automaticamente

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
