from models import Record
from utils import input_error


def hello():
    return (
        "Hello! 👋\n"
        "I am your Address Book bot.\n"
        "Type 'help' to see available commands."
    )


@input_error
def add_contact(args, book):
    *name_parts, phone = args
    name = " ".join(name_parts)

    record = book.find(name) or Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact saved."


@input_error
def change_contact(args, book):
    *name_parts, old_phone, new_phone = args
    name = " ".join(name_parts)

    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def delete_contact(args, book):
    name = " ".join(args)
    book.delete(name)
    return f"Contact '{name}' deleted."


@input_error
def show_phone(args, book):
    name = " ".join(args)
    record = book.find(name)
    return str(record)


@input_error
def show_all(_, book):
    return str(book) if book.data else "No contacts."


@input_error
def add_birthday(args, book):
    *name_parts, birthday = args
    name = " ".join(name_parts)

    record = book.find(name)
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def birthdays(_, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."

    return "\n".join(
        f"{item['name']}: {item['congratulation_date']}"
        for item in upcoming
    )


def clear_book(book):
    book.clear()
    return "All contacts removed."


def show_help():
    return """📘 ADDRESS BOOK BOT — HELP

Most used:
  add Ivan Petrov 0501234567
  phone Ivan Petrov
  all
  birthdays

Commands:
  hello
      - Greet the bot

  add [name] [phone]
      - Add contact or phone

  change [name] [old_phone] [new_phone]
      - Change phone number

  delete [name]
      - Delete contact

  phone [name]
      - Show contact phones

  add-birthday [name] [DD.MM.YYYY]
      - Add birthday

  birthdays
      - Upcoming birthdays

  clear
      - Remove all contacts

  help
      - Show this help

  exit / close
      - Exit the bot
"""
