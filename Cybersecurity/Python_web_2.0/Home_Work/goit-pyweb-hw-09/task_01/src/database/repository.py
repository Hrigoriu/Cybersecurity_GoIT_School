from mongoengine import connect, disconnect
from src.database.models import Author, Quote
from src.config import Config
from src.logger import RetroLogger

class MongoRepository:
    """Паттерн Repository: інкапсулює логіку роботи з MongoDB."""

    @staticmethod
    def initialize():
        connect(host=Config.MONGODB_URI)
        RetroLogger.info("UPLINK ESTABLISHED: MongoDB Atlas Connected.")

    @staticmethod
    def close():
        disconnect()
        RetroLogger.info("UPLINK SEVERED: Database connection closed.")

    @staticmethod
    def upsert_author(author_data: dict) -> Author:
        """Створює або оновлює автора (щоб уникнути дублікатів)."""
        author = Author.objects(fullname=author_data['fullname']).first() # type: ignore
        if not author:
            author = Author(**author_data).save()
        return author

    @staticmethod
    def save_quote(quote_data: dict, author_obj: Author):
        """Зберігає цитату, перевіряючи на дублікати за текстом."""
        exists = Quote.objects(quote=quote_data['quote']).first() # type: ignore
        if not exists:
            Quote(
                tags=quote_data['tags'],
                author=author_obj,
                quote=quote_data['quote']
            ).save()
