# Modelos da aplicação

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr, field_validator


class Livro(BaseModel):
    """Modelo de livro"""
    titulo: str = Field(..., min_length=1, max_length=200)
    autor: str = Field(..., min_length=1, max_length=100)
    ano: int = Field(..., ge=1000, le=datetime.now().year)
    isbn: Optional[str] = Field(None, min_length=10, max_length=13)
    paginas: int = Field(..., gt=0)
    disponivel: bool = Field(default=True)

    @field_validator('isbn')
    @classmethod
    def isbn_apenas_numeros(cls, valor: Optional[str]) -> Optional[str]:
        if valor is None:
            return valor
        if not valor.replace("-", "").isdigit():
            raise ValueError('ISBN deve conter apenas números e hífens')
        return valor

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "titulo": "Python Fluente",
                    "autor": "Luciano Ramalho",
                    "ano": 2015,
                    "isbn": "978-1491946008",
                    "paginas": 792,
                    "disponivel": True
                }
            ]
        }
    }


class Autor(BaseModel):
    """Modelo de autor"""
    nome: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    biografia: Optional[str] = Field(None, max_length=1000)
    ativo: bool = Field(default=True)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nome": "Luciano Ramalho",
                    "email": "luciano@example.com",
                    "biografia": "Programador Python há mais de 20 anos",
                    "ativo": True
                }
            ]
        }
    }


class RespostaPadrao(BaseModel):
    """Resposta padrão da API"""
    sucesso: bool
    mensagem: str
    dados: Optional[dict | list] = None
