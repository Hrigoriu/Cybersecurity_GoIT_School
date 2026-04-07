from typing import Optional
from mongoengine import connect
from models import Contact
from config import Config
from logger import RetroLogger

class ContactRepository:
    """
    Паттерн Repository для інкапсуляції логіки роботи з базою даних.
    Забезпечує абстракцію над ODM.
    """
    @staticmethod
    def connect_db():
        """Встановлює з'єднання з MongoDB."""
        connect(host=Config.MONGO_URI)
        RetroLogger.info("SYSTEM: MongoDB Connection Established.")

    @staticmethod
    def create_contact(data: dict) -> str:
        """Створює новий контакт і повертає його ObjectID як рядок."""
        contact = Contact(**data).save()
        return str(contact.id)

    @staticmethod
    def get_contact_by_id(contact_id: str) -> Optional[Contact]:
        """Отримує контакт за його унікальним ідентифікатором."""
        try:
            return Contact.objects.get(id=contact_id) # type: ignore
        except Contact.DoesNotExist: # type: ignore
            RetroLogger.error(f"Contact {contact_id} not found in database.")
            return None

    @staticmethod
    def mark_as_sent(contact_id: str) -> bool:
        """Оновлює статус відправки повідомлення на True."""
        contact = ContactRepository.get_contact_by_id(contact_id)
        if contact:
            contact.is_sent = True
            contact.save()
            return True
        return False
