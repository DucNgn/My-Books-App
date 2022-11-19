from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from backend.models.shelf import Shelves
from backend.crud.base import CRUDBase
from backend.schemas.shelf import ShelvesCreate, ShevlesUpdate


class CRUDShelves(CRUDBase[Shelves, ShelvesCreate, ShevlesUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: ShelvesCreate, owner_id: int
    ) -> Shelves:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_owner_id(self, db: Session, owner_id: int) -> Optional[Shelves]:
        return db.query(Shelves).filter(Shelves.owner_id == owner_id).first()


shelves = CRUDShelves(Shelves)
