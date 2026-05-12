# quotes/services.py
import requests
from bs4 import BeautifulSoup
from django.db import transaction

from .models import Author, Quote, Tag


class ScraperService:
    """Сервіс для повного імпорту даних з сайту, включаючи деталі авторів."""

    BASE_URL = "http://quotes.toscrape.com"

    @classmethod
    def scrape_and_save(cls, user=None):
        url = cls.BASE_URL
        count_quotes = 0
        # Кеш, щоб не робити зайві запити для авторів, яких ми вже обробили в цьому циклі
        scraped_authors_cache = set()

        try:
            with transaction.atomic():
                while url:
                    response = requests.get(url)
                    if response.status_code != 200:
                        raise Exception(f"Помилка з'єднання: {url}")

                    soup = BeautifulSoup(response.text, "html.parser")
                    quotes_blocks = soup.find_all("div", class_="quote")

                    for block in quotes_blocks:
                        # 1. Парсинг базових даних цитати
                        text = (
                            block.find("span", class_="text")
                            .get_text(strip=True)
                            .strip("“”")
                        )
                        author_name = block.find("small", class_="author").get_text(
                            strip=True
                        )
                        tags = [
                            tag.get_text(strip=True)
                            for tag in block.find_all("a", class_="tag")
                        ]

                        # 2. Отримання або створення автора (базовий запис)
                        author, created_author = Author.objects.get_or_create(
                            fullname=author_name, defaults={"added_by": user}
                        )

                        # 3. ДОДАТКОВИЙ КРОК: Збір деталей про автора
                        # Шукаємо лінк на сторінку автора
                        author_about_link = block.find("a", string="(about)")

                        # Робимо запит ТІЛЬКИ якщо ми ще не парсили його в цій сесії
                        # АБО якщо в БД ще немає його опису (description)
                        if (
                            author_about_link
                            and (author_name not in scraped_authors_cache)
                            and not author.description
                        ):
                            author_url = cls.BASE_URL + author_about_link["href"]
                            author_res = requests.get(author_url)

                            if author_res.status_code == 200:
                                a_soup = BeautifulSoup(author_res.text, "html.parser")

                                # Оновлюємо дані автора
                                author.born_date = a_soup.find(
                                    "span", class_="author-born-date"
                                ).get_text(strip=True)
                                author.born_location = a_soup.find(
                                    "span", class_="author-born-location"
                                ).get_text(strip=True)
                                author.description = a_soup.find(
                                    "div", class_="author-description"
                                ).get_text(strip=True)
                                author.save()

                            # Запам'ятовуємо, що ми його вже перевірили
                            scraped_authors_cache.add(author_name)

                        # 4. Створення самої цитати
                        quote, created_quote = Quote.objects.get_or_create(
                            text=text, author=author, defaults={"added_by": user}
                        )

                        if created_quote:
                            count_quotes += 1
                            for tag_name in tags:
                                tag_obj, _ = Tag.objects.get_or_create(name=tag_name)
                                quote.tags.add(tag_obj)

                    # Перехід на наступну сторінку пагінації Quotes to Scrape
                    next_btn = soup.select_one("li.next a")
                    url = cls.BASE_URL + next_btn["href"] if next_btn else None

            return (
                True,
                f"Успішно імпортовано {count_quotes} нових цитат та оновлено біографії авторів.",
            )

        except Exception as e:
            return False, f"Сталася помилка під час скрапінгу: {str(e)}"
        except Exception as e:
            return False, f"Сталася помилка під час скрапінгу: {str(e)}"
