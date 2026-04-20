import scrapy
from src.scraper.items import QuoteItem, AuthorItem
from src.logger import RetroLogger

class QuotesSpider(scrapy.Spider):
    """
    Павук, який проходить по всіх сторінках цитат та паралельно
    заходить на сторінки авторів для збору їхньої біографії.
    """
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        RetroLogger.info(f"SCANNING GRID: {response.url}")

        # Парсинг цитат на поточній сторінці
        for quote_block in response.css("div.quote"):
            quote_item = QuoteItem()
            quote_item["quote"] = quote_block.css("span.text::text").get().replace('“', '').replace('”', '')
            quote_item["author"] = quote_block.css("small.author::text").get()
            quote_item["tags"] = quote_block.css("div.tags a.tag::text").getall()
            yield quote_item

            # Витягуємо лінк на сторінку автора (наприклад, /author/Albert-Einstein)
            author_link = quote_block.css("span a::attr(href)").get()
            if author_link:
                yield response.follow(author_link, callback=self.parse_author)

        # Перехід на наступну сторінку
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_author(self, response):
        """Парсинг деталей автора."""
        author_item = AuthorItem()
        author_item["fullname"] = response.css("h3.author-title::text").get().strip()
        author_item["born_date"] = response.css("span.author-born-date::text").get().strip()
        author_item["born_location"] = response.css("span.author-born-location::text").get().strip()
        author_item["description"] = response.css("div.author-description::text").get().strip()
        yield author_item
