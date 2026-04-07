import os

import redis
from config.db import init_mongodb
from dotenv import load_dotenv
from models.author import Author
from models.quote import Quote
from utils.logger import RetroTerminal

# Завантажуємо змінні середовища, якщо Redis налаштований через .env
load_dotenv()


def clean():
    # 1. Очищення MongoDB
    init_mongodb()
    Author.drop_collection()
    Quote.drop_collection()
    RetroTerminal.print_sys(
        "Базу даних MongoDB повністю очищено від старих даних та дублікатів!"
    )

    # 2. Очищення кешу Redis
    try:
        redis_host = os.getenv("REDIS_HOST", "localhost")
        redis_port = int(os.getenv("REDIS_PORT", 6379))

        # Підключаємось до Redis та очищаємо всю базу ключів
        cache = redis.Redis(host=redis_host, port=redis_port, db=0)
        cache.flushdb()
        RetroTerminal.print_sys("Кеш Redis успішно скинуто!")
    except Exception as e:
        RetroTerminal.print_sys(f"Помилка при очищенні кешу Redis: {e}")


if __name__ == "__main__":
    clean()
