import json
from src.database.repository import MongoRepository
from src.config import Config
from src.logger import RetroLogger

class DataService:
    """
    Паттерн Service: Координує бізнес-процеси збереження даних.
    Сюди Scrapy Pipeline передає зібрані дані.
    """
    def __init__(self):
        self.repo = MongoRepository()

    def process_and_save_data(self, authors: list, quotes: list):
        """
        Зберігає дані в JSON та синхронізує з хмарною БД.
        Гарантує цілісність: спочатку зберігаються автори, потім цитати.
        """
        # 1. Експорт у JSON
        self._export_to_json(Config.JSON_AUTHORS_PATH, authors)
        self._export_to_json(Config.JSON_QUOTES_PATH, quotes)

        # 2. Експорт у MongoDB
        self.repo.initialize()
        RetroLogger.process(f"SYNCING DATA: {len(authors)} Authors, {len(quotes)} Quotes...")

        # Створюємо словник авторів для швидкого зв'язування O(1) замість O(n)
        author_cache = {}
        for author_data in authors:
            author_obj = self.repo.upsert_author(author_data)
            author_cache[author_data['fullname']] = author_obj

        for quote_data in quotes:
            author_name = quote_data.pop('author') # Витягуємо ім'я
            author_obj = author_cache.get(author_name)
            if author_obj:
                self.repo.save_quote(quote_data, author_obj)

        self.repo.close()
        RetroLogger.success("DATA SYNC COMPLETE. System Standby.")

    def _export_to_json(self, filepath: str, data: list):
        """Допоміжний метод для запису JSON."""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        RetroLogger.success(f"FILE GENERATED: {filepath}")
