from mongoengine import Document, StringField, ListField, ReferenceField
from models.author import Author

class Quote(Document):
    """
    Модель цитати.
    Використовує ReferenceField для зв'язку з колекцією authors.
    Індекс на поле 'tags' для швидкого пошуку за тегами.
    """
    tags = ListField(StringField())
    author = ReferenceField(Author, required=True, reverse_delete_rule=2) # CASCADE
    quote = StringField(required=True)

    meta = {
        'collection': 'quotes',
        'indexes': ['tags', 'author']
    }
