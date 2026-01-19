"""
        Третє завдання (не обов'язкове)

Розробіть Python-скрипт для аналізу файлів логів. 
1. Скрипт повинен вміти читати лог-файл, переданий як аргумент командного рядка, і виводити статистику за рівнями логування наприклад, INFO, ERROR, DEBUG. 
2. Також користувач може вказати рівень логування як другий аргумент командного рядка, щоб отримати всі записи цього рівня.

Файли логів – це файли, що містять записи про події, які відбулися в операційній системі, програмному забезпеченні або інших системах. Вони допомагають відстежувати та аналізувати поведінку системи, виявляти та діагностувати проблеми.

Для виконання завдання візьміть наступний приклад лог-файлу:
2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance.

Вимоги до завдання:
1. Скрипт повинен приймати шлях до файлу логів як аргумент командного рядка.
2. Скрипт повинен приймати не обов'язковий аргумент командного рядка, після аргументу шляху до файлу логів. Він відповідає за виведення всіх записи певного рівня логування. І приймає значення відповідно до рівня логування файлу. Наприклад аргумент error виведе всі записи рівня ERROR з файлу логів.
3. Скрипт має зчитувати і аналізувати лог-файл, підраховуючи кількість записів для кожного рівня логування (INFO, ERROR, DEBUG, WARNING).
4.Реалізуйте функцію parse_log_line(line: str) -> dict для парсингу рядків логу.
5. Реалізуйте функцію load_logs(file_path: str) -> list для завантаження логів з файлу.
6. Реалізуйте функцію filter_logs_by_level(logs: list, level: str) -> list для фільтрації логів за рівнем.
7. Реалізуйте функцію count_logs_by_level(logs: list) -> dict для підрахунку записів за рівнем логування.
8. Результати мають бути представлені у вигляді таблиці з кількістю записів для кожного рівня. Для цього реалізуйте функцію display_log_counts(counts: dict), яка форматує та виводить результати. Вона приймає результати виконання функції count_logs_by_level.

Рекомендації для виконання:
1. Перш ніж почати, ознайомтеся зі структурою вашого лог-файлу. Зверніть увагу на формат дати та часу, рівні логування INFO, ERROR, DEBUG, WARNING і структуру повідомлень.
2. Зрозумійте, як розділені різні компоненти логу, це зазвичай пробіли або спеціальні символи.
3. Розділіть ваше завдання на логічні блоки і функції для кращої читабельності і подальшого розширення.
4. Парсинг рядка логу виконує функцію parse_log_line(line: str) -> dict, яка приймає рядок з логу як вхідний параметр і повертає словник з розібраними компонентами: дата, час, рівень, повідомлення. 
5. Використовуйте методи рядків, такі як split(), для розділення рядка на частини.
6. Завантаження лог-файлів виконує функція load_logs(file_path: str) -> list, що відкриває файл, читає кожен рядок і застосовує до нього функцію parse_log_line, зберігаючи результати в список.
7. Фільтрацію за рівнем логування виконує функція filter_logs_by_level(logs: list, level: str) -> list. Вона дозволить вам отримати всі записи логу для певного рівня логування.
8. Підрахунок записів за рівнем логування повинна робити функція count_logs_by_level(logs: list) -> dict, яка проходить по всім записам і підраховує кількість записів для кожного рівня логування.
9. Виведення результатів виконайте за допомоги функції display_log_counts(counts: dict), яка форматує та виводить результати підрахунку в читабельній формі.
10. Ваш скрипт повинен вміти обробляти різні види помилок, такі як відсутність файлу або помилки при його читанні. Використовуйте блоки try/except для обробки виняткових ситуацій.

Критерії оцінювання:
1. Скрипт виконує всі зазначені вимоги, правильно аналізуючи лог-файли та виводячи інформацію.
2. Скрипт коректно обробляє помилки, такі як неправильний формат лог-файлу або відсутність файлу.
3. При розробці обов'язково було використано один з елементів функціонального програмування: лямбда-функція, списковий вираз, функція filter, тощо.
4. Код добре структурований, зрозумілий і містить коментарі там, де це необхідно.

Приклад використання:

При запуску скрипту: 
        python [main.py](<http://main.py/>) /path/to/logfile.log

ми повинні очікувати таке виведення:
Рівень логування | Кількість
-----------------|----------
INFO             | 4
DEBUG            | 3
ERROR            | 2
WARNING          | 1

Якщо користувач хоче переглянути всі записи певного рівня логування, він може запустити скрипт з додатковим аргументом, наприклад: 
        python main.py path/to/logfile.log error

Це виведе загальну статистику за рівнями, а також детальну інформацію для всіх записів з рівнем ERROR.

Рівень логування | Кількість
-----------------|----------
INFO             | 4
DEBUG            | 3
ERROR            | 2
WARNING          | 1

Деталі логів для рівня 'ERROR':
2024-01-22 09:00:45 - Database connection failed.
2024-01-22 11:30:15 - Backup process failed.
"""

import sys
from pathlib import Path
from collections import Counter
from typing import List, Dict, Optional

def parse_log_line(line: str) -> Optional[Dict[str, str]]:
    """
    Ця функція парсить рядок логу.
    Формат: YYYY-MM-DD HH:MM:SS LEVEL Message
    """
    try:
        # split(' ', 3) розділяє рядок тільки по перших 3 пробілах:
        # [Date, Time, Level, Message]
        parts = line.split(' ', 3)
        
        if len(parts) < 4:
            return None

        return {
            "date": parts[0],
            "time": parts[1],
            "level": parts[2],
            "message": parts[3].strip()
        }
    except Exception:
        return None

def load_logs(file_path: str) -> List[Dict[str, str]]:
    """
    Ця функція завантажує логи з файлу.
    """
    path = Path(file_path)
    logs = []

    try:
        if not path.exists():
            print(f"Помилка: Файл '{path.absolute()}' не знайдено.")
            sys.exit(1)

        with path.open('r', encoding='utf-8') as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)

    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)

    return logs

def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """
    Ця функція фільтрує логи за рівнем.
    """
    target_level = level.upper()
    return list(filter(lambda log: log['level'] == target_level, logs))

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Ця функуія підраховує кількість записів для кожного рівня.
    """
    # Генератор списку рівнів передається в Counter
    return dict(Counter(log['level'] for log in logs))

def display_log_counts(counts: Dict[str, int]):
    """
    Ця функція виводить таблицю результатів.
    """
    print(f"\n{'Рівень логування':<17} | {'Кількість':<10}")
    print("-" * 17 + "-|-" + "-" * 10)
    
    for level, count in sorted(counts.items()):
        print(f"{level:<17} | {count:<10}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python task_03.py <path_to_logfile> [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    # 1. Проведемо завантаження
    logs = load_logs(file_path)

    # 2. Проведемо підрахунок і вивід статистики
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # 3. Проведемо вивід деталей, якщо вказано аргумент
    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)
        print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
        
        if filtered_logs:
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print("Записів не знайдено.")

if __name__ == "__main__":
    main()

"""
Інструкція як запустити скрипт:
1. Комбінація кнопок: win+R
2. Прописати у рядку: cmd ,  потім Enter
3. У терміналі прописати шлях до task_03.py та aap.log
3.  Запустити скрипт у терміналі:
* **Тільки статистика:**
    `python task_03.py app.log`
* **Статистика + фільтр помилок:**
    `python task_03.py app.log error`
"""