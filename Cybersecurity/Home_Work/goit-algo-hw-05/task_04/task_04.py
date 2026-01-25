"""
        ! Четверте завдання !

Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.

Вимоги до завдання:
1. Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо.
2. Декоратор input_error повинен обробляти винятки, що виникають у функціях — handler — і це винятки KeyError, ValueError, IndexError. Коли відбувається виняток декоратор повинен повертати відповідь користувачеві. Виконання програми при цьому не припиняється.

Рекомендації для виконання:
1. В якості прикладу додамо декоратор input_error для обробки помилки ValueError

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner

2. Та обгорнемо декоратором функцію add_contact нашого бота, щоб ми почали обробляти помилку ValueError.

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

3. Вам треба додати обробники до інших команд (функцій), та додати в декоратор обробку обробку винятків інших типів з відповідними повідомленнями.

Критерії оцінювання:
1. Наявність декоратора input_error, який обробляє помилки введення користувача для всіх команд.
2. Обробка помилок типу KeyError, ValueError, IndexError у функціях за допомогою декоратора input_error.
3. Кожна функція для обробки команд має власний декоратор input_error, який обробляє відповідні помилки і повертає відповідні повідомлення про помилку.
4. Коректна реакція бота на різні команди та обробка помилок введення без завершення програми.

Приклад використання:
При запуску скрипту діалог з ботом повинен бути схожим на цей.

Enter a command: add
Enter the argument for the command
Enter a command: add Bob
Enter the argument for the command
Enter a command: add Jime 0501234356
Contact added.
Enter a command: phone
Enter the argument for the command
Enter a command: all
Jime: 0501234356 
Enter a command:
"""

welcom_baner = """
 
 _____                _                 _    ______         _   
/  __ \              | |               | |   | ___ \       | |  
| /  \/  ___   _ __  | |_   __ _   ___ | |_  | |_/ /  ___  | |_ 
| |     / _ \ | '_ \ | __| / _` | / __|| __| | ___ \ / _ \ | __|
| \__/\| (_) || | | || |_ | (_| || (__ | |_  | |_/ /| (_) || |_ 
 \____/ \___/ |_| |_| \__| \__,_| \___| \__| \____/  \___/  \__|
                                                                
                                                                
"""
from functools import wraps

def input_error(func):
    """
    Створимо декоратор для обробки помилок введення користувача.
    Він обгорне функції-обробники команд (handlers) і перехопить можливі типові помилки,
    які можуть виникнути при роботі з даними (неправильні аргументи, відсутність даних тощо).
    """
    @wraps(func)  # @wraps зберігає ім'я та документацію оригінальної функції func
    def inner(*args, **kwargs):
        try:
            # Спроба виконати декоровану функцію (наприклад, add_contact)
            return func(*args, **kwargs)
        except ValueError:
            # Ця помилка виникає, коли не вдається розпакувати аргументи
            # Наприклад, очікується [ім'я, телефон], а отримано тільки [ім'я]
            return "Give me name and phone please."
        except KeyError:
            # Ця помилка виникає, коли ми звертаємось до ключа словника, якого не існує
            # Наприклад, спроба змінити номер контакту, якого немає в списку
            return "Contact not found."
        except IndexError:
            # Ця помилка виникає, коли ми звертаємось до індексу списку, якого не існує
            # Наприклад, команда 'phone' без аргументів (args[0] викличе помилку)
            return "Enter user name."
        except Exception as e:
            # Обробка будь-яких інших непередбачуваних помилок
            return f"Error: {e}"

    return inner

def parse_input(user_input: str):
    """
    Ця функція розбирає введений рядок на команду та список аргументів.
    Args:
        user_input (str): Рядок, введений користувачем. 
    Returns:
        tuple: Команда (str) у нижньому регістрі та список аргументів (list).
    """
    try:
        # Розбиваємо рядок по пробілах.
        # cmd - перше слово, *args - всі інші слова у вигляді списку.
        cmd, *args = user_input.split()
        
        # Приводимо команду до нижнього регістру та видаляємо зайві пробіли для стандартизації
        cmd = cmd.strip().lower()
        return cmd, args
    except ValueError:
        # Якщо введено порожній рядок або лише пробіли, split() не поверне нічого
        return "", []

@input_error
def add_contact(args: list, contacts: dict) -> str:
    """
    Ця функція додає новий контакт у словник.
    Очікує args = [name, phone].
    Якщо len(args) != 2, при розпакуванні виникне ValueError, який обробить декоратор.
    """
    name, phone = args  # Спроба розпакувати аргументи
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: list, contacts: dict) -> str:
    """
    Ця функція змінює номер телефону для існуючого контакту.
    Очікує args = [name, new_phone].
    Якщо контакт не знайдено, викликає KeyError вручну, щоб активувати декоратор.
    """
    name, phone = args
    if name not in contacts:
        raise KeyError  # Це перехопить декоратор і поверне "Contact not found."
    
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args: list, contacts: dict) -> str:
    """
    Ця функція показує номер телефону за іменем контакту.
    Очікує args = [name].
    Якщо список args порожній, args[0] викличе IndexError (обробить декоратор).
    """
    name = args[0]
    return contacts[name]  # Якщо ключа немає, виникне KeyError (обробить декоратор)

@input_error
def show_all(args: list, contacts: dict) -> str:
    """
    Ця функція виводить список всіх збережених контактів.
    Не приймає аргументи, але приймає 'args' для сумісності з іншими функціями.
    """
    if not contacts:
        return "No contacts saved."
    
    # Використаємо генератор списку та метод join для ефективного створення рядка.
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    """Це основна функція управління циклом бота."""
    contacts = {}  # Словник для зберігання даних у пам'яті під час роботи програми
    print(welcom_baner) # Банер - заставка на початку бота
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
            
        elif command == "add":
            print(add_contact(args, contacts))
            
        elif command == "change":
            print(change_contact(args, contacts))
            
        elif command == "phone":
            print(show_phone(args, contacts))
            
        elif command == "all":
            print(show_all(args, contacts))
            
        elif command == "":
            pass # Ігноруємо порожній ввід 
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
    
"""
Як писати бот:
https://www.youtube.com/watch?v=4cPq0cxFvK4

Як зробити заставку у бота на початку діалога
https://patorjk.com/software/taag/#p=display&f=Doom&t=Contact+Bot&x=none&v=0&h=0&w=90&we=true
"""
