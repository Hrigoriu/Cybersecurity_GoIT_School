from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    img_url = Column(String)
    rating = Column(Integer)
    title = Column(String)
    price = Column(Float)
