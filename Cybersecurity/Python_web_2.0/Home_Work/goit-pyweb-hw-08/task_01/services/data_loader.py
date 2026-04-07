import json

from models.author import Author
from models.quote import Quote
from utils.logger import RetroTerminal


class DataLoaderService:
    """Сервіс для початкового завантаження даних з JSON у MongoDB."""

    @staticmethod
    def load_authors(filepath: str) -> None:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                authors_data = json.load(f)

            # 1. ГАРАНТІЯ: Очищаємо авторів перед новим завантаженням
            Author.drop_collection()

            for data in authors_data:
                fullname = data["fullname"].strip()
                Author(
                    fullname=fullname,
                    born_date=data.get("born_date"),
                    born_location=data.get("born_location"),
                    description=data.get("description")
                ).save()

            RetroTerminal.print_db("Авторів успішно завантажено.")
        except FileNotFoundError:
            RetroTerminal.print_error(f"Файл {filepath} не знайдено.")

    @staticmethod
    def load_quotes(filepath: str) -> None:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                quotes_data = json.load(f)

            # 1. ГАРАНТІЯ: Очищаємо цитати перед новим завантаженням
            Quote.drop_collection()

            # 2. ВИДАЛЕННЯ ДУБЛІКАТІВ У PYTHON
            unique_quotes = {}
            for data in quotes_data:
                clean_name = data["author"].strip()
                clean_quote = data["quote"].strip()

                # Створюємо унікальний ключ: "Ім'я автора + Текст цитати"
                key = f"{clean_name}:::{clean_quote}"

                # Словник перезапише дублікат, залишаючи лише 1 копію
                if key not in unique_quotes:
                    unique_quotes[key] = {
                        "author": clean_name,
                        "quote": clean_quote,
                        "tags": data.get("tags", [])
                    }

            # 3. Зберігаємо в базу ТІЛЬКИ унікальні відфільтровані цитати
            for item in unique_quotes.values():
                author = Author.objects(fullname=item["author"]).first()  # type: ignore
                if author:
                    Quote(
                        author=author,
                        quote=item["quote"],
                        tags=item["tags"]
                    ).save()

            RetroTerminal.print_db("Цитати успішно завантажено (100% БЕЗ дублікатів).")
        except FileNotFoundError:
            RetroTerminal.print_error(f"Файл {filepath} не знайдено.")
        except json.JSONDecodeError:
            RetroTerminal.print_error(f"Файл {filepath} містить некоректний JSON.")
