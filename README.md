## Run project

```bash
poetry run fastapi dev fastapi_zero/app.py

````

### Ruff
```bash
 poetry run ruff check
 poetry run ruff format
```

### Pytest
```bash
pytest
pytest --cov=fastapi_zero -v

coverage html

zen-browser htmlcov/index.html
````

### Create git ignore
```bash
pipx run ignr -p python > .gitignore
````

### Create secret
```bash
python

import secrets

secrets.token_hex(32)
````