import os
import redis
from mongoengine import connect
from dotenv import load_dotenv
from utils.logger import RetroTerminal

# Завантажуємо змінні середовища з файлу .env
load_dotenv()

def init_mongodb() -> None:
    """Ініціалізація з'єднання з MongoDB Atlas."""
    uri = os.getenv("MONGODB_URI")
    if not uri:
        RetroTerminal.print_error("MONGODB_URI не знайдено у .env файлі!")
        exit(1)

    connect(host=uri)
    RetroTerminal.print_db("MongoDB Atlas підключено успішно.")

def get_redis_client() -> redis.Redis:
    """Повертає клієнт Redis для кешування."""
    host = os.getenv("REDIS_HOST", "localhost")
    port = int(os.getenv("REDIS_PORT", 6379))
    password = os.getenv("REDIS_PASSWORD", None)

    client = redis.Redis(host=host, port=port, password=password, decode_responses=True)
    try:
        client.ping()
        RetroTerminal.print_db("Redis кеш підключено успішно.")
    except redis.ConnectionError:
        RetroTerminal.print_error("Не вдалося підключитися до Redis. Кешування буде вимкнено.")

    return client
