from datetime import datetime
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc

from books.schemas import BookCreate, BookUpdate
from books.models import Book as BookModel

class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(BookModel).order_by(desc(BookModel.created_at))
        results = await session.execute(statement)
        return results.all()

    async def get_book_by_id(self, book_id: str, session: AsyncSession):
        statement = select(BookModel).where(BookModel.id == book_id)
        results = await session.execute(statement)
        return results.one_or_none()

    async def create_book(self, book_data: BookCreate, session: AsyncSession):
        book_data_dict = book_data.model_dump()
        book = BookModel(**book_data_dict)
        book.published_date = datetime.strptime(book_data_dict["published_date"], "%Y-%m-%d").date()
        print(book.published_date)

        session.add(book)
        await session.commit()
        await session.refresh(book)
        return book

    async def update_book(self, book_id: str, book_data: BookUpdate, session: AsyncSession) -> dict:
        book_to_update = await self.get_book_by_id(book_id, session)
        if not book_to_update:
            return None
        for key, value in book_data.model_dump(exclude_unset=True).items():
            setattr(book_to_update[0], key, value)
        session.add(book_to_update[0])
        await session.commit()
        await session.refresh(book_to_update[0])
        return book_to_update

    async def delete_book(self, book_id: str, session: AsyncSession):
        book_to_delete = await self.get_book_by_id(book_id, session)
        if not book_to_delete:
            return None
        await session.delete(book_to_delete[0])
        await session.commit()
        return book_to_delete