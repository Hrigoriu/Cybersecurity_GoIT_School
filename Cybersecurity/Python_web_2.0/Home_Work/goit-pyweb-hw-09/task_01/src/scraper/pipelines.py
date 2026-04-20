from src.scraper.items import QuoteItem, AuthorItem
from src.services.data_service import DataService
from src.logger import RetroLogger

class RetroPipeline:
    """
    Pipeline, який збирає всі Items у пам'яті під час роботи Spider,
    а після завершення передає їх у Service для пакетного збереження.
    Це уникає блокування асинхронного циклу Scrapy повільними запитами до БД.
    """
    def __init__(self):
        self.quotes = []
        self.authors = []
        self.seen_authors = set() # Запобігає дублюванню авторів в JSON

    def process_item(self, item, spider):
        if isinstance(item, QuoteItem):
            self.quotes.append(dict(item))
            RetroLogger.process(f"EXTRACTED QUOTE: {item['author'][:20]}...")

        elif isinstance(item, AuthorItem):
            if item['fullname'] not in self.seen_authors:
                self.authors.append(dict(item))
                self.seen_authors.add(item['fullname'])
                RetroLogger.process(f"EXTRACTED AUTHOR: {item['fullname']}")
        return item

    def close_spider(self, spider):
        """Викликається, коли павук закінчив сканування всіх сторінок."""
        RetroLogger.info("SPIDER TERMINATED. Initiating data compilation...")
        service = DataService()
        service.process_and_save_data(self.authors, self.quotes)
