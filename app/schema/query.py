import strawberry
from sqlalchemy.future import select

from app import models
from app.db import get_session

from .types import Artist, Song


@strawberry.type
class Query:
    @strawberry.field
    async def songs(self) -> list[Song]:
        async with get_session() as session:
            sql = select(models.Song).order_by(models.Song.id)
            db_tasks = await session.execute(sql)
            vals = db_tasks.scalars().all()
        return [Song.marshal(v) for v in vals]

    @strawberry.field
    async def song_by_id(self, id: strawberry.ID) -> Song:
        async with get_session() as session:
            sql = select(models.Song).where(models.Song.id == id)
            db_tasks = await session.execute(sql)
            val = db_tasks.scalars().first()
        return Song.marshal(val)  # type: ignore

    @strawberry.field
    async def artists(self) -> list[Artist]:
        async with get_session() as session:
            sql = select(models.Artist).order_by(models.Artist.id)
            db_tasks = await session.execute(sql)
            vals = db_tasks.scalars().all()
        return [Artist.marshal(v) for v in vals]

    @strawberry.field
    async def artist_by_id(self, id: strawberry.ID) -> Artist:
        async with get_session() as session:
            sql = select(models.Artist).where(models.Artist.id == id)
            db_tasks = await session.execute(sql)
            val = db_tasks.scalars().first()
        return Artist.marshal(val)  # type: ignore
