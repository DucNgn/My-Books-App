from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend import crud, models, schemas
from backend.api import deps
from . import utils

router = APIRouter()


@router.get("/", response_model=schemas.Shelves)
def get_shelves_with_books_id(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve shelves for the current user.
    """
    current_shelves = crud.shelves.get_by_owner_id(db, owner_id=current_user.id)
    if not current_shelves:
        raise HTTPException(status_code=404, detail="The user does not have any shelf")
    return current_shelves


@router.get("/all", response_model=schemas.ShelvesWithBooks)
def get_shelves_with_books_props(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve shelves for the current user.
    """
    current_shelves = crud.shelves.get_by_owner_id(db, owner_id=current_user.id)
    if not current_shelves:
        raise HTTPException(status_code=404, detail="The user does not have any shelf")

    current_shelves.toread_shelf = utils.extract_books(db, current_shelves.toread_shelf)
    current_shelves.reading_shelf = utils.extract_books(
        db, current_shelves.reading_shelf
    )
    current_shelves.read_shelf = utils.extract_books(db, current_shelves.read_shelf)
    current_shelves.favorite_shelf = utils.extract_books(
        db, current_shelves.favorite_shelf
    )
    current_shelves.recommendation_shelf = utils.extract_books(
        db, current_shelves.recommendation_shelf
    )
    return current_shelves


@router.put("/", response_model=schemas.Shelves)
def update_shelves(
    *,
    db: Session = Depends(deps.get_db),
    shelves_in: schemas.ShevlesUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser)
):
    shelves = crud.shelves.get_by_owner_id(db, owner_id=current_user.id)
    if not shelves:
        raise HTTPException(status_code=404, detail="The user does not have any shelf")
    shelves = crud.shelves.update(db, db_obj=shelves, obj_in=shelves_in)
    return shelves
