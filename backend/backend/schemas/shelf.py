from typing import Optional, List

from pydantic import BaseModel


# Shared properties
class ShelvesBase(BaseModel):
    ...


# Properties to receive on item creation
class ShelvesCreate(ShelvesBase):
    reading_shelf: List[str]
    toread_shelf: List[str]
    read_shelf: List[str]
    favorite_shelf: List[str]


# Properties to receive on item update
class ShevlesUpdate(ShelvesBase):
    reading_shelf: Optional[List[str]]
    toread_shelf: Optional[List[str]]
    read_shelf: Optional[List[str]]
    favorite_shelf: Optional[List[str]]
    recommendation_shelf: Optional[List[str]]


# Properties shared by models stored in DB
class ShelvesInDBBase(ShelvesBase):
    id: int
    owner_id: int
    reading_shelf: List[str]
    toread_shelf: List[str]
    read_shelf: List[str]
    favorite_shelf: List[str]
    recommendation_shelf: List[str]

    class Config:
        orm_mode = True


# Properties to return to client
class Shelves(ShelvesInDBBase):
    pass


# Properties properties stored in DB
class ShelvesInDB(ShelvesInDBBase):
    pass
