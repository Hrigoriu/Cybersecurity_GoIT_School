import os
from dotenv import load_dotenv

# Завантажуємо змінні оточення з файлу .env
load_dotenv()

class Config:
    """Клас для зберігання конфігурації додатку."""
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/test_db")
    RABBITMQ_URI = os.getenv("RABBITMQ_URI", "amqp://localhost/")
    QUEUE_EMAIL = "email_queue"
    QUEUE_SMS = "sms_queue"
