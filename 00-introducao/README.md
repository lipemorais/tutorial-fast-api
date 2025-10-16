# Etapa 00: Introdução aos Frameworks Web e FastAPI

Antes de começarmos a codar, vamos entender o contexto: o que são frameworks web e como o FastAPI surgiu.

## O que é um Framework Web?

Um **framework web** é uma ferramenta que facilita a criação de aplicações web e APIs. Pense nele como um conjunto de componentes prontos que você pode usar para não ter que "reinventar a roda" toda vez que criar um projeto.

### Sem framework você precisaria:
- Gerenciar conexões HTTP manualmente
- Criar seu próprio sistema de rotas
- Implementar validação de dados do zero
- Configurar serialização JSON
- Lidar com CORS, autenticação, etc.

### Com um framework você ganha:
- ✅ Sistema de rotas já pronto
- ✅ Validação automática de dados
- ✅ Conversão automática entre JSON e Python
- ✅ Ferramentas de teste
- ✅ Documentação automática (no caso do FastAPI)
- ✅ Ecossistema de extensões

## A História dos Frameworks Web em Python

### 2005: Django - O Framework "Baterias Incluídas"
Django foi um dos primeiros grandes frameworks Python, criado para desenvolvimento web completo (front + back). Traz ORM, admin, templates - tudo integrado. Ótimo para sites completos, mas pesado para APIs simples.

### 2010: Flask - O Framework Minimalista
Flask trouxe simplicidade: um microframework que te dá o básico e deixa você escolher o resto. Perfeito para APIs pequenas e projetos onde você quer controle total.

### 2011: Tornado - Focado em Performance
Tornado foi pioneiro em operações assíncronas no Python, focado em alta performance e conexões em tempo real (WebSockets).

### 2018: FastAPI - O Moderno e Rápido 🚀

É aqui que nossa história começa!

## A História do FastAPI

### O Criador: Sebastián Ramírez

Em 2018, **Sebastián Ramírez** (também conhecido como [@tiangolo](https://github.com/tiangolo) no GitHub), um desenvolvedor colombiano, tinha um problema: ele precisava criar APIs rapidamente, com validação robusta de dados, e que fossem muito rápidas.

Os frameworks existentes não atendiam todos os requisitos:
- Django era completo demais e lento para APIs puras
- Flask era simples mas não tinha validação automática
- Nenhum aproveitava bem a nova sintaxe `async/await` do Python

### O Nascimento do FastAPI

Sebastián combinou o melhor dos dois mundos:
1. **Starlette** - Framework assíncrono rápido e leve (camada base)
2. **Pydantic** - Validação de dados usando type hints do Python

E adicionou:
- ✨ Documentação automática (Swagger/OpenAPI)
- ✨ Validação baseada em tipos Python modernos
- ✨ Performance comparável a Node.js e Go
- ✨ Editor support (autocomplete, type checking)
- ✨ Facilidade de uso do Flask, com poder do Django

### Primeira Release: 5 de dezembro de 2018
A versão 0.1.0 foi lançada e rapidamente ganhou atenção da comunidade.

## Por que FastAPI Explodiu em Popularidade?

### 1. **Chegou no Momento Certo**
Python 3.6+ tinha introduzido type hints, e Python 3.7+ melhorou muito o `async/await`. FastAPI aproveitou essas features modernas.

### 2. **Desenvolvedor Productivity**
```python
# Com FastAPI, isso valida automaticamente:
@app.post("/users/")
def create_user(name: str, age: int):
    return {"name": name, "age": age}

# Sem framework, seria preciso ~20 linhas para fazer o mesmo!
```

### 3. **Performance Real**
FastAPI é um dos frameworks Python mais rápidos, competindo com Node.js e Go em benchmarks.

### 4. **Documentação Excelente**
A documentação do FastAPI é referência no mundo Python - clara, com exemplos, e sempre atualizada.

### 5. **Comunidade Ativa**
Hoje o FastAPI tem:
- +70.000 ⭐ no GitHub
- É usado por empresas como Microsoft, Uber, Netflix
- Milhões de downloads mensais no PyPI

## Comparação Rápida

| Framework | Ano | Foco | Async | Validação Auto | Docs Auto |
|-----------|-----|------|-------|----------------|-----------|
| Django    | 2005 | Full Stack | Parcial | Via Forms | ❌ |
| Flask     | 2010 | Minimalista | Via Extensão | ❌ | ❌ |
| FastAPI   | 2018 | APIs Modernas | ✅ | ✅ | ✅ |

## Por que Usar FastAPI em 2025?

1. **Padrão da Indústria** - Virou o padrão para novas APIs em Python
2. **Moderna** - Usa as melhores práticas e features do Python moderno
3. **Rápida** - Performance de produção real
4. **Fácil de Aprender** - Sintaxe intuitiva
5. **Type Safety** - Menos bugs graças aos type hints
6. **Documentação Automática** - Economiza horas de trabalho

## O que Você Vai Construir Neste Tutorial

Neste tutorial, você vai aprender FastAPI do zero:
- ✅ Criar endpoints (GET, POST)
- ✅ Validar dados com Pydantic
- ✅ Usar a documentação automática
- ✅ Organizar código como um projeto profissional

Ao final, você terá as bases para criar qualquer API em Python!

## Curiosidades

- 🌟 FastAPI foi um projeto solo que virou fenômeno global
- 📚 A documentação tem exemplos em vários idiomas
- 🏢 Microsoft usa FastAPI internamente e contribui para o projeto
- 🚀 Em 2023, Sebastián criou a Tiangolo (empresa) para manter o projeto
- 🎓 FastAPI é ensinado em universidades e bootcamps ao redor do mundo

---

**Pronto para começar?** Agora que você entende o contexto, vamos colocar a mão no código!

➡️ [Etapa 01: Hello World](../01-hello-world/)

## Referências

- [FastAPI GitHub](https://github.com/tiangolo/fastapi)
- [História Completa](https://fastapi.tiangolo.com/history-design-future/)
- [Benchmarks de Performance](https://www.techempower.com/benchmarks/)
- [Entrevista com Sebastián Ramírez](https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-wrongs)