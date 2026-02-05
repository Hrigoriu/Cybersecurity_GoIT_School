from models import Record
from utils import input_error

@input_error
def add_contact(args, book):
    if len(args) < 2:
        raise ValueError("Invalid command format. Use: add [name] [phone]")
    
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    
    if record is None:
        record = Record(name)
        book.add_record(record) # Логування спрацьовує всередині add_record у AddressBook
        message = "Contact added."
    else:
        # Якщо контакт існує, ми оновлюємо його
        book.log(f"Contact {name} updated (phone added/checked).")
        
    if phone:
        record.add_phone(phone)
        
    return message

@input_error
def change_contact(args, book):
    if len(args) < 3:
        raise ValueError("Invalid command format. Use: change [name] [old_phone] [new_phone]")
    
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    
    if record:
        record.edit_phone(old_phone, new_phone)
        # Додаємо явне логування події редагування
        book.log(f"Contact {name} has been edited (phone changed)!")
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(args, book):
    if len(args) < 1:
        raise IndexError
        
    name, *_ = args
    record = book.find(name)
    
    if record:
        return f"{name}: {'; '.join(p.value for p in record.phones)}"
    else:
        raise KeyError

@input_error
def show_all(args, book):
    if not book.data:
        return "No contacts saved."
    return str(book)

@input_error
def add_birthday(args, book):
    if len(args) < 2:
        raise ValueError("Invalid command format. Use: add-birthday [name] [DD.MM.YYYY]")
        
    name, birthday, *_ = args
    record = book.find(name)
    
    if record:
        record.add_birthday(birthday)
        # Логуємо додавання дати народження
        book.log(f"Birthday for {name} has been added/updated.")
        return "Birthday added."
    else:
        raise KeyError

@input_error
def show_birthday(args, book):
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
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    return "\n".join(f"{item['name']}: {item['congratulation_date']}" for item in upcoming)

def show_help():
    return """Available commands:
    hello                                     - Greet the bot
    add [name] [phone]                        - Add a new contact
    change [name] [old_phone] [new_phone]     - Change a phone number
    phone [name]                              - Show phone numbers
    all                                       - Show all contacts
    add-birthday [name] [date]                - Add a birthday
    show-birthday [name]                      - Show birthday
    birthdays                                 - Show upcoming birthdays
    help                                      - Show this help message
    close / exit                              - Exit the bot"""