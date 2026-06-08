#app/api/contacts.py
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from app.db.database import get_db
from app.schemas.contact import ContactCreate, ContactUpdate, ContactResponse
from app.services.contact import ContactService

router = APIRouter(prefix="/contacts", tags=["Contacts"])

def get_contact_service(db: AsyncSession = Depends(get_db)) -> ContactService:
    """Dependency Injection для сервісу бізнес-логіки."""
    return ContactService(db)

@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED, summary="Створити новий контакт")
async def create_contact(contact_in: ContactCreate, service: ContactService = Depends(get_contact_service)):
    """Створює новий контакт. Перевіряє унікальність email."""
    return await service.create_contact(contact_in)

@router.get("/", response_model=List[ContactResponse], summary="Отримати список контактів")
async def get_contacts(
    skip: int = Query(0, ge=0, description="Пагінація: пропустити N записів"),
    limit: int = Query(100, ge=1, le=1000, description="Пагінація: ліміт записів"),
    service: ContactService = Depends(get_contact_service)
):
    """Повертає список контактів з можливістю пагінації."""
    return await service.get_contacts(skip, limit)

@router.get("/search/", response_model=List[ContactResponse], summary="Пошук контактів")
async def search_contacts(
    q: str = Query(..., min_length=2, description="Пошуковий запит (Ім'я, Прізвище, Email)"),
    service: ContactService = Depends(get_contact_service)
):
    """Пошук контактів за частковим збігом (Full Text Search/ILike)."""
    return await service.search_contacts(q)

@router.get("/birthdays/", response_model=List[ContactResponse], summary="Дні народження")
async def upcoming_birthdays(service: ContactService = Depends(get_contact_service)):
    """Повертає список контактів, у яких день народження протягом наступних 7 днів."""
    return await service.upcoming_birthdays()

@router.get("/{contact_id}", response_model=ContactResponse, summary="Отримати контакт за ID")
async def get_contact(contact_id: int, service: ContactService = Depends(get_contact_service)):
    """Отримання конкретного контакту за його унікальним ідентифікатором."""
    return await service.get_contact_by_id(contact_id)

@router.patch("/{contact_id}", response_model=ContactResponse, summary="Оновити контакт")
async def update_contact(contact_id: int, contact_in: ContactUpdate, service: ContactService = Depends(get_contact_service)):
    """Часткове оновлення інформації про існуючий контакт."""
    return await service.update_contact(contact_id, contact_in)

@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Видалити контакт")
async def delete_contact(contact_id: int, service: ContactService = Depends(get_contact_service)):
    """Повне видалення контакту з бази даних."""
    await service.delete_contact(contact_id)
