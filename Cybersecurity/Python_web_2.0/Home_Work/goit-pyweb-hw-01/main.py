from address_book import AddressBook
from handlers import (
    hello,
    add_contact,
    change_contact,
    delete_contact,
    show_phone,
    show_all,
    add_birthday,
    birthdays,
    clear_book,
    get_help_data,
)
from utils import parse_input, welcom_big_baner, WELCOME_BANNER
from views import ConsoleView  # Імпортуємо наш View


COMMANDS = {
    "hello": lambda *_: hello(),
    "add": add_contact,
    "change": change_contact,
    "delete": delete_contact,
    "phone": show_phone,
    "all": show_all,
    "add-birthday": add_birthday,
    "birthdays": birthdays,
    "clear": lambda _, book: clear_book(book),
    "help": lambda *_: get_help_data(),
}

ALIASES = {
    "a": "add",
    "c": "change",
    "p": "phone",
    "h": "help",
    "q": "exit",
}



def main():
    # 1. Ініціалізація компонентів
    book = AddressBook.load()
    view = ConsoleView()  # Тут можна легко підмінити на Webview()
    view.display_message(welcom_big_baner)
    view.display_message(WELCOME_BANNER)

    # 2. Головний цикл
    while True:
        user_input = input('Пиши тут, або "help" >: ')
        command, args = parse_input(user_input)
        command = ALIASES.get(command, command)

        if command in ("exit", "close"):
            book.save()
            view.display_message("До побачення! Ваші дані збережено.")
            break

        handler = COMMANDS.get(command)
        if handler:
            # Отримуємо результат від бізнес-логіки
            result = handler(args, book)

            # Вибираємо метод відображення залежно від команди
            if command == "all":
                view.display_contacts(result)
            elif command == "birthdays":
                view.display_birthdays(result)
            elif command == "help":
                view.display_help(result)
            else:
                # Для простих повідомлень (успіх/помилка)
                view.display_message(str(result))

            # Автозбереження після змін
            if command in {"add", "change", "delete", "add-birthday", "clear"}:
                book.save()
        else:
            view.display_message("Невідома команда. Введіть 'help'.")


if __name__ == "__main__":
    main()