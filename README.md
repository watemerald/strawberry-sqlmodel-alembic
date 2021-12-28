# Python Strawberry, SQLModel, alembic template

This is a repository meant to scaffold a template for a python GraphQL server. It is meant to be used as a starting point for a new project.

It uses [Strawberry GraphQL](https://strawberry.rocks) for the GraphQL server, [FastAPI](https://fastapi.tiangolo.com/) for the ASGI server, and [SQLModel](https://sqlmodel.tiangolo.com/) for the database. Database migrations are handled using [Alembic](https://alembic.sqlalchemy.org/en/latest/).

## Installation

Copy the .env.example file to .env and fill in the values as appropriate.

```bash
cp .env.example .env
```

Install the dependencies using [poetry](https://python-poetry.org/):

```bash
poetry install
```

_If using docker for development_ launch the db using docker-compose:

```bash
docker-compose up -d
```

Run the development server using:

```bash
uvicorn main:app --reload
```
