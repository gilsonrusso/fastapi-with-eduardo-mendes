
# 🚀 FastAPI Zero

Um projeto de exemplo utilizando [FastAPI](https://fastapi.tiangolo.com/), estruturado com boas práticas de desenvolvimento, autenticação JWT, ambiente configurado com `poetry`, testes automatizados com `pytest` e análise de código com `ruff`.

---

## 📦 Requisitos

- Python `>=3.13,<4.0`
- [Poetry](https://python-poetry.org/docs/#installation)

---

## ⚙️ Instalação

```bash
git clone https://github.com/seu-usuario/fastapi-zero.git
cd fastapi-zero

poetry install
```

> Certifique-se de ativar o ambiente virtual do poetry:
```bash
poetry shell
```

---

## ▶️ Executar o projeto

```bash
poetry run fastapi dev fastapi_zero/app.py
```

O servidor será iniciado em:  
🔗 http://localhost:8000

---

## 🧪 Testes

Executar testes unitários com cobertura:

```bash
poetry run pytest --cov=fastapi_zero -vv
```

Gerar relatório em HTML:

```bash
poetry run coverage html
# depois abra o arquivo
zen-browser htmlcov/index.html
```

---

## 🎯 Lint e formatação com Ruff

### Verificar problemas:

```bash
poetry run ruff check
```

### Corrigir automaticamente:

```bash
poetry run ruff check --fix
```

### Formatar com padrão definido:

```bash
poetry run ruff format
```

---

## 🧰 Task Runner (taskipy)

Algumas tarefas estão automatizadas:

```bash
# Lint
poetry run task lint

# Formatação automática
poetry run task format

# Executar aplicação
poetry run task run

# Executar testes com cobertura
poetry run task test
```

---

## 🔐 Gerar chave secreta para JWT

```python
import secrets
secrets.token_hex(32)
```

---

## 📁 Estrutura do projeto

```
fastapi_zero/
│
├── app.py                 # Ponto de entrada da aplicação
├── database/              # Conexão e configuração com banco de dados
├── models/                # Modelos do SQLAlchemy
├── schemas/               # Schemas do Pydantic
├── security/              # Lógica de autenticação e segurança
├── tests/                 # Testes automatizados
└── ...
```

---

## 📄 .gitignore

Crie seu `.gitignore` com:

```bash
pipx run ignr -p python > .gitignore
```

---

## 🧪 Ferramentas utilizadas

- ✅ **FastAPI** para APIs assíncronas e robustas
- ✅ **SQLAlchemy 2.0** como ORM
- ✅ **Alembic** para migrations
- ✅ **JWT (PyJWT)** para autenticação
- ✅ **pytest + pytest-cov** para testes
- ✅ **ruff** para lint e formatação
- ✅ **taskipy** para automatizar tarefas

---

## 📬 Autor

**Gilson Russo**  
[Email](mailto:gilsonrusso@outlook.com)

---

## 📜 Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).
