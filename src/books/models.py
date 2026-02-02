from datetime import datetime, date
import uuid
from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg


class Book(SQLModel, table=True):
    __tablename__ = "books"
    id: uuid.UUID = Field(
        sa_column=Column(primary_key=True, index=True, unique=True, default=uuid.uuid4, type_=pg.UUID)
    )
    title: str
    author: str
    publisher: str
    published_date: date
    pages: int
    language: str
    created_at: datetime = Field(sa_column=Column(default=datetime.now, type_=pg.TIMESTAMP))
    updated_at: datetime = Field(sa_column=Column(default=datetime.now, onupdate=datetime.now, type_=pg.TIMESTAMP))

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author}, publisher={self.publisher})>"
