"""
В цьому домашньому завданні ви повинні додати функціонал збереження адресної книги на диск та відновлення з диска.

Для минулого домашнього завдання ви маєте вибрати pickle протокол серіалізації/десеріалізації даних та реалізувати методи, які дозволять зберегти всі дані у файл і завантажити їх із файлу.

Головна мета, щоб застосунок не втрачав дані після виходу із застосунку та при запуску відновлював їх з файлу. Повинна зберігатися адресна книга з якою ми працювали на попередньому сеансі.

Реалізуйте функціонал для збереження стану AddressBook у файл при закритті програми і відновлення стану при її запуску.

Приклади коду які стануть в нагоді.
# --- Приклад реалізації методів збереження та завантаження даних з використанням pickle ---

Серіалізація з pickle

import pickle

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено


Інтеграція збереження та завантаження в основний цикл

def main():
    book = load_data()

    # Основний цикл програми

    save_data(book)  # Викликати перед виходом з програми


Ці приклади допоможуть вам у реалізації домашнього завдання.

Критерії оцінювання:
1. Реалізовано протокол серіалізації/десеріалізації даних за допомогою pickle
2. Всі дані повинні зберігатися при виході з програми
3. При новому сеансі Адресна книга повинна бути у застосунку, яка була при попередньому запуску.
"""

import sys
import pickle
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
# ЧАСТИНА 1: Класи адресної книги (AddressBook System)
# ==============================================================================

class Field:
    """Створимо базовий клас для полів запису."""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """
    Створимо клас для зберігання імені контакту. 
    Обов'язкове поле.
    """
    pass


class Phone(Field):
    """
    Створимо клас для зберігання номера телефону.
    Включає валідацію формату (має бути 10 цифр).
    """
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Invalid phone number: must be 10 digits")
        super().__init__(value)

    @staticmethod
    def validate(phone_number):
        """Створимо функцію, яка перевіряє, чи складається рядок рівно з 10 цифр."""
        return len(phone_number) == 10 and phone_number.isdigit()


class Birthday(Field):
    """
    Створимо клас для зберігання дати народження.
    Формат: DD.MM.YYYY.
    """
    def __init__(self, value):
        try:
            # Перетворимо рядок у об'єкт date
            # Формат має бути сурово DD.MM.YYYY
            self.date = datetime.strptime(value, "%d.%m.%Y").date()
            # Збережемо оригінальне рядкове значення або відформатоване
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        # Повернемо дату у зручному форматі рядка
        return self.date.strftime("%d.%m.%Y")


class Record:
    """
    Створимо клас для зберігання інформації про контакт,
    включаючи ім'я, список телефонів та день народження.
    """
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        """Створимо функція, яка додає телефон до запису."""
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        """Створимо функцію, яка видаляє телефон із запису."""
        phone_to_remove = self.find_phone(phone_number)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)

    def edit_phone(self, old_phone, new_phone):
        """Створимо функцію, яка редагує телефон."""
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            # Валідація нового номеру відбудеться у конструкторі Phone
            self.phones = [Phone(new_phone) if p.value == old_phone else p for p in self.phones]
        else:
            raise ValueError("Phone number not found")

    def find_phone(self, phone_number):
        """Створимо функцію, яка шукає телефон за номером."""
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def add_birthday(self, birthday):
        """Створимо функцію, яка додає дату народження до запису."""
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones_str = '; '.join(p.value for p in self.phones)
        birthday_str = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones_str}{birthday_str}"


