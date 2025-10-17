# Etapa 03: Rotas POST - Recebendo dados do cliente

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="API de Tarefas",
    description="Uma API para gerenciar suas tarefas diárias",
    version="1.0.0"
)

# ===== MODELOS PYDANTIC =====
# Pydantic é uma biblioteca para validação de dados usando type hints
# Aqui definimos a "estrutura" dos dados que esperamos receber


class Tarefa(BaseModel):
    """Modelo que representa uma tarefa"""
    titulo: str
    descricao: str
    concluida: bool = False  # Valor padrão: False

    # Configuração de exemplo para a documentação
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "titulo": "Estudar FastAPI",
                    "descricao": "Completar o tutorial da Python Brasil",
                    "concluida": False
                }
            ]
        }
    }


# ===== "BANCO DE DADOS" =====
# Em memória - será perdido quando reiniciar o servidor
# Em produção, você usaria um banco de dados real
tarefas = []
proximo_id = 1


# ===== ROTAS =====

@app.get("/")
def raiz():
    """Informações sobre a API"""
    return {
        "mensagem": "API de Tarefas",
        "total_tarefas": len(tarefas),
        "endpoints": {
            "listar": "GET /tarefas",
            "criar": "POST /tarefas",
            "obter": "GET /tarefas/{id}",
        }
    }


@app.get("/tarefas")
def listar_tarefas():
    """Lista todas as tarefas"""
    return {
        "total": len(tarefas),
        "tarefas": tarefas
    }


@app.get("/tarefas/{tarefa_id}")
def obter_tarefa(tarefa_id: int):
    """Obtém uma tarefa específica pelo ID"""
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            return tarefa

    return {"erro": "Tarefa não encontrada"}


@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    """
    Cria uma nova tarefa

    Recebe um JSON com:
    - titulo: string (obrigatório)
    - descricao: string (obrigatório)
    - concluida: boolean (opcional, padrão: false)
    """
    global proximo_id

    # Converte o modelo Pydantic para dicionário
    nova_tarefa = tarefa.model_dump()

    # Adiciona o ID
    nova_tarefa["id"] = proximo_id
    proximo_id += 1

    # Adiciona à lista
    tarefas.append(nova_tarefa)

    return {
        "mensagem": "Tarefa criada com sucesso!",
        "tarefa": nova_tarefa
    }


@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: Tarefa):
    """
    Atualiza uma tarefa existente

    - **tarefa_id**: ID da tarefa a atualizar
    - **tarefa_atualizada**: Novos dados da tarefa
    """
    for i, tarefa in enumerate(tarefas):
        if tarefa["id"] == tarefa_id:
            # Atualiza mantendo o ID original
            tarefas[i] = tarefa_atualizada.model_dump()
            tarefas[i]["id"] = tarefa_id

            return {
                "mensagem": "Tarefa atualizada com sucesso!",
                "tarefa": tarefas[i]
            }

    return {"erro": "Tarefa não encontrada"}


@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
    """Remove uma tarefa pelo ID"""
    for i, tarefa in enumerate(tarefas):
        if tarefa["id"] == tarefa_id:
            tarefa_removida = tarefas.pop(i)
            return {
                "mensagem": "Tarefa removida com sucesso!",
                "tarefa": tarefa_removida
            }

    return {"erro": "Tarefa não encontrada"}


# Para rodar: uvicorn main:app --reload
#
# Para testar as rotas POST/PUT/DELETE, use a documentação interativa:
# http://localhost:8000/docs
#
# Lá você pode testar todas as rotas clicando em "Try it out"!
