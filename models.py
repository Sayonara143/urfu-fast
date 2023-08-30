from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    datetime = Column(DateTime)

