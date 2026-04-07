import json
from redis.exceptions import ConnectionError
from config.db import get_redis_client
from repositories.quote_repository import QuoteRepository
from utils.logger import RetroTerminal

redis_client = get_redis_client()

class SearchService:
    """Сервіс для пошуку цитат із застосуванням кешування."""

    @staticmethod
    def _cache_result(key: str, data_fetcher_func) -> list:
        """Внутрішній метод для роботи з Redis кешем (DRY)."""
        try:
            cached_data = redis_client.get(key)
            if cached_data:
                RetroTerminal.print_sys(f"Дані отримано з кешу Redis (ключ: {key})")
                return json.loads(cached_data)
        except ConnectionError:
            pass # Якщо Redis недоступний, просто йдемо в БД

        # Якщо в кеші немає, йдемо в БД
        RetroTerminal.print_db(f"Виконання запиту до MongoDB...")
        data = data_fetcher_func()

        try:
            if data:
                # Зберігаємо в кеш на 1 годину (3600 секунд)
                redis_client.setex(key, 3600, json.dumps(data, ensure_ascii=False))
        except ConnectionError:
            pass

        return data

    @staticmethod
    def search_by_name(name: str) -> list:
        return SearchService._cache_result(
            f"name:{name}",
            lambda: QuoteRepository.get_quotes_by_author_name(name)
        )

    @staticmethod
    def search_by_tag(tag: str) -> list:
        return SearchService._cache_result(
            f"tag:{tag}",
            lambda: QuoteRepository.get_quotes_by_tag(tag)
        )

    @staticmethod
    def search_by_tags(tags_str: str) -> list:
        tags_list = tags_str.split(',')
        # Для списку тегів ключ кешу генеруємо сортуванням, щоб "life,live" == "live,life"
        cache_key = f"tags:{','.join(sorted(tags_list))}"
        return SearchService._cache_result(
            cache_key,
            lambda: QuoteRepository.get_quotes_by_tags(tags_list)
        )
