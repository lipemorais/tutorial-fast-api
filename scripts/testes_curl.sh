#!/bin/bash

# Scripts de teste com curl para as APIs do tutorial
# Execute este arquivo com: bash scripts/testes_curl.sh

echo "========================================="
echo "Scripts de Teste com curl"
echo "========================================="
echo ""
echo "Certifique-se de que a API está rodando em http://localhost:8000"
echo "Comando: uvicorn main:app --reload"
echo ""

# Cores para output (opcional)
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Função auxiliar para printar seções
print_section() {
    echo ""
    echo -e "${BLUE}===========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}===========================================${NC}"
    echo ""
}

# Função para executar comando e mostrar
run_curl() {
    echo -e "${YELLOW}Executando:${NC} $1"
    echo ""
    eval $1
    echo ""
    echo "---"
}

# ===== ETAPA 01: Hello World =====
print_section "ETAPA 01: Hello World"

run_curl "curl http://localhost:8000/"

# ===== ETAPA 02: Rotas GET =====
print_section "ETAPA 02: Rotas GET"

echo "Listar todos os livros:"
run_curl "curl http://localhost:8000/livros"

echo "Obter livro por ID (1):"
run_curl "curl http://localhost:8000/livros/1"

echo "Buscar livros por título (python):"
run_curl "curl 'http://localhost:8000/livros/buscar/titulo?q=python'"

echo "Filtrar livros por ano (2015-2020):"
run_curl "curl 'http://localhost:8000/livros/filtrar/ano?ano_min=2015&ano_max=2020'"

# ===== ETAPA 03: Rotas POST =====
print_section "ETAPA 03: Rotas POST - Tarefas"

echo "Criar uma tarefa:"
run_curl "curl -X POST http://localhost:8000/tarefas \\
  -H 'Content-Type: application/json' \\
  -d '{
    \"titulo\": \"Estudar FastAPI\",
    \"descricao\": \"Completar o tutorial da Python Brasil\",
    \"concluida\": false
  }'"

echo "Criar outra tarefa:"
run_curl "curl -X POST http://localhost:8000/tarefas \\
  -H 'Content-Type: application/json' \\
  -d '{
    \"titulo\": \"Fazer exercícios\",
    \"descricao\": \"Praticar o que aprendi\",
    \"concluida\": false
  }'"

echo "Listar todas as tarefas:"
run_curl "curl http://localhost:8000/tarefas"

echo "Atualizar tarefa (marcar como concluída):"
run_curl "curl -X PUT http://localhost:8000/tarefas/1 \\
  -H 'Content-Type: application/json' \\
  -d '{
    \"titulo\": \"Estudar FastAPI\",
    \"descricao\": \"Completar o tutorial da Python Brasil\",
    \"concluida\": true
  }'"

echo "Deletar tarefa:"
run_curl "curl -X DELETE http://localhost:8000/tarefas/2"

# ===== ETAPA 04: Validação Pydantic =====
print_section "ETAPA 04: Validação Pydantic"

echo "Criar usuário válido:"
run_curl "curl -X POST http://localhost:8000/usuarios \\
  -H 'Content-Type: application/json' \\
  -d '{
    \"nome\": \"Maria Silva\",
    \"email\": \"maria@example.com\",
    \"idade\": 25,
    \"bio\": \"Desenvolvedora Python\"
  }'"

echo "Criar produto válido:"
run_curl "curl -X POST http://localhost:8000/produtos \\
  -H 'Content-Type: application/json' \\
  -d '{
    \"nome\": \"Notebook Dell\",
    \"descricao\": \"Notebook profissional com 16GB de RAM e SSD 512GB\",
    \"preco\": 3500.00,
    \"estoque\": 10,
    \"categoria\": \"Eletrônicos\"
  }'"

echo "Listar produtos:"
run_curl "curl http://localhost:8000/produtos"

echo -e "${YELLOW}Testando validação - Email inválido (deve dar erro):${NC}"
run_curl "curl -X POST http://localhost:8000/usuarios \\
  -H 'Content-Type: application/json' \\
  -d '{
    \"nome\": \"João\",
    \"email\": \"email-invalido\",
    \"idade\": 30
  }'"

# ===== ETAPA 05: Organizando Código =====
print_section "ETAPA 05: Organizando Código - Biblioteca"

echo "Criar livro:"
run_curl "curl -X POST http://localhost:8000/livros/ \\
  -H 'Content-Type: application/json' \\
  -d '{
    \"titulo\": \"Python Fluente\",
    \"autor\": \"Luciano Ramalho\",
    \"ano\": 2015,
    \"paginas\": 792,
    \"disponivel\": true
  }'"

echo "Criar autor:"
run_curl "curl -X POST http://localhost:8000/autores/ \\
  -H 'Content-Type: application/json' \\
  -d '{
    \"nome\": \"Luciano Ramalho\",
    \"email\": \"luciano@example.com\",
    \"biografia\": \"Programador Python há mais de 20 anos\"
  }'"

echo "Listar livros:"
run_curl "curl http://localhost:8000/livros/"

echo "Listar autores:"
run_curl "curl http://localhost:8000/autores/"

print_section "Testes concluídos!"
echo "Para testar de forma interativa, acesse: http://localhost:8000/docs"
echo ""
