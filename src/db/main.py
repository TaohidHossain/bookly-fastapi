from sqlmodel import SQLModel, create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

from src.config import Config

engine = AsyncEngine(
    create_engine(
        Config.DB_URL,
        echo=True,
        future=True,
        connect_args={"timeout": 15},
    )
)

async def init_db():
    async with engine.begin() as conn:
        from src.books.models import Book  # Import here to avoid circular imports
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncSession: # type: ignore
    session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with session() as s:
        yield s