import os
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# Додаємо корінь проекту до PYTHONPATH, щоб імпорти працювали коректно
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.scraper.spiders.quotes_spider import QuotesSpider
from src.logger import RetroLogger

def boot_sequence():
    """Ініціалізація та запуск краулера з Python-скрипта (Controller)."""
    RetroLogger.info("SYSTEM BOOT: Initializing Web Scraper Protocol...")
    RetroLogger.info("TARGET: http://quotes.toscrape.com")

    # Завантажуємо налаштування з src/scraper/settings.py
    os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'src.scraper.settings')
    settings = get_project_settings()

    # Запускаємо процес
    process = CrawlerProcess(settings)
    process.crawl(QuotesSpider)
    process.start()

if __name__ == "__main__":
    boot_sequence()
