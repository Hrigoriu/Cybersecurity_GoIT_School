from datetime import datetime
from utils import normalize_phone


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        value = normalize_phone(value)
        if not self.validate(value):
            raise ValueError("Invalid phone format: +380XXXXXXXXX")
        super().__init__(value)

    @staticmethod
    def validate(phone: str) -> bool:
        return phone.startswith("+380") and len(phone) == 13


class Birthday(Field):
    def __init__(self, value):
        try:
            self.date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        if not self.find_phone(phone):
            self.phones.append(Phone(phone))

    def edit_phone(self, old, new):
        phone = self.find_phone(old)
        if not phone:
            raise ValueError("Phone not found")
        self.phones[self.phones.index(phone)] = Phone(new)

    def find_phone(self, phone):
        phone = normalize_phone(phone)
        return next((p for p in self.phones if p.value == phone), None)

    def add_birthday(self, value):
        self.birthday = Birthday(value)

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        birthday = f", birthday: {self.birthday}" if self.birthday else ""
        return f"{self.name.value}: {phones}{birthday}"