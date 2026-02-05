from datetime import datetime
from utils import normalize_phone

class Field:
    """Базовий клас для полів запису."""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """Клас для зберігання імені контакту."""
    pass

class Phone(Field):
    """
    Клас для зберігання номера телефону.
    Автоматично нормалізує номер при ініціалізації.
    """
    def __init__(self, value):
        normalized_value = normalize_phone(value)
        if not self.validate(normalized_value):
            raise ValueError(f"Invalid phone number '{value}'. Expected format: +380XXXXXXXXX (12 digits)")
        super().__init__(normalized_value)

    @staticmethod
    def validate(phone_number):
        return len(phone_number) == 13 and phone_number.startswith('+380') and phone_number[1:].isdigit()

class Birthday(Field):
    """Клас для зберігання дати народження. Формат: DD.MM.YYYY."""
    def __init__(self, value):
        try:
            self.date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.date.strftime("%d.%m.%Y")

class Record:
    """Клас для зберігання інформації про контакт."""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        phone_to_remove = self.find_phone(phone_number)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)

    def edit_phone(self, old_phone, new_phone):
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            idx = self.phones.index(phone_obj)
            self.phones[idx] = Phone(new_phone)
        else:
            raise ValueError("Phone number not found")

    def find_phone(self, phone_number):
        target = normalize_phone(phone_number)
        for phone in self.phones:
            if phone.value == target:
                return phone
        return None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones_str = '; '.join(p.value for p in self.phones)
        birthday_str = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones_str}{birthday_str}"