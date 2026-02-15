import argparse  # Імпортуємо бібліотеку для обробки команд з терміналу (щоб передавати шлях до папки)
from pathlib import Path  # Імпортуємо бібліотеку для роботи зі шляхами до файлів (краще ніж os.path)
from shutil import move  # Імпортуємо функцію для фізичного переміщення файлів
import logging  # Імпортуємо бібліотеку для виведення повідомлень (логів) про роботу програми
from concurrent.futures import ThreadPoolExecutor  # Імпортуємо інструмент для створення пулу потоків (багатопоточність)

# Налаштуємо логування
# level=logging.INFO означає, що ми будемо бачити звичайні повідомлення та помилки
# format - це вигляд повідомлення: "Ім'яПотоку: Повідомлення"
logging.basicConfig(level=logging.INFO, format='%(threadName)s: %(message)s')

# Створимо словник констант, де визначио, які розширення куди класти.
EXTENSIONS = {
    'images': ['.jpeg', '.png', '.jpg', '.svg', '.bmp'],
    'video': ['.avi', '.mp4', '.mov', '.mkv'],
    'documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    'audio': ['.mp3', '.ogg', '.wav', '.amr'],
    'archives': ['.zip', '.gz', '.tar'],
}

def get_category(file_path: Path) -> str:
    """
    Створимо функцію, яка приймає шлях до файлу і визначить його категорію.
    Наприклад: 'photo.jpg' -> поверне 'images'
    """
    # Отримаємо розширення файлу (наприклад, '.jpg') і перетвориємо на малі літери (.JPG -> .jpg)
    ext = file_path.suffix.lower()
    
    # Перебиремо наш словник категорій
    for cat, exts in EXTENSIONS.items():
        if ext in exts:
            return cat  # Якщо знайшли розширення - повертаємо назву категорії
            
    return 'other'  # Якщо розширення немає в списку - це категорія 'other'

def sort_file(file_path: Path, root_folder: Path):
    """
    Сиворимо головну функцію-робітник. Вона буде запускатися в окремому потоці.
    ВОна переміщує один конкретний файл у відповідну папку.
    """
    try:
        # 1. Визначио, куди нести файл
        category = get_category(file_path)
        target_folder = root_folder / category  # Сформуємо шлях: "Папка/images"
        
        # 2. Створимо цільову папку, якщо її ще немає.
        # parents=True: створимо всі проміжні папки.
        # exist_ok=True: не свариться, якщо папка вже є 
        # (це важливо для потоків, які можуть одночасно це робити).
        target_folder.mkdir(exist_ok=True, parents=True)
        
        # 3. Сформуємо повний шлях, де буде лежати файл після переміщення
        target_path = target_folder / file_path.name
        
        # 4. Перевіримо на дублікати: якщо файл з таким іменем вже є в папці призначення
        if target_path.exists():
            # Додамо "_copy" до імені, щоб не затерти існуючий файл
            # .stem - це ім'я без розширення ("photo"), .suffix - розширення (".jpg")
            target_path = target_folder / f"{file_path.stem}_copy{file_path.suffix}"

        # 5. Фізичне переміщення файлу
        move(str(file_path), str(target_path))
        
    except Exception as e:
        # Якщо щось педе не так (наприклад, файл зайнятий іншою програмою), напишемо помилку в лог
        logging.error(f"Error moving {file_path}: {e}")

def clean_empty_folders(path: Path):
    """
    Створимо функцію, яка видаляє порожні папки після сортування.
    Працює рекурсивно "знизу вгору".
    """
    # path.rglob('*') шукає все підряд у всіх папках.
    # Сортуємо результати за глибиною (len(p.parts)), reverse=True означає від найглибших до верхніх.
    # Це треба, щоб спочатку видалити порожню вкладену папку, а потім її батьківську, якщо та теж стане порожньою.
    for element in sorted(path.rglob('*'), key=lambda p: len(p.parts), reverse=True):
        # Перевірио, чи це папка, і чи це не одна з наших створених папок категорій
        if element.is_dir() and element.name not in EXTENSIONS.keys() and element.name != 'other':
            try:
                element.rmdir()  # rmdir видалить ТІЛЬКИ порожні папки. Якщо там щось є - видасть помилку.
            except OSError:
                pass # Якщо помилка (папка не порожня) - просто будемо ігнорувати.

def main():
    # Створимо функцію налаштування обробки аргументів командного рядка
    parser = argparse.ArgumentParser(description="Сортування файлів у папці за допомогою потоків.")
    # nargs="?" робить аргумент необов'язковим
    parser.add_argument("source", type=str, nargs="?", help="Шлях до вихідної папки для сортування.")
    args = parser.parse_args()

    # СТОРИМО ЛОГІКУ ОТРИМАННЯ ШЛЯХУ
    if args.source:
        # Якщо користувач вкаже шлях при запуску (python main.py "D:/Folder")
        source_path = Path(args.source)
    else:
        # Якщо користувач не вкаже - питаємо через консоль
        print("Папку не вказано через аргументи.")
        user_input = input("Введіть шлях до папки для сортування: ").strip()
        if not user_input:
            print("Шлях не введено. Завершення роботи.")
            return
        source_path = Path(user_input)

    # Створимо перевірку, чи існує така папка взагалі
    if not source_path.exists() or not source_path.is_dir():
        print(f"Помилка: Папка '{source_path}' не існує.")
        return

    print(f"Починаємо сортування в: {source_path}")
    
    # КРОК 1: Почнемо збирати список файлів (Синхронно - одним потоком)
    # Використовуємо rglob('*'), це дуже швидкий системний виклик для пошуку файлів.
    # Зробимо це ДО запуску потоків, щоб уникнути помилок блокування.
    all_files = []
    for item in source_path.rglob('*'):
        if item.is_file():
            # Важливий фільтр: пропускаємо файли, які вже лежать у відсортованих папках (images, video...)
            # item.parent.name - це назва папки, в якій лежить файл.
            if item.parent.name in EXTENSIONS.keys() or item.parent.name == 'other':
                continue
            all_files.append(item)

    if not all_files:
        print("Файлів для сортування не знайдено.")
        # Про всяк випадок чистимо порожні папки, навіть якщо файлів немає
        clean_empty_folders(source_path)
        return

    print(f"Знайдено файлів: {len(all_files)}. Запускаємо потоки...")

    # КРОК 2: Багатопотокова обробка
    # ThreadPoolExecutor створить пул (групу) з 4 потоків.
    # with гарантує, що програма не піде далі, доки всі потоки не закінчать роботу.
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Для кожного файлу зі списку дамо завдання пулу: "Виконай функцію sort_file з цим файлом"
        for file in all_files:
            executor.submit(sort_file, file, source_path)
            # submit не чекає виконання, він просто кидає задачу в чергу і йде далі.
            # Потоки підхоплять задачі з черги, як тільки звільняться.
    
    print("Сортування завершено.")
    
    # КРОК 3: Прибирання сміття
    clean_empty_folders(source_path)
    print("Порожні папки видалено.")

if __name__ == "__main__":
    main()