from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend import crud, models, schemas
from backend.api import deps

router = APIRouter()


@router.get("/", response_model=schemas.Shelves)
def get_shelves(
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
