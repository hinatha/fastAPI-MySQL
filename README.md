# Overview
Project for todo app

## Structure

```bash
.
├── README.md
├── api
│   ├── __init__.py
│   ├── cruds
│   │   ├── __init__.py
│   │   ├── done.py
│   │   └── task.py
│   ├── db.py
│   ├── main.py
│   ├── migrate_db.py
│   ├── models
│   │   ├── __init__.py
│   │   └── task.py
│   ├── routers
│   │   ├── __init__.py
│   │   ├── done.py
│   │   └── task.py
│   └── schemas
│       ├── __init__.py
│       ├── done.py
│       └── task.py
├── docker-compose.yaml
├── dockerfile
├── poetry.lock
├── pyproject.toml
└── tests
    ├── __init__.py
    └── test_main.py

6 directories, 22 files
```

# Features
This app is able to use below function.

## User Story
- Add a task.
- See the list of tasks.
- Delete tasks.
- Change status of task.
- Edit tasks.

# Using of language, framework, technology
- Python
- fastAPI
- Docker compose
- MySQL
- SQLite3
- SQLAlchemy
- pymysql
- aiomysql
- GitHub Actions
- mypy
- flake8
- black
- isort
- dependabot
  
# Requirement
[tool.poetry.dependencies]
- python = "^3.9"
- fastapi = "^0.71.0"
- uvicorn = {extras = ["standard"], version = "^0.16.0"}
- SQLAlchemy = "^1.4.29"
- aiomysql = "^0.0.22"
- taskipy = "^1.9.0"

[tool.poetry.dev-dependencies]
- pytest-asyncio = "^0.17.0"
- aiosqlite = "^0.17.0"
- httpx = "^0.21.3"
- mypy = "^0.931"
- black = "^22.1.0"
- pyproject-flake8 = "^0.0.1-alpha.2"
- isort = "^5.10.1"

[build-system]
- requires = ["poetry-core>=1.0.0"]
- build-backend = "poetry.core.masonry.api"

# Installation
 
```bash
$ git clone https://github.com/hinatha/fastAPI-MySQL.git
$ cd fastAPI-MySQL  
$ docker-compose build
$ docker-compose run --entrypoint "poetry install" demo-app
```
 
# Usage
 
```bash
$ docker-compose up
```

# Test

```bash
$ docker-compose up
$ docker-compose exec demo-app poetry add -D pytest-asyncio aiosqlite httpx
$ docker-compose run --entrypoint "poetry run pytest" demo-app
$ docker-compose run --entrypoint "poetry run task lint" demo-app
$ docker-compose run --entrypoint "poetry run task fmt" demo-app
```
 
# Future plans
- Develop frontend with React.
