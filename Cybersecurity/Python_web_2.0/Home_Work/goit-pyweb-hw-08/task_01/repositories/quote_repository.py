from typing import List

from models.author import Author
from models.quote import Quote


class QuoteRepository:
    """Репозиторій для роботи з колекціями MongoDB."""

    @staticmethod
    def get_quotes_by_author_name(name_prefix: str) -> List[str]:
        """Шукає авторів за префіксом імені (regex) та повертає їхні цитати."""
        authors = Author.objects(fullname__iregex=f"^{name_prefix}") # type: ignore
        if not authors:
            return []

        quotes = Quote.objects(author__in=authors) # type: ignore

        # ГАРАНТІЯ: Видаляємо будь-які можливі дублікати перед віддачею (зберігаючи порядок)
        return list(dict.fromkeys([q.quote.strip() for q in quotes]))

    @staticmethod
    def get_quotes_by_tag(tag_prefix: str) -> List[str]:
        """Шукає цитати за префіксом тегу."""
        quotes = Quote.objects(tags__iregex=f"^{tag_prefix}") # type: ignore
        return list(dict.fromkeys([q.quote.strip() for q in quotes]))

    @staticmethod
    def get_quotes_by_tags(tags_list: List[str]) -> List[str]:
        """Шукає цитати за точним збігом хоча б одного тегу з переліку."""
        quotes = Quote.objects(tags__in=tags_list) # type: ignore
        return list(dict.fromkeys([q.quote.strip() for q in quotes]))
