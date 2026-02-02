from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine

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
        statement = text("SELECT 'hello';")  # Placeholder for actual initialization SQL
        result = await conn.execute(statement)
        print(result.all())