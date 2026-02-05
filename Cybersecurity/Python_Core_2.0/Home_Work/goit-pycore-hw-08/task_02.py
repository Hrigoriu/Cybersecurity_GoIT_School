"""
Це зміненний код в завданні goit-pycore-hw-08 з домашньої роботи GoIT Python Core 2.0.
Він включає нормалізацію телефонних номерів у класі Phone.
"""
import sys
import pickle
import re
from pathlib import Path
from collections import UserDict
from datetime import datetime, timedelta
from functools import wraps

welcom_baner = """
 
 _____                _                 _    ______         _   
/  __ \              | |               | |   | ___ \       | |  
| /  \/  ___   _ __  | |_   __ _   ___ | |_  | |_/ /  ___  | |_ 
| |     / _ \ | '_ \ | __| / _` | / __|| __| | ___ \ / _ \ | __|
| \__/\| (_) || | | || |_ | (_| || (__ | |_  | |_/ /| (_) || |_ 
 \____/ \___/ |_| |_| \__| \__,_| \___| \__| \____/  \___/  \__|
                                                                
                                                                
"""

# ==============================================================================
# ЧАСТИНА 0: Допоміжні функції (Utils)
# ==============================================================================

def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує телефонні номери до стандартного формату +380XXXXXXXXX.
    Функція взята з task_03.py.
    """
    # 1. Проведемо санітарну очистку (Sanitization)
    # Використовуємо регулярний вираз \D (все, що НЕ є цифрою).
    sanitized_number = re.sub(r'\D', '', phone_number)
    
    # 2. Проведемо форматування (Normalization)
    # Випадок А: Номер вже має міжнародний код 380
    if sanitized_number.startswith("380"):
        return f"+{sanitized_number}"
    
    # Випадок Б: Номер не має коду (додаємо +38)
    else:
        return f"+38{sanitized_number}"

# ==============================================================================
# ЧАСТИНА 1: Класи адресної книги (AddressBook System)
# ==============================================================================

class Field:
    """Створимо базовий клас для полів запису."""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Створимо клас для зберігання імені контакту."""
    pass


class Phone(Field):
    """
    Створимо клас для зберігання номера телефону.
    Автоматично нормалізує номер та перевіряє його валідність.
    """
    def __init__(self, value):
        # Спочатку нормалізуємо номер (наприклад, 0671234567 -> +380671234567)
        normalized_value = normalize_phone(value)
        
        # Перевіряємо вже нормалізований номер
        if not self.validate(normalized_value):
            # Якщо після нормалізації номер не має правильної довжини
            raise ValueError(f"Invalid phone number '{value}'. Expected format: +380XXXXXXXXX (12 digits)")
            
        # Зберігаємо нормалізоване значення
        super().__init__(normalized_value)

    @staticmethod
    def validate(phone_number):
        """
        Перевіряє, чи відповідає номер формату +380XXXXXXXXX (13 символів).
        """
        return len(phone_number) == 13 and phone_number.startswith('+380') and phone_number[1:].isdigit()


class Birthday(Field):
    """Створимо клас для зберігання дати народження. Формат: DD.MM.YYYY."""
    def __init__(self, value):
        try:
            self.date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.date.strftime("%d.%m.%Y")


class Record:
    """Створимо клас для зберігання інформації про контакт."""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        """Додає телефон до запису."""
        # Клас Phone автоматично нормалізує номер при створенні
        # Якщо номер некоректний, Phone викине ValueError, який спіймає декоратор
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        """Видаляє телефон із запису."""
        phone_to_remove = self.find_phone(phone_number)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)

    def edit_phone(self, old_phone, new_phone):
        """Редагує телефон."""
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            # Створюємо новий об'єкт Phone (він пройде валідацію та нормалізацію)
            new_phone_obj = Phone(new_phone)
            # Оновлюємо значення в існуючому об'єкті або замінюємо його
            # Тут краще замінити об'єкт у списку, щоб зберегти цілісність
            idx = self.phones.index(phone_obj)
            self.phones[idx] = new_phone_obj
        else:
            raise ValueError("Phone number not found")

    def find_phone(self, phone_number):
        """
        Шукає телефон за номером.
        Нормалізує вхідний номер перед пошуком, щоб знайти +380... навіть якщо ввели 0...
        """
        target = normalize_phone(phone_number)
        for phone in self.phones:
            if phone.value == target:
                return phone
        return None

    def add_birthday(self, birthday):
        """Додає дату народження."""
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones_str = '; '.join(p.value for p in self.phones)
        birthday_str = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones_str}{birthday_str}"