class AddressBook(UserDict):
    """
    Створимо клас для зберігання та управління записами.
    """
    
    def add_record(self, record):
        """Створимо функцію, яка додає запис до книги."""
        self.data[record.name.value] = record

    def find(self, name):
        """Створимо функцію, яка знаходить запис за ім'ям."""
        return self.data.get(name)

    def delete(self, name):
        """Створимо функцію, яка видаляє запис за ім'ям."""
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self, days=7):
        """
        Створимо функцію, яка повертає список користувачів, яких потрібно привітати протягом наступних 'days' днів.
        Враховуємо вихідні (переносимо на понеділок).
        """
        upcoming_birthdays = []
        today = datetime.today().date()

        for record in self.data.values():
            # Пропускаємо записи без дати народження
            if record.birthday is None:
                continue
            
            # Отримуємо дату народження цього року
            birthday_date = record.birthday.date
            birthday_this_year = birthday_date.replace(year=today.year)

            # Якщо день народження вже минув у цьому році, дивимось наступний рік
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            # Різниця в днях
            delta_days = (birthday_this_year - today).days

            # Перевіряємо, чи потрапляє дата у вікно 'days'
            if 0 <= delta_days <= days:
                # Логіка перенесення вихідних (субота 5, неділя 6)
                congratulation_date = birthday_this_year
                if congratulation_date.weekday() == 5: # Субота
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6: # Неділя
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
    """
    Створимо декоратор для обробки помилок введення.
    """
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
    """Створимо функцію, яка розбирає введений рядок на команду та аргументи."""
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args
    except ValueError:
        return "", []


@input_error
def add_contact(args, book: AddressBook):
    """Створимо функцію, яка додає новий контакт або оновлює телефон для існуючого."""
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
    """Створимо функцію, яка змінює телефон контакту."""
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
    """Створимо функцію, яка показує телефони контакту."""
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
    """Створимо функцію, яка показує всі контакти."""
    if not book.data:
        return "No contacts saved."
    return str(book)


@input_error
def add_birthday(args, book: AddressBook):
    """Створимо функцію, яка додає дату народження до контакту."""
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
    """Створимо функцію, яка показує дату народження контакту."""
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
    """Створимо функцію, яка показує іменинників на наступні 7 днів."""
    upcoming = book.get_upcoming_birthdays()
    
    if not upcoming:
        return "No upcoming birthdays."
    
    return "\n".join(f"{item['name']}: {item['congratulation_date']}" for item in upcoming)

def show_help():
    """Створимо функцію, яка повертає список доступних команд з поясненнями."""
    return """Available commands:
    hello                                     - Greet the bot
    add [name] [phone]                        - Add a new contact or update existing
    change [name] [old_phone] [new_phone]     - Change a phone number
    phone [name]                              - Show phone numbers for a contact
    all                                       - Show all contacts
    add-birthday [name] [date]                - Add a birthday (DD.MM.YYYY)
    show-birthday [name]                      - Show birthday for a contact
    birthdays                                 - Show upcoming birthdays
    help                                      - Show this help message
    close / exit                              - Exit the bot"""

# ==============================================================================
# ЧАСТИНА 3: Збереження та завантаження даних (Persistence Layer)
# ==============================================================================

def save_data(book, filename="addressbook.pkl"):
    """
    Створимо функцію, яка зберігає адресну книгу у файл за допомогою pickle.
    Файл зберігається у папку 'data'.
    """
    # Створюємо шлях до файлу: поточна папка / data / filename
    folder_path = Path("data")
    file_path = folder_path / filename
    
    # Створюємо папку data, якщо вона не існує
    folder_path.mkdir(exist_ok=True)
    
    with open(file_path, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    """
    Створимо функцію, яка завантажує адресну книгу з файлу.
    Якщо файл не знайдено, повертає нову AddressBook.
    """
    file_path = Path("data") / filename
    
    try:
        with open(file_path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        # Якщо це перший запуск і файлу немає - повертаємо нову книгу
        return AddressBook()

# ==============================================================================
# ЧАСТИНА 4: Головний цикл (Main Loop)
# ==============================================================================

def main():
    # Завантажуємо дані при запуску програми
    book = load_data()
    
    print(welcom_baner)
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command or write 'help' : ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            # Зберігаємо дані перед виходом
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