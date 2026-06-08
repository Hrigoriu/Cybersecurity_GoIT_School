#app/repositories/contact.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_, and_, func
from datetime import datetime, timedelta
from typing import List, Optional

from app.db.models import Contact
from app.schemas.contact import ContactCreate, ContactUpdate
from app.core.logger import log

class ContactRepository:
    """
    Патерн Repository.
    Ізолює логіку доступу до бази даних (SQLAlchemy) від бізнес-логіки.
    """
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, contact_in: ContactCreate) -> Contact:
        log.info(f"INITIATING DB WRITE: Оновлення бази даних новим контактом {contact_in.email}")
        db_contact = Contact(**contact_in.model_dump())
        self.session.add(db_contact)
        await self.session.commit()
        await self.session.refresh(db_contact)
        return db_contact

    async def get_by_id(self, contact_id: int) -> Optional[Contact]:
        result = await self.session.execute(select(Contact).where(Contact.id == contact_id))
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> Optional[Contact]:
        result = await self.session.execute(select(Contact).where(Contact.email == email))
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Contact]:
        result = await self.session.execute(select(Contact).offset(skip).limit(limit))
        return list(result.scalars().all())

    async def search(self, query: str) -> List[Contact]:
        """Пошук за частковим збігом (ігноруючи регістр) в імені, прізвищі або email."""
        log.info(f"QUERY EXECUTION: Пошук за критерієм '{query}'")
        search_pattern = f"%{query}%"
        stmt = select(Contact).where(
            or_(
                Contact.first_name.ilike(search_pattern),
                Contact.last_name.ilike(search_pattern),
                Contact.email.ilike(search_pattern)
            )
        )
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def get_upcoming_birthdays(self, days: int = 7) -> List[Contact]:
        """
        Використовує форматування 'MMDD' на рівні БД, щоб обробити високосні роки
        та безпечно перейти через Новий Рік (грудень-січень).
        """
        log.info(f"CRON/QUERY: Розрахунок днів народжень на наступні {days} днів")
        today = datetime.today().date()
        target_date = today + timedelta(days=days)

        today_mmdd = today.strftime("%m%d")
        target_mmdd = target_date.strftime("%m%d")

        # Функція бази даних для приведення дати до формату 'MMDD'
        birthday_mmdd = func.to_char(Contact.birthday, 'MMDD')

        # Логіка обробки переходу через кінець року
        if today_mmdd <= target_mmdd:
            condition = and_(birthday_mmdd >= today_mmdd, birthday_mmdd <= target_mmdd)
        else:
            # Наприклад, сьогодні 28 грудня (1228), а кінець періоду 4 січня (0104)
            condition = or_(birthday_mmdd >= today_mmdd, birthday_mmdd <= target_mmdd)

        result = await self.session.execute(select(Contact).where(condition))
        return list(result.scalars().all())

    async def update(self, db_contact: Contact, contact_in: ContactUpdate) -> Contact:
        update_data = contact_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_contact, key, value)
        await self.session.commit()
        await self.session.refresh(db_contact)
        log.info(f"DB UPDATE: Запис {db_contact.id} успішно модифіковано.")
        return db_contact

    async def delete(self, db_contact: Contact) -> None:
        await self.session.delete(db_contact)
        await self.session.commit()
        log.info(f"DB DELETE: Запис {db_contact.id} видалено з системи.")
