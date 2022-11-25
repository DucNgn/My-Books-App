from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend import crud, models, schemas
from backend.api import deps

router = APIRouter()


@router.get("/", response_model=schemas.Book)
def get_book_by_id(db: Session = Depends(deps.get_db), id: str = "") -> Any:
    """
    Retrieve shelves for the current user.
    """
    current_book = crud.book.get(db=db, id=id)
    if not current_book:
        raise HTTPException(status_code=404, detail="Invalid Book Request")
    return current_book
