from typing import Any, List

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


@router.post("/search", response_model=List[schemas.Book])
def search_book_by_title(
    db: Session = Depends(deps.get_db), book_title: str = ""
) -> Any:
    """
    Retrieve book based on the title
    """
    search_result = crud.book.search_by_title(db=db, title=book_title)
    return search_result


@router.post("/search", response_model=List[schemas.Book])
def search_book_by_title(
    db: Session = Depends(deps.get_db), book_title: str = ""
) -> Any:
    """
    Retrieve book based on the title
    """
    search_result = crud.book.search_by_title(db=db, title=book_title)
    return search_result


@router.put("/search_not_on_shelves", response_model=List[schemas.Book])
def search_book_by_title_not_on_shelves(
    *,
    db: Session = Depends(deps.get_db),
    book_search: schemas.BookSearch,
    current_user: models.user = Depends(deps.get_current_active_user),
):
    if not book_search.book_title.strip():
        return []
    shelves = crud.shelves.get_by_owner_id(db, owner_id=current_user.id)
    if not shelves:
        raise HTTPException(status_code=404, detail="The user does not have any shelf")
    all_book_ids_on_shelves = set()
    for shelf in [
        shelves.read_shelf,
        shelves.reading_shelf,
        shelves.recommendation_shelf,
        shelves.toread_shelf,
        shelves.favorite_shelf,
    ]:
        if shelf:
            all_book_ids_on_shelves.update(shelf)
    search_results = crud.book.search_by_title_exclude_ids(
        db=db, title=book_search.book_title, exclude_ids=all_book_ids_on_shelves
    )
    return search_results
