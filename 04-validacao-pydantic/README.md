# Etapa 04: Validação Avançada com Pydantic

Agora vamos explorar o verdadeiro poder do Pydantic! Nesta etapa você vai aprender a criar validações robustas e customizadas para seus dados.

## Objetivo

Aprender a:
- Usar `Field()` para adicionar restrições aos campos
- Validar strings com comprimento mínimo/máximo e padrões
- Validar números com limites
- Criar validadores customizados
- Validar emails
- Usar valores padrão dinâmicos (como data/hora atual)
- Retornar respostas padronizadas com `response_model`

## Conceitos

### Field() - Validações Declarativas

O `Field()` permite adicionar metadados e validações aos campos:

```python
from pydantic import Field

nome: str = Field(
    ...,              # Obrigatório
    min_length=2,     # Mínimo 2 caracteres
    max_length=100,   # Máximo 100 caracteres
    description="Nome do usuário"
)
```

### Validações Numéricas

```python
idade: int = Field(
    ge=18,  # Greater or Equal - maior ou igual a 18
    le=120  # Less or Equal - menor ou igual a 120
)

preco: float = Field(
    gt=0,   # Greater Than - maior que 0 (não pode ser 0)
)
```

### Validadores Customizados

Quando as validações padrão não são suficientes:

```python
@field_validator('nome')
@classmethod
def nome_nao_pode_ter_numeros(cls, valor: str) -> str:
    if any(char.isdigit() for char in valor):
        raise ValueError('O nome não pode conter números')
    return valor
```

## Estrutura do Código

### models.py - Modelos com Validações

Organizamos os modelos em um arquivo separado:

**Usuario:**
- Nome: 2-100 caracteres, sem números
- Email: validação automática de email válido
- Idade: 18-120 anos
- Site: deve começar com http:// ou https://
- Bio: máximo 500 caracteres, sem palavras proibidas

**Produto:**
- Nome: 3-100 caracteres, com pelo menos um caractere alfanumérico
- Descrição: 10-1000 caracteres
- Preço: maior que 0, máximo 1 milhão
- Estoque: não pode ser negativo
- Data de criação: gerada automaticamente

### main.py - Rotas usando os modelos

As rotas importam e usam os modelos validados.

## Como executar

### 1. Execute o servidor (a partir da raiz do projeto)

```bash
uv run fastapi dev 04-validacao-pydantic/main.py
```

### 2. Acesse a documentação

http://localhost:8000/docs

## Testando as Validações

A melhor forma de aprender é testando! Use a documentação interativa em `/docs` para experimentar.

### Exemplos de Dados Válidos

**Usuário válido:**
```json
{
  "nome": "Maria Silva",
  "email": "maria@example.com",
  "idade": 25,
  "site": "https://maria.dev",
  "bio": "Desenvolvedora Python"
}
```

**Produto válido:**
```json
{
  "nome": "Notebook Dell",
  "descricao": "Notebook profissional com 16GB de RAM",
  "preco": 3500.00,
  "estoque": 10,
  "categoria": "Eletrônicos"
}
```

### Exemplos de Dados Inválidos

Experimente cada um destes e observe as mensagens de erro:

**1. Nome com números:**
```json
{
  "nome": "João123",
  "email": "joao@example.com",
  "idade": 25
}
```
❌ Erro: "O nome não pode conter números"

**2. Idade abaixo do mínimo:**
```json
{
  "nome": "Ana Silva",
  "email": "ana@example.com",
  "idade": 17
}
```
❌ Erro: idade deve ser >= 18

**3. Email inválido:**
```json
{
  "nome": "Pedro Costa",
  "email": "pedro.email.invalido",
  "idade": 30
}
```
❌ Erro: value is not a valid email address

**4. Site sem protocolo:**
```json
{
  "nome": "Maria",
  "email": "maria@example.com",
  "idade": 28,
  "site": "maria.com"
}
```
❌ Erro: site deve começar com http:// ou https://

**5. Bio com palavra proibida:**
```json
{
  "nome": "José Santos",
  "email": "jose@example.com",
  "idade": 35,
  "bio": "Confira meu spam de produtos"
}
```
❌ Erro: A bio não pode conter a palavra "spam"

**6. Preço negativo:**
```json
{
  "nome": "Produto Teste",
  "descricao": "Descrição do produto aqui",
  "preco": -10.00,
  "categoria": "Teste"
}
```
❌ Erro: preco deve ser > 0

**7. Descrição muito curta:**
```json
{
  "nome": "Produto",
  "descricao": "Curto",
  "preco": 100.00,
  "categoria": "Teste"
}
```
❌ Erro: descrição deve ter pelo menos 10 caracteres

## Recursos Avançados Demonstrados

### 1. EmailStr

```python
from pydantic import EmailStr

email: EmailStr  # Valida automaticamente se é email válido
```

### 2. Pattern (Regex)

```python
site: Optional[str] = Field(
    pattern=r"^https?://"  # Deve começar com http:// ou https://
)
```

### 3. Valores Padrão Dinâmicos

```python
from datetime import datetime

data_criacao: datetime = Field(
    default_factory=datetime.now  # Chama a função no momento da criação
)
```

### 4. Response Model

```python
@app.post("/usuarios", response_model=RespostaPadrao)
def criar_usuario(usuario: Usuario):
    return RespostaPadrao(
        sucesso=True,
        mensagem="Criado!",
        dados=usuario.model_dump()
    )
```

Garante que a resposta sempre siga o formato definido.

### 5. HTTPException

```python
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="Recurso não encontrado"
)
```

Retorna erro HTTP com mensagem customizada.

## Testando com curl

```bash
# Criar usuário válido
curl -X POST http://localhost:8000/usuarios \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Maria Silva",
    "email": "maria@example.com",
    "idade": 25
  }'

# Criar usuário inválido (idade < 18)
curl -X POST http://localhost:8000/usuarios \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Ana",
    "email": "ana@example.com",
    "idade": 16
  }'

# Criar produto válido
curl -X POST http://localhost:8000/produtos \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Notebook",
    "descricao": "Notebook para desenvolvimento",
    "preco": 3500.00,
    "categoria": "Eletrônicos"
  }'
```

## Experimente

1. **Adicione um validador** que garante que o nome do produto não contém apenas espaços
2. **Crie um campo `desconto`** que só aceita valores entre 0 e 100 (porcentagem)
3. **Adicione validação** para garantir que o email do usuário não é de um domínio específico (ex: não aceitar emails @example.com)
4. **Crie um modelo `Pedido`** que valida que o total é maior que 0 e que a lista de itens não está vazia

## Diferenças da Etapa Anterior

- ✅ Modelos em arquivo separado (organização)
- ✅ Validações com Field() (min, max, pattern, etc)
- ✅ Validadores customizados com @field_validator
- ✅ Validação de email com EmailStr
- ✅ Valores padrão dinâmicos (datetime.now)
- ✅ Response models para padronizar respostas
- ✅ HTTPException para erros customizados

## Próxima Etapa

Na próxima e última etapa, vamos organizar melhor o código separando rotas em arquivos diferentes!

➡️ [Etapa 05: Organizando o Código](../05-organizando-codigo/)

## Referências

- [Pydantic - Field](https://docs.pydantic.dev/latest/concepts/fields/)
- [Pydantic - Validators](https://docs.pydantic.dev/latest/concepts/validators/)
- [FastAPI - Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)
- [FastAPI - Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
