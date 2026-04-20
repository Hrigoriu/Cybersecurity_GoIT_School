from mongoengine import Document, StringField, ListField, ReferenceField, CASCADE

class Author(Document):
    """Модель автора для MongoDB."""
    fullname = StringField(required=True, unique=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=150)
    description = StringField()

    meta = {
        'collection': 'authors',
        'indexes': ['fullname']  # Індекс для швидкого пошуку при зв'язуванні
    }

class Quote(Document):
    """Модель цитати. Зв'язана з Автором через ReferenceField."""
    tags = ListField(StringField(max_length=50))
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField(required=True)

    meta = {
        'collection': 'quotes',
        'indexes': ['tags', 'author'] # Індекси для пошуку за тегами та авторами
    }
