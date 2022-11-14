from typing import Optional

from pydantic import BaseModel


# Shared properties
class ShelfBase(BaseModel):
    title: Optional[str] = None


# Properties to receive on item creation
class ShelfCreate(ShelfBase):
    title: str


# Properties to receive on item update
class ShelfUpdate(ShelfBase):
    pass


# Properties shared by models stored in DB
class ShelfInDBBase(ShelfBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Shelf(ShelfInDBBase):
    pass


# Properties properties stored in DB
class ShelfInDB(ShelfInDBBase):
    pass