class AddressBook(UserDict):
    """Створимо клас для зберігання та управління записами."""
    
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = datetime.today().date()

        for record in self.data.values():
            if record.birthday is None:
                continue
            
            birthday_date = record.birthday.date
            birthday_this_year = birthday_date.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days

            if 0 <= delta_days <= days:
                congratulation_date = birthday_this_year
                if congratulation_date.weekday() == 5: 
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6: 
                    congratulation_date += timedelta(days=1)

                upcoming_birthdays.append({
                    "name": record.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                })

        return upcoming_birthdays

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


# ==============================================================================
# ЧАСТИНА 2: Логіка бота (Bot Logic)
# ==============================================================================

def input_error(func):
    """Декоратор для обробки помилок."""
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return inner


def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args
    except ValueError:
        return "", []


@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Invalid command format. Use: add [name] [phone]")
    
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
        
    if phone:
        record.add_phone(phone)
        
    return message


@input_error
def change_contact(args, book: AddressBook):
    if len(args) < 3:
        raise ValueError("Invalid command format. Use: change [name] [old_phone] [new_phone]")
    
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Contact updated."
    else:
        raise KeyError


@input_error
def show_phone(args, book: AddressBook):
    if len(args) < 1:
        raise IndexError
        
    name, *_ = args
    record = book.find(name)
    
    if record:
        return f"{name}: {'; '.join(p.value for p in record.phones)}"
    else:
        raise KeyError


@input_error
def show_all(args, book: AddressBook):
    if not book.data:
        return "No contacts saved."
    return str(book)


@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Invalid command format. Use: add-birthday [name] [DD.MM.YYYY]")
        
    name, birthday, *_ = args
    record = book.find(name)
    
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        raise KeyError


@input_error
def show_birthday(args, book: AddressBook):
    if len(args) < 1:
        raise IndexError
        
    name, *_ = args
    record = book.find(name)
    
    if record:
        if record.birthday:
            return f"{name}'s birthday: {record.birthday}"
        else:
            return f"{name} has no birthday set."
    else:
        raise KeyError


@input_error
def birthdays(args, book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    return "\n".join(f"{item['name']}: {item['congratulation_date']}" for item in upcoming)

def show_help():
    return """Available commands:
    hello                                     - Greet the bot
    add [name] [phone]                        - Add a new contact (e.g. 0671234567)
    change [name] [old_phone] [new_phone]     - Change a phone number
    phone [name]                              - Show phone numbers for a contact
    all                                       - Show all contacts
    add-birthday [name] [date]                - Add a birthday (DD.MM.YYYY)
    show-birthday [name]                      - Show birthday for a contact
    birthdays                                 - Show upcoming birthdays
    help                                      - Show this help message
    close / exit                              - Exit the bot"""

# ==============================================================================
# ЧАСТИНА 3: Збереження та завантаження даних
# ==============================================================================

def save_data(book, filename="addressbook.pkl"):
    folder_path = Path("data")
    file_path = folder_path / filename
    folder_path.mkdir(exist_ok=True)
    with open(file_path, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    file_path = Path("data") / filename
    try:
        with open(file_path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

# ==============================================================================
# ЧАСТИНА 4: Головний цикл
# ==============================================================================

def main():
    book = load_data()
    print(welcom_baner)
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command or write 'help': ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(args, book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        elif command == "help":
            print(show_help())

        elif command == "":
            pass

        else:
            print("Invalid command. Type 'help' to see valid commands.")

if __name__ == "__main__":
    main()