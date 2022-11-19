from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, ARRAY
from sqlalchemy.orm import relationship

from backend.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Shelves(Base):
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    reading_shelf = Column(ARRAY(String))
    toread_shelf = Column(ARRAY(String))
    read_shelf = Column(ARRAY(String))
    favorite_shelf = Column(ARRAY(String))
    recommendation_shelf = Column(ARRAY(String))
    owner = relationship("User", back_populates="shelves")
