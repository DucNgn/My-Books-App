from sqlalchemy import Column, Float, Integer, String
from backend.db.base_class import Base


class Book(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    rating = Column(String)
    description = Column(String)
    isbn = Column(String)
    genre = Column(String)
    num_of_pages = Column(Integer)
    publisher = Column(String)
    publication_year = Column(String)
    cover_image_url = Column(String)
