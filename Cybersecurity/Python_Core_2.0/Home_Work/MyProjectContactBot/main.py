from address_book import AddressBook
from utils import parse_input, WELCOME_BANNER
# Імпортуємо функції-обробники команд
from handlers import (
    add_contact, 
    change_contact, 
    show_phone, 
    show_all, 
    add_birthday, 
    show_birthday, 
    birthdays, 
    show_help
)

def main():
    """
    Головна функція програми.
    Відповідає за ініціалізацію, цикл запит-відповідь та збереження даних.
    """
    # 1. Завантажуємо дані при запуску (використовуємо статичний метод класу)
    book = AddressBook.load_data()
    
    print(WELCOME_BANNER)
    print("Welcome to the assistant bot!")
    print("Type 'help' to see available commands.")
    
    while True:
        # Отримуємо введення від користувача
        user_input = input("Enter a command: ")
        
        # Парсимо команду та аргументи
        command, args = parse_input(user_input)

        # Маршрутизація команд (Command Routing)
        if command in ["close", "exit"]:
            # 2. Зберігаємо дані перед виходом
            AddressBook.save_data(book)
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
            pass # Ігноруємо порожній ввід (просто новий рядок)

        else:
            print("Invalid command. Type 'help' to see valid commands.")

if __name__ == "__main__":
    main()