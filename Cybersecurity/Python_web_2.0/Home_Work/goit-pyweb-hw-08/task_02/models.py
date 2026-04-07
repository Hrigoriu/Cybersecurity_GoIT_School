from mongoengine import Document, StringField, BooleanField, EmailField

class Contact(Document):
    """
    Модель контакту пацієнта/клієнта.

    Атрибути:
        full_name (str): Повне ім'я особи.
        email (str): Електронна адреса.
        phone (str): Телефонний номер.
        is_sent (bool): Логічне поле, чи було відправлено сповіщення.
        prefer_sms (bool): Метод зв'язку (True - SMS, False - Email).
        diagnosis_code (str): Додаткове інформаційне поле (наприклад, шифр за МКХ-10).
    """
    full_name = StringField(required=True, max_length=150)
    email = EmailField(required=True)
    phone = StringField(required=True, max_length=20)
    is_sent = BooleanField(default=False)
    prefer_sms = BooleanField(default=False)
    diagnosis_code = StringField(max_length=10)

    # Оптимізація БД: Індекси для швидкого пошуку невідправлених повідомлень
    # та фільтрації за пріоритетним каналом зв'язку.
    meta = {
        'collection': 'contacts',
        'indexes': [
            'is_sent',
            'prefer_sms'
        ]
    }
