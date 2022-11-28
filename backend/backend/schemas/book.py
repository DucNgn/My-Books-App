from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    rating: Optional[str] = None
    description: Optional[str]= None
    isbn: Optional[str] = None
    genre: Optional[str] = None
    num_of_pages: Optional[int] = None
    publisher: Optional[str] = None
    publication_year: Optional[str] = None
    cover_image_url: Optional[str] = None


class BookCreate(BookBase):
    title: str
    author: str
    genre: str


class BookUpdate(BookBase):
    pass


class BookInDBBase(BookBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Book(BookInDBBase):
    pass


class BookInDB(BookInDBBase):
    pass

class BookSearch(BaseModel):
    book_title: str
