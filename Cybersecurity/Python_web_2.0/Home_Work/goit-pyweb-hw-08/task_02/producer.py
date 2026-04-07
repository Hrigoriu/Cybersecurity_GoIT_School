import random
from faker import Faker
from repository import ContactRepository
from services import RabbitMQService
from config import Config
from logger import RetroLogger

def generate_contacts(count: int = 10):
    """
    Генерує фейкові контакти (наприклад, пацієнтів) та відправляє їх ObjectID у відповідну чергу.
    """
    fake = Faker('uk_UA')
    repo = ContactRepository()
    repo.connect_db()
    mq_service = RabbitMQService()

    RetroLogger.info(f"PRODUCER: Starting generation of {count} contacts...")

    for _ in range(count):
        # Генеруємо профіль, близький до медичного контексту
        prefer_sms = random.choice([True, False])
        contact_data = {
            "full_name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "prefer_sms": prefer_sms,
            "diagnosis_code": f"J{random.randint(0, 99)}.{random.randint(0, 9)}"  # Наприклад, клас захворювань дихальних шляхів
        }

        # 1. Зберігаємо в БД
        contact_id = repo.create_contact(contact_data)
        RetroLogger.info(f"DB: Contact saved. ID: {contact_id} | Name: {contact_data['full_name']}")

        # 2. Визначаємо чергу
        target_queue = Config.QUEUE_SMS if prefer_sms else Config.QUEUE_EMAIL

        # 3. Відправляємо в RabbitMQ
        mq_service.publish_message(target_queue, contact_id)

    mq_service.close()
    RetroLogger.success("PRODUCER: Task completed. All contacts queued.")

if __name__ == "__main__":
    generate_contacts(15)
