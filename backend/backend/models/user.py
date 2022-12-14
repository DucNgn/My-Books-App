from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ARRAY
from sqlalchemy.orm import relationship

from backend.db.base_class import Base

if TYPE_CHECKING:
    from .shelf import Shelves  # noqa: F401


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    favorite_genres = Column(ARRAY(String))
    shelves = relationship("Shelves", back_populates="owner")
