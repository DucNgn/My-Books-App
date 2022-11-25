from typing import List, Optional

from sqlalchemy.orm import Session

from backend import crud, schemas


def extract_books(db: Session, books_list: Optional[List[str]]) -> List[schemas.Book]:
    if not books_list:
        return []
    result = []
    for id in books_list:
        book = crud.book.get(db=db, id=id)
        if not book:
            continue
        result.append(book)
    return result
