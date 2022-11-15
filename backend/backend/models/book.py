from sqlalchemy import Column, Float, ForeignKey, Integer, String
from backend.db.base_class import Base


class Book(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    book_genre = Column(String)
    isbn = Column(Float)
    year_of_publication = Column(Integer)
    cover_image_url = Column(String)
    num_of_pages = Column(Integer)
