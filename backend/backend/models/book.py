from sqlalchemy import Column, Float, Integer, String

from backend.db.base_class import Base


class Book(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    genre = Column(String)
    isbn = Column(Float)
    publication_year = Column(Integer)
    cover_image_url = Column(String)
    num_of_pages = Column(Integer)
