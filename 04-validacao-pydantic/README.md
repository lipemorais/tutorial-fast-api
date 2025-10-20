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
- Nome: 3-100 caracteres, com pelo menos um caracter alfanumérico
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

### 2. Teste usando a documentação interativa

Acesse: http://localhost:8000/docs

Agora você verá rotas para **Usuários** e **Produtos**. Vamos testar as validações avançadas!

💡 **Dica:** As rotas GET também podem ser testadas no navegador:
- http://localhost:8000/usuarios - Lista usuários
- http://localhost:8000/produtos - Lista produtos

## Testando as Validações

#### 1. Criar um usuário válido

1. Expanda `POST /usuarios`
2. **"Try it out"**
3. Use este exemplo:
   ```json
   {
     "nome": "Maria Silva",
     "email": "maria@example.com",
     "idade": 25,
     "site": "https://maria.dev",
     "bio": "Desenvolvedora Python"
   }
   ```
4. **"Execute"**
5. Criado! ✅ Status 201

#### 2. Criar um produto válido

1. Expanda `POST /produtos`
2. **"Try it out"**
3. Use este exemplo:
   ```json
   {
     "nome": "Notebook Dell",
     "descricao": "Notebook profissional com 16GB de RAM e SSD de 512GB",
     "preco": 3500.00,
     "estoque": 10,
     "categoria": "Eletrônicos"
   }
   ```
4. **"Execute"**
5. Criado! ✅ Veja a `data_criacao` preenchida automaticamente

### 3. Testando Validações Inválidas

Agora vamos testar dados inválidos e ver as validações em ação!

#### Teste 1: Nome com números (Validador customizado)
1. `POST /usuarios` → **"Try it out"**
2. Envie:
   ```json
   {
     "nome": "João123",
     "email": "joao@example.com",
     "idade": 25
   }
   ```
3. ❌ Erro: "O nome não pode conter números"

#### Teste 2: Idade abaixo do mínimo (Field com ge=18)
1. Envie:
   ```json
   {
     "nome": "Ana Silva",
     "email": "ana@example.com",
     "idade": 17
   }
   ```
2. ❌ Erro: idade deve ser >= 18

#### Teste 3: Email inválido (EmailStr)
1. Envie:
   ```json
   {
     "nome": "Pedro Costa",
     "email": "pedro.email.invalido",
     "idade": 30
   }
   ```
2. ❌ Erro: value is not a valid email address

#### Teste 4: Site sem protocolo (Pattern/Regex)
1. Envie:
   ```json
   {
     "nome": "Maria",
     "email": "maria@example.com",
     "idade": 28,
     "site": "maria.com"
   }
   ```
2. ❌ Erro: site deve começar com http:// ou https://

#### Teste 5: Bio com palavra proibida (Validador customizado)
1. Envie:
   ```json
   {
     "nome": "José Santos",
     "email": "jose@example.com",
     "idade": 35,
     "bio": "Confira meu spam de produtos"
   }
   ```
2. ❌ Erro: A bio não pode conter a palavra "spam"

#### Teste 6: Preço negativo (Field com gt=0)
1. `POST /produtos` → **"Try it out"**
2. Envie:
   ```json
   {
     "nome": "Produto Teste",
     "descricao": "Descrição completa do produto aqui",
     "preco": -10.00,
     "categoria": "Teste"
   }
   ```
3. ❌ Erro: preco deve ser > 0

#### Teste 7: Descrição muito curta (Field com min_length=10)
1. Envie:
   ```json
   {
     "nome": "Produto",
     "descricao": "Curto",
     "preco": 100.00,
     "categoria": "Teste"
   }
   ```
2. ❌ Erro: descrição deve ter pelo menos 10 caracteres

**Observe:** Todas as validações são mostradas claramente na resposta! O Pydantic fornece mensagens de erro detalhadas. 🛡️

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

### 4. Explorando a Documentação

Olhe atentamente no `/docs` e observe:

1. **Schemas na parte inferior:**
   - Role até o final da página
   - Veja os modelos `Usuario` e `Produto` detalhados
   - Veja todos os campos, tipos e restrições!

2. **Validações visíveis:**
   - Campos obrigatórios marcados com `*`
   - Tipos de dados mostrados (string, integer, number)
   - Valores mínimos/máximos documentados
   - Patterns (regex) mostrados

3. **Response Model:**
   - Todas as respostas seguem o modelo `RespostaPadrao`
   - Sempre tem: `sucesso`, `mensagem`, `dados`
   - Isso garante consistência na API!

## Experimente (e teste no /docs!)

1. **Validador para nome sem apenas espaços:**
   ```python
   @field_validator('nome')
   @classmethod
   def nome_nao_vazio(cls, valor: str) -> str:
       if not valor.strip():
           raise ValueError('O nome não pode ser vazio')
       return valor
   ```
   - Teste no `/docs` enviando "   " (apenas espaços)

2. **Campo desconto com validação:**
   ```python
   desconto: float = Field(ge=0, le=100, description="Desconto em porcentagem")
   ```
   - Teste com 50 (ok), 101 (erro), -5 (erro)

3. **Validar domínio de email:**
   ```python
   @field_validator('email')
   @classmethod
   def validar_dominio(cls, valor: str) -> str:
       if valor.endswith('@example.com'):
           raise ValueError('Domínio example.com não permitido')
       return valor
   ```
   - Teste com "teste@example.com" - deve dar erro!

4. **Modelo Pedido complexo:**
   ```python
   class Pedido(BaseModel):
       itens: list[str] = Field(min_length=1)
       total: float = Field(gt=0)
   ```
   - Crie a rota `POST /pedidos`
   - Veja aparecer no `/docs` automaticamente
   - Teste com lista vazia (erro)
   - Teste com total 0 (erro)

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
