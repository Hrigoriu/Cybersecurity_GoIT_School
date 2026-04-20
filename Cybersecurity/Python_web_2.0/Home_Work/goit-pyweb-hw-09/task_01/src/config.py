import os
from pathlib import Path
from dotenv import load_dotenv

# 1. Визначаємо абсолютний шлях до кореня проекту (на рівень вище від папки src)
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Будуємо точний шлях до файлу .env
ENV_PATH = BASE_DIR / '.env'

# 3. Примусово читаємо саме цей файл
load_dotenv(dotenv_path=ENV_PATH)

class Config:
    """Конфігурація додатку з використанням змінних оточення."""

    # Тепер os.getenv гарантовано побачить змінну з файлу
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/quotes_hw08")

    JSON_QUOTES_PATH = "quotes.json"
    JSON_AUTHORS_PATH = "authors.json"
