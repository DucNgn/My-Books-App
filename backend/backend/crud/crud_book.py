from typing import List

from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import not_

from backend.models.book import Book
from backend.crud.base import CRUDBase
from backend.schemas.book import BookCreate, BookUpdate


class CRUDBook(CRUDBase[Book, BookCreate, BookUpdate]):
    def get_suggestions(self, db: Session, favorite_genres: List[str]) -> List[str]:
        """
        Get Suggestions based on favorite genres declared by user.
        Return a list of Book IDs that match the genre
        """
        # Always refer to genre in lowercase when interact with database.
        favorite_genres = set([genre.lower() for genre in favorite_genres])
        recommended_books = (
            db.query(Book).filter(func.lower(Book.genre).in_(favorite_genres)).all()
        )

        recommended_book_ids = [book.id for book in recommended_books]
        return recommended_book_ids

    def search_by_title(self, db: Session, title: str):
        """
        Get Book by title, case insensitive.
        """
        book_result = (
            db.query(Book).filter(func.lower(Book.title).contains(title.lower())).all()
        )
        return book_result

    def search_by_title_exclude_ids(
        self, db: Session, title: str, exclude_ids: List[int] = []
    ):
        """
        Get Book by title, case insensitive, exclude all books with id in exclude_ids
        """
        book_result = (
            db.query(Book)
            .filter(
                func.lower(Book.title).contains(title.lower())
                & not_(Book.id.in_(exclude_ids))
            )
            .all()
        )
        return book_result


book = CRUDBook(Book)
