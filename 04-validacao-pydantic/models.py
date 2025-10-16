# Modelos Pydantic com Validações Avançadas

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr, field_validator


class Usuario(BaseModel):
    """Modelo de usuário com validações avançadas"""

    # Field() permite adicionar validações e metadados
    nome: str = Field(
        ...,  # ... significa obrigatório
        min_length=2,
        max_length=100,
        description="Nome completo do usuário",
        examples=["Maria Silva"]
    )

    email: EmailStr = Field(
        ...,
        description="Email válido do usuário"
    )

    idade: int = Field(
        ...,
        ge=18,  # greater or equal - maior ou igual
        le=120,  # less or equal - menor ou igual
        description="Idade do usuário (18-120)"
    )

    site: Optional[str] = Field(
        None,
        pattern=r"^https?://",  # Deve começar com http:// ou https://
        description="Website do usuário (opcional)"
    )

    bio: Optional[str] = Field(
        None,
        max_length=500,
        description="Biografia curta (máximo 500 caracteres)"
    )

    # Validador customizado
    @field_validator('nome')
    @classmethod
    def nome_nao_pode_ter_numeros(cls, valor: str) -> str:
        """Valida que o nome não contém números"""
        if any(char.isdigit() for char in valor):
            raise ValueError('O nome não pode conter números')
        return valor.strip()  # Remove espaços extras

    @field_validator('bio')
    @classmethod
    def bio_nao_pode_ter_palavras_proibidas(cls, valor: Optional[str]) -> Optional[str]:
        """Valida que a bio não contém palavras proibidas"""
        if valor is None:
            return valor

        palavras_proibidas = ['spam', 'anúncio']
        valor_lower = valor.lower()

        for palavra in palavras_proibidas:
            if palavra in valor_lower:
                raise ValueError(f'A bio não pode conter a palavra "{palavra}"')

        return valor

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nome": "Maria Silva",
                    "email": "maria@example.com",
                    "idade": 25,
                    "site": "https://maria.dev",
                    "bio": "Desenvolvedora Python apaixonada por FastAPI"
                }
            ]
        }
    }


class Produto(BaseModel):
    """Modelo de produto com validações de preço e estoque"""

    nome: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Nome do produto"
    )

    descricao: str = Field(
        ...,
        min_length=10,
        max_length=1000,
        description="Descrição detalhada do produto"
    )

    preco: float = Field(
        ...,
        gt=0,  # greater than - maior que (não pode ser 0)
        description="Preço do produto em reais"
    )

    estoque: int = Field(
        default=0,
        ge=0,  # Não pode ser negativo
        description="Quantidade em estoque"
    )

    categoria: str = Field(
        ...,
        description="Categoria do produto",
        examples=["Eletrônicos", "Livros", "Roupas"]
    )

    ativo: bool = Field(
        default=True,
        description="Se o produto está ativo para venda"
    )

    data_criacao: datetime = Field(
        default_factory=datetime.now,  # Valor padrão é a data/hora atual
        description="Data de criação do produto"
    )

    # Validador que usa múltiplos campos
    @field_validator('preco')
    @classmethod
    def preco_maximo_razoavel(cls, valor: float) -> float:
        """Valida que o preço não é absurdamente alto"""
        if valor > 1_000_000:
            raise ValueError('Preço muito alto! Verifique o valor.')
        return valor

    @field_validator('nome')
    @classmethod
    def nome_sem_caracteres_especiais(cls, valor: str) -> str:
        """Valida que o nome não tem apenas caracteres especiais"""
        if not any(char.isalnum() for char in valor):
            raise ValueError('O nome deve conter pelo menos uma letra ou número')
        return valor.strip()

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nome": "Notebook Dell Inspiron",
                    "descricao": "Notebook para uso profissional com 16GB RAM e SSD 512GB",
                    "preco": 3500.00,
                    "estoque": 10,
                    "categoria": "Eletrônicos",
                    "ativo": True
                }
            ]
        }
    }


class RespostaPadrao(BaseModel):
    """Modelo padrão de resposta da API"""
    sucesso: bool
    mensagem: str
    dados: Optional[dict] = None
