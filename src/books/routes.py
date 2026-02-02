from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.books.schemas import Book, BookCreate, BookUpdate
from src.db.main import get_session
from src.books.service import BookService


book_router = APIRouter()
book_service = BookService()


@book_router.get("/", response_model=list[Book], status_code=status.HTTP_200_OK)
async def list_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return [book[0] for book in books]

@book_router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate, session: AsyncSession = Depends(get_session)):
    return await book_service.create_book(book, session)

@book_router.get("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def get_book(book_id: str, session: AsyncSession = Depends(get_session)):
    book = await book_service.get_book_by_id(book_id, session)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book[0]

@book_router.put("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def update_book(book_id: str, book: BookUpdate, session: AsyncSession = Depends(get_session)):
    updated_book  = await book_service.update_book(book_id, book, session)
    if not updated_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return updated_book[0]

@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: str, session: AsyncSession = Depends(get_session)):
    deleted_book = await book_service.delete_book(book_id, session)
    if not deleted_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")