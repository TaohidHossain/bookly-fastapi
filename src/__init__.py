from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.db.main import init_db

version = "v1"
description = """
A REST API for a book review web service.

This REST API is able to;
- Create Read Update And delete books
- Add reviews to books
- Add tags to Books e.t.c.
"""

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code here
    print("Starting up...")
    await init_db()
    yield
    # Shutdown code here
    print("Shutting down...")


app = FastAPI(
    title="Book Review API",
    version=version,
    description=description,
    lifespan=lifespan,
)

