import strawberry
from sqlalchemy.future import select

from app import models
from app.db import get_session


@strawberry.type
class Song:
    id: strawberry.ID
    name: str
    artist_id: strawberry.ID

    @strawberry.field
    async def artist(self) -> "Artist":
        async with get_session() as session:
            sql = select(models.Artist).where(models.Artist.id == int(self.artist_id))
            db_tasks = await session.execute(sql)
            val = db_tasks.scalars().first()
        return Artist.marshal(val)  # type: ignore

    @classmethod
    def marshal(cls, model: models.Song) -> "Song":
        return cls(
            id=strawberry.ID(str(model.id)),
            name=model.name,
            artist_id=strawberry.ID(str(model.artist_id)),
        )


@strawberry.input
class SongCreate:
    name: str
    artist_id: strawberry.ID


@strawberry.type
class Artist:
    id: strawberry.ID
    name: str

    @strawberry.field
    async def songs(self) -> list[Song]:
        async with get_session() as session:
            sql = select(models.Song).where(models.Song.artist_id == int(self.id))
            db_tasks = await session.execute(sql)
            vals = db_tasks.scalars().all()
        return [Song.marshal(v) for v in vals]

    @classmethod
    def marshal(cls, model: models.Artist) -> "Artist":
        return cls(id=strawberry.ID(str(model.id)), name=model.name)
