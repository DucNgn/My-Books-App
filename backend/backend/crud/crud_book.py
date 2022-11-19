from backend.models.book import Book
from backend.crud.base import CRUDBase
from backend.schemas.book import BookCreate, BookUpdate


class CRUDBook(CRUDBase[Book, BookCreate, BookUpdate]):
    pass

book = CRUDBook(Book)