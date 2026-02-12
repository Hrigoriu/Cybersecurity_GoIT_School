from models import Record
from utils import input_error


def hello():
    return "Привіт! 👋 Я твій бот-асистент."


@input_error
def add_contact(args, book):
    *name_parts, phone = args
    name = " ".join(name_parts)

    record = book.find(name) or Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Контакт збережено."


@input_error
def change_contact(args, book):
    *name_parts, old_phone, new_phone = args
    name = " ".join(name_parts)

    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    return "Контакт оновлено."


@input_error
def delete_contact(args, book):
    name = " ".join(args)
    book.delete(name)
    return f"Контакт '{name}' видалено."


@input_error
def show_phone(args, book):
    name = " ".join(args)
    record = book.find(name)
    return str(record)


@input_error
def show_all(_, book):
    # Повертаємо список записів, а не рядок
    return list(book.data.values())


@input_error
def add_birthday(args, book):
    *name_parts, birthday = args
    name = " ".join(name_parts)

    record = book.find(name)
    record.add_birthday(birthday)
    return "День народження додано."


@input_error
def birthdays(_, book):
    # Повертаємо список словників
    return book.get_upcoming_birthdays()


def clear_book(book):
    book.clear()
    return "Всі контакти видалено."


def get_help_data():
    # Повертаємо словник команд для відображення
    return {
        "hello": "Привітатися з ботом",
        "add": "Додати контакт (add Ім'я Телефон)",
        "change": "Змінити номер (change Ім'я Старий Новий)",
        "phone": "Показати номер (phone Ім'я)",
        "all": "Показати всі контакти",
        "add-birthday": "Додати ДН (add-birthday Ім'я DD.MM.YYYY)",
        "birthdays": "Показати іменинників на тиждень",
        "delete": "Видалити контакт",
        "clear": "Очистити книгу",
        "exit/close": "Вихід",
        "help": "Показати це меню"
    }