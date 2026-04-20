# Налаштування Scrapy для забезпечення стилю та ефективності
BOT_NAME = "retro_scraper"
SPIDER_MODULES = ["src.scraper.spiders"]
NEWSPIDER_MODULE = "src.scraper.spiders"

# Підключаємо наш кастомний Pipeline
ITEM_PIPELINES = {
    "src.scraper.pipelines.RetroPipeline": 300,
}

# Робимо Scrapy тихим, щоб бачити лише наш RetroLogger
LOG_LEVEL = 'WARNING'
ROBOTSTXT_OBEY = True
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
