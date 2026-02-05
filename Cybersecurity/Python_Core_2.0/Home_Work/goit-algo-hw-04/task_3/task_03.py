"""
        !  Третє завдання (не обов'язкове) !

Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів. Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.

Вимоги до завдання:
1. Створіть віртуальне оточення Python для ізоляції залежностей проєкту.
2. Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
3. Використання бібліотеки colorama для реалізації кольорового виведення.
4. Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
5. Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.

Рекомендації для виконання:
1. Спочатку встановіть бібліотеку colorama. Для цього створіть та активуйте віртуальне оточення Python, а потім встановіть пакет за допомогою pip.
2. Використовуйте модуль sys для отримання шляху до директорії як аргументу командного рядка.
3. Для роботи з файловою системою використовуйте модуль pathlib.
4. Забезпечте належне форматування виводу, використовуючи функції colorama.

Критерії оцінювання:
1. Створення та використання віртуального оточення.
2. Правильність отримання та обробки шляху до директорії.
3. Точність виведення структури директорії.
4. Коректне застосування кольорового виведення за допомогою colorama.
5. Якість коду, включаючи читабельність, структурування та коментарі.

Приклад використання:
Якщо виконати скрипт та передати йому абсолютний шлях до директорії як параметр.
python hw03.py /шлях/до/вашої/директорії

Це призведе до виведення в терміналі списку всіх піддиректорій та файлів у вказаній директорії з використанням різних кольорів для піддиректорій та файлів, що полегшить візуальне сприйняття файлової структури.

Для директорії зі наступною структурою

📦picture
 ┣ 📂Logo
 ┃ ┣ 📜IBM+Logo.png
 ┃ ┣ 📜ibm.svg
 ┃ ┗ 📜logo-tm.png
 ┣ 📜bot-icon.png
 ┗ 📜mongodb.jpg

"""

import sys
from pathlib import Path
from colorama import init, Fore, Style


def display_tree(path: Path, indent: str="", is_last: bool=True):
    """
    Ця функція рекурсивно виводить дерево директорій.
    :param path: Шлях до поточного об'єкта (файл або папка).
    :param indent: Відступ для поточного рівня (рядок).
    :param is_last: Чи є цей елемент останнім у батьківському списку.
    """
    
    # Визначимо візуальні елементи залежно від того, чи це останній елемент
    connector = "┗━━ " if is_last else "┣━━ "
    
    # Визначаємо іконку та колір
    if path.is_dir():
        icon = "📂"
        color = Fore.BLUE + Style.BRIGHT
    else:
        icon = "📜"
        color = Fore.GREEN
    
    # Виведемо поточний елемент
    print(f"{indent}{connector}{icon} {color}{path.name}{Style.RESET_ALL}")
    pass


def print_directory_structure(directory: Path, prefix: str=""):
    """
    Ця функція проходить по директорії та друкує її вміст.
    """
    try:
        # Отримаємо список вмісту і посортуємо: спочатку папки, потім файли, все за алфавітом
        # lambda p: (p.is_file(), p.name.lower()) -> False (папка) < True (файл)
        items = sorted(directory.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    except PermissionError:
        print(f"{prefix}┗━━ {Fore.RED}Access Denied (Немає доступу){Style.RESET_ALL}")
        return
    except FileNotFoundError:
        print(f"{prefix}┗━━ {Fore.RED}Dir Not Found (Не знайдено){Style.RESET_ALL}")
        return

    count = len(items)
    for index, item in enumerate(items):
        is_last = (index == count - 1)
        connector = "┗━━ " if is_last else "┣━━ "
        
        if item.is_dir():
            print(f"{prefix}{connector}📂 {Fore.BLUE}{Style.BRIGHT}{item.name}{Style.RESET_ALL}")
            # Обчислимо префікс для підпапок цієї папки
            # Якщо ця папка остання в списку, то вертикальну лінію малювати не треба
            new_prefix = prefix + ("    " if is_last else "┃   ")
            print_directory_structure(item, new_prefix)
        else:
            print(f"{prefix}{connector}📜 {Fore.GREEN}{item.name}{Style.RESET_ALL}")


def main():
    # Це функція ініціалізації colorama (autoreset скидає колір після кожного print)
    init(autoreset=True)

    # Перевіримо аргументи
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Помилка: потрібно вказати шлях до директорії.")
        print(f"{Fore.YELLOW}Використання: python {sys.argv[0]} /шлях/до/папки")
        sys.exit(1)

    root_path = Path(sys.argv[1])

    if not root_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{root_path}' не існує.")
        sys.exit(1)
    
    if not root_path.is_dir():
        print(f"{Fore.RED}Помилка: '{root_path}' це файл, а потрібна директорія.")
        sys.exit(1)

    # Виведемо кореневу папку
    print(f"\n📦 {Fore.CYAN}{Style.BRIGHT}{root_path.resolve().name}{Style.RESET_ALL}")
    
    # Запуск рекурсії
    print_directory_structure(root_path)


if __name__ == "__main__":
    main()


"""
Алгоритм як запустити цей скрипт:
1. Створимо віртуальне оточення у директорії проєкту (task_3):
   python -m venv .venv  
2. Активуємо віртуальне оточення:
   - На Windows:    .venv\Scripts\activate     
3. Встановимо бібліотеку colorama:
   pip install colorama
4. Запустимо скрипт, передавши шлях до директорії:
   python task_03.py /шлях/до/вашої/директорії
   Мій варіант для Windows:
   python task_03.py "D:\IT school\Projects\Projects_GoIT\Cybersecurity\Home_Work\goit-algo-hw-04\task_3" 
5. Створимо файл requirements.txt для збереження залежностей:
   pip freeze > requirements.txt   
6. Деактивуємо віртуальне оточення після завершення роботи:
   deactivate     
"""
