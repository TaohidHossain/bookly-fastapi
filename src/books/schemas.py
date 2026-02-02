from datetime import datetime
import uuid
from pydantic import BaseModel


class Book(BaseModel):
    id: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: datetime
    language: str
    pages: int
    created_at: datetime
    updated_at: datetime

class BookCreate(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    language: str
    pages: int

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    publisher: str | None = None
    pages: int | None = None
    language: str | None = None

