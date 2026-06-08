#app/db/models.py
from sqlalchemy import Column, Integer, String, Date
from app.db.database import Base

class Contact(Base):
    """
    ORM Модель контакту (відображення таблиці в БД).
    Додано індекси для полів, за якими здійснюється пошук, для оптимізації SQL-запитів.
    """
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), index=True, nullable=False)
    last_name = Column(String(50), index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phone = Column(String(20), nullable=False)
    birthday = Column(Date, nullable=False)
    additional_info = Column(String(500), nullable=True)
