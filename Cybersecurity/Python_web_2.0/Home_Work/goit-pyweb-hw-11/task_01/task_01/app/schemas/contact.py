#app/schemas/contact.py
from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import Optional

class ContactBase(BaseModel):
    """Базова схема з основними полями контакту."""
    first_name: str = Field(..., min_length=2, max_length=50, description="Ім'я контакту")
    last_name: str = Field(..., min_length=2, max_length=50, description="Прізвище контакту")
    email: EmailStr = Field(..., description="Електронна пошта")
    phone: str = Field(..., min_length=7, max_length=20, description="Номер телефону")
    birthday: date = Field(..., description="Дата народження")
    additional_info: Optional[str] = Field(None, max_length=500, description="Додаткові дані")

class ContactCreate(ContactBase):
    """Схема для створення нового контакту."""
    pass

class ContactUpdate(BaseModel):
    """Схема для часткового оновлення контакту (усі поля опціональні)."""
    first_name: Optional[str] = Field(None, min_length=2, max_length=50)
    last_name: Optional[str] = Field(None, min_length=2, max_length=50)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, min_length=7, max_length=20)
    birthday: Optional[date] = None
    additional_info: Optional[str] = Field(None, max_length=500)

class ContactResponse(ContactBase):
    """Схема для повернення даних контакту клієнту."""
    id: int

    class Config:
        from_attributes = True  # Дозволяє Pydantic читати дані з ORM SQLAlchemy
