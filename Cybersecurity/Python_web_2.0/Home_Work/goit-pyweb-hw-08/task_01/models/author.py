from mongoengine import Document, StringField


class Author(Document):
    """
    Модель автора.
    Індекс на поле 'fullname' для швидкого пошуку за ім'ям.
    """

    fullname = StringField(required=True, unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

    meta = {"collection": "authors", "indexes": ["fullname"]}
