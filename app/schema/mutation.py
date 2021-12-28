import strawberry

from app import models
from app.db import get_session

from .types import Artist, Song, SongCreate


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_song(self, song: SongCreate) -> Song:
        async with get_session() as session:
            dbsong = models.Song(name=song.name, artist_id=int(song.artist_id))
            session.add(dbsong)
            await session.commit()
        return Song.marshal(dbsong)

    @strawberry.mutation
    async def create_artist(self, name: str) -> Artist:
        async with get_session() as session:
            dbartist = models.Artist(name=name)
            session.add(dbartist)
            await session.commit()
        return Artist.marshal(dbartist)
