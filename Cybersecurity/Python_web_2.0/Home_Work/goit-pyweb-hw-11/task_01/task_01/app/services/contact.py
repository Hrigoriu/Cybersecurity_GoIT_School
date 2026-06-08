#app/services/contact.py
from typing import List
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.contact import ContactCreate, ContactUpdate, ContactResponse
from app.repositories.contact import ContactRepository

class ContactService:
    """
    Патерн Service.
    Відповідає за бізнес-логіку (перевірки на унікальність, викидання помилок).
    """
    def __init__(self, session: AsyncSession):
        self.repo = ContactRepository(session)

    async def create_contact(self, contact_in: ContactCreate) -> ContactResponse:
        # Перевірка чи існує вже контакт з таким email (DRY & SOLID)
        existing_contact = await self.repo.get_by_email(contact_in.email)
        if existing_contact:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Контакт з такою електронною адресою вже існує."
            )
        return await self.repo.create(contact_in)

    async def get_contacts(self, skip: int, limit: int) -> List[ContactResponse]:
        return await self.repo.get_all(skip, limit)

    async def get_contact_by_id(self, contact_id: int) -> ContactResponse:
        contact = await self.repo.get_by_id(contact_id)
        if not contact:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Контакт не знайдено.")
        return contact

    async def update_contact(self, contact_id: int, contact_in: ContactUpdate) -> ContactResponse:
        db_contact = await self.repo.get_by_id(contact_id)
        if not db_contact:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Контакт не знайдено.")

        # Перевірка унікальності email при оновленні
        if contact_in.email and contact_in.email != db_contact.email:
            existing = await self.repo.get_by_email(contact_in.email)
            if existing:
                raise HTTPException(status_code=409, detail="Email вже використовується.")

        return await self.repo.update(db_contact, contact_in)

    async def delete_contact(self, contact_id: int) -> None:
        db_contact = await self.repo.get_by_id(contact_id)
        if not db_contact:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Контакт не знайдено.")
        await self.repo.delete(db_contact)

    async def search_contacts(self, query: str) -> List[ContactResponse]:
        return await self.repo.search(query)

    async def upcoming_birthdays(self) -> List[ContactResponse]:
        return await self.repo.get_upcoming_birthdays(days=7)
