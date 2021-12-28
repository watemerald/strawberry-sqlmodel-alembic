from fastapi import FastAPI

from app.graphql import graphql_app

app = FastAPI()


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


app.include_router(graphql_app, prefix="/graphql")
