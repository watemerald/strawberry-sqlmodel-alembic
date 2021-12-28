from contextlib import asynccontextmanager
from typing import AsyncGenerator

from pydantic import BaseSettings, Field
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm.session import sessionmaker
from sqlmodel import SQLModel


class DBSettings(BaseSettings):
    db_url: str = Field(..., env="DATABASE_URL")

    class Config:
        env_file = ".env"


db_url = DBSettings().db_url

engine = create_async_engine(db_url, echo=True)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False, autocommit=False, autoflush=False
    )
    async with async_session() as session:
        async with session.begin():
            try:
                yield session
            finally:
                await session.close()
