from typing import List

from sqlalchemy.orm import Session

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
            db.query(Book).filter(Book.genre.in_(favorite_genres)).all()
        )
        
        recommended_book_ids = [book.id for book in recommended_books]
        return recommended_book_ids


book = CRUDBook(Book)