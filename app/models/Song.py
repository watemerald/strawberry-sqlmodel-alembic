from sqlmodel import Field, SQLModel


class Song(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

    artist_id: int = Field(default=None, foreign_key="artist.id")
