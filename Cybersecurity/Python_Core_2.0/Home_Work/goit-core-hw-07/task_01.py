"""
Продовжимо робити консольного бота помічника. 
Настав час об'єднати наші попередні домашні завдання в одне.

    A. Додамо додатковий функціонал до класів з попередньої домашньої роботи:
1. Додайте поле birthday для дня народження в клас Record . Це поле має бути класу Birthday. 
Це поле не обов'язкове, але може бути тільки одне.

class Birthday(Field):
    def __init__(self, value):
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

2. Додайте функціонал роботи з Birthday у клас Record, а саме функцію add_birthday, яка додає дату народження до контакту.
3. Додайте функціонал перевірки значення в класі Birthday.
4. Додайте та адаптуйте до класу AddressBook фінальну функцію з автоперевірки, (тиждень 3), get_upcoming_birthdays . 
Це буде метод, який визначає контакти, у яких день народження припадає вперед на 7 днів включаючи поточний день. Метод має повертати список словників. 
Кожен словник містить два значення - ім’я з ключем "name", та дата привітання з ключем "birthday”. 
Не забудьте врахувати перенесення дати на наступний робочий день, якщо день народження припадає на вихідний.

    B. Тепер ваш бот (4 домашнє завдання тиждень 5) повинен працювати саме з функціоналом класу AddressBook. 
Це значить, що замість словника contacts ми використовуємо book = AddressBook()

    C. Для реалізації нового функціоналу також додайте функції обробники з наступними командами:
add-birthday - додаємо до контакту день народження в форматі DD.MM.YYYY
show-birthday - показуємо день народження контакту
birthdays - повертає список користувачів, яких потрібно привітати по днях на наступному тижні

@input_error
def add_birthday(args, book):
    # реалізація

@input_error
def show_birthday(args, book):
    # реалізація

@input_error
def birthdays(args, book):
    # реалізація

    D. Тож в фіналі наш бот повинен підтримувати наступний список команд:
add [ім'я] [телефон]: Додати або новий контакт з іменем та телефонним номером, або телефонний номер до контакту який вже існує.
change [ім'я] [старий телефон] [новий телефон]: Змінити телефонний номер для вказаного контакту.
phone [ім'я]: Показати телефонні номери для вказаного контакту.
all: Показати всі контакти в адресній книзі.
add-birthday [ім'я] [дата народження]: Додати дату народження для вказаного контакту.
show-birthday [ім'я]: Показати дату народження для вказаного контакту.
birthdays: Показати дні народження на найближчі 7 днів з датами, коли їх треба привітати.
hello: Отримати вітання від бота.
close або exit: Закрити програму.

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            # реалізація

        elif command == "change":
            # реалізація

        elif command == "phone":
            # реалізація

        elif command == "all":
            # реалізація

        elif command == "add-birthday":
            # реалізація

        elif command == "show-birthday":
            # реалізація

        elif command == "birthdays":
            # реалізація

        else:
            print("Invalid command.")

    E. 📌Для прикладу розглянемо реалізацію команди add [ім'я] [телефон]. 
В функції main ми повинні додати обробку цієї команди, в відповідне місце:

         elif command == "add":
            print(add_contact(args, book))


    F. Сама реалізація функції add_contact може виглядати наступним чином:
    
@input_error
def add_contact(args, book: AddressBook):
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


    G. Наша функція add_contact має два призначення - додавання нового контакту або оновлення телефону для контакту, що вже існує в адресній книзі. 
Параметри функції це список аргументів args та сама адресна книга book.

Спочатку функція розпаковує список args, отримуючи ім'я name і телефон phone з перших двох елементів списку. 
Решта аргументів ігнорується завдяки використанню *_. 
Далі метод find об'єкта book виконує пошук запису з іменем name. Якщо запис з таким іменем існує, метод повертає цей запис, інакше повертається None. 
Якщо запис не знайдено, то це новий контакт і функція створює новий об'єкт Record з іменем name і додає його до book викликом методу add_record. 
Після додавання нового запису змінній message присвоюється повідомлення "Contact added." успішності операції. 
Далі незалежно від того, чи був запис знайдений або створений новий, до цього запису додається телефонний номер за допомогою методу add_phone, якщо він був наданий. 
На завершення функція повертає повідомлення про результат своєї роботи: "Contact updated.", якщо контакт був оновлений, або "Contact added.", якщо контакт був доданий. 
Для перехоплення помилок вводу та виведення відповідного повідомлення про помилку використовуємо декоратор @input_error.

Критерії оцінювання:
1. Реалізовані всі вказані команди до бота.
2. Використані ті класи, що були написані в 6 дз.
3. Доданий клас Birthday, який наслідується від класу Field. Значення зберігається в полі value. Тип - рядок формата DD.MM.YYYY.
4. Доданий метод add_birthday в клас Record.
5. Доданий метод get_upcoming_birthdays в клас AddressBook.
6. Всі дані повинні виводитися у зрозумілому та зручному для користувача форматі.
7. Всі помилки, такі як неправильний ввід чи відсутність контакту, повинні оброблятися інформативно з відповідним повідомленням для користувача за допомогою декоратора input_error.
8. Валідація даних:
Дата народження має бути у форматі DD.MM.YYYY.
Телефонний номер має складатися з 10 цифр.
9. Обробка всіх команд має відбуватись в окремих функція-хендлерах.
10. Програма повинна закриватися коректно після виконання команд close або exit
"""

import sys
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
            # Обробка помилок валідації (дати, телефону, кількості аргументів)
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
    """
    Створимо функцію, яка додає новий контакт або оновлює телефон для існуючого.
    Формат: add [name] [phone]
    """
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
    """
    Створимо функцію, яка змінює телефон контакту.
    Формат: change [name] [old_phone] [new_phone]
    """
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
    """
    Створимо функцію, яка показує телефони контакту.
    Формат: phone [name]
    """
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
    """
    Створимо функцію, яка додає дату народження до контакту.
    Формат: add-birthday [name] [DD.MM.YYYY]
    """
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
    """
    Створимо функцію, яка показує дату народження контакту.
    Формат: show-birthday [name]
    """
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
    """
    Створимо функцію, яка показує іменинників на наступні 7 днів.
    Формат: birthdays
    """
    upcoming = book.get_upcoming_birthdays()
    
    if not upcoming:
        return "No upcoming birthdays."
    
    return "\n".join(f"{item['name']}: {item['congratulation_date']}" for item in upcoming)

def show_help():
    """Повертає список доступних команд з поясненнями."""
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
# ЧАСТИНА 3: Головний цикл (Main Loop)
# ==============================================================================

def main():
    # Ініціалізація адресної книги
    book = AddressBook()
    
    print(welcom_baner)
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command or write 'help' : ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
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