from typing import Optional, List

from pydantic import BaseModel
from .book import Book


# Shared properties
class ShelvesBase(BaseModel):
    reading_shelf: Optional[List[str]]
    toread_shelf: Optional[List[str]]
    read_shelf: Optional[List[str]]
    favorite_shelf: Optional[List[str]]
    recommendation_shelf: Optional[List[str]]


# Properties to receive on item creation
class ShelvesCreate(ShelvesBase):
    reading_shelf: List[str]
    toread_shelf: List[str]
    read_shelf: List[str]
    favorite_shelf: List[str]
    recommendation_shelf: List[str]


# Properties to receive on item update
class ShelvesUpdate(ShelvesBase):
    pass


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


class ShelvesWithBooks(Shelves):
    reading_shelf: Optional[List[Book]] = []
    toread_shelf: Optional[List[Book]] = []
    read_shelf: Optional[List[Book]] = []
    favorite_shelf: Optional[List[Book]] = []
    recommendation_shelf: Optional[List[Book]] = []
