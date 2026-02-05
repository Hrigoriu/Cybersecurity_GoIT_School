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
    show_help,
)
from utils import parse_input, WELCOME_BANNER


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
    "help": lambda *_: show_help(),
}

ALIASES = {
    "a": "add",
    "c": "change",
    "p": "phone",
    "h": "help",
    "q": "exit",
}


def main():
    book = AddressBook.load()
    print(WELCOME_BANNER)

    while True:
        command, args = parse_input(input("> "))
        command = ALIASES.get(command, command)

        if command in ("exit", "close"):
            book.save()
            print("Good bye!")
            break

        handler = COMMANDS.get(command)
        if handler:
            result = handler(args, book)
            print(result)

            if command in {"add", "change", "delete", "add-birthday", "clear"}:
                book.save()
        else:
            print("Unknown command. Type 'help'.")


if __name__ == "__main__":
    main()
