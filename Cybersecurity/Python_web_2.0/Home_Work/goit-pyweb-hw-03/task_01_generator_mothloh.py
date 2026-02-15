import os
from pathlib import Path  # Імпортуємо клас Path для зручної роботи зі шляхами (Windows/Mac/Linux)

# 1. КОНФІГУРАЦІЯ
# ----------------
# Назва папки, яку ми створимо. Path автоматично зрозуміє формат шляху вашої ОС.
TARGET_FOLDER = Path("Test_Folder_Mothloh")

# Використаємо словник з розширеннями.
# Ключ (наприклад, 'images') стане частиною назви файлу.
# Значення (список) - це розширення, які ми будемо використовувати.
EXTENSIONS = {
    'images': ['.jpeg', '.png', '.jpg', '.svg', '.bmp'],
    'video': ['.avi', '.mp4', '.mov', '.mkv'],
    'documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    'audio': ['.mp3', '.ogg', '.wav', '.amr'],
    'archives': ['.zip', '.gz', '.tar'],
}

def create_dummy_files(root_path: Path):
    """
    Створимо головну функцію для створення тестового середовища, яка
    приймає шлях (root_path), де треба створити файли.
    """
    
    # 2. СТВОРЕННЯ КОРЕНЕВОЇ ПАПКИ
    # ----------------------------
    # mkdir - створить папку. 
    # exist_ok=True означатиме: "не видавати помилку, якщо папка вже існує".
    root_path.mkdir(exist_ok=True)
    
    # .absolute() покаже повний шлях на диску (наприклад, C:\Users\...\Test_Folder_Mothloh)
    print(f"Створено/знайдено папку: {root_path.absolute()}")

    # 3. ГЕНЕРАЦІЯ ОСНОВНИХ ФАЙЛІВ
    # ----------------------------
    print("Генерую файли в кореневій директорії...")
    
    # items() розбиратиме словник на пари: category ('images') та exts (['.jpeg', ...])
    for category, exts in EXTENSIONS.items():
        # Тепер перебиремо кожне розширення у списку (наприклад, спочатку .jpeg, потім .png)
        for ext in exts:
            # Створимо по 4 файли кожного типу (range(1, 5) дасть числа 1, 2, 3, 4)
            for i in range(1, 5):
                # f-string: сформуємо назву, наприклад "images_file_1.jpeg"
                filename = f"{category}_file_{i}{ext}"
                
                # root_path / filename - це "склеювання" шляху. 
                # Вийде: Test_Folder_Mothloh\images_file_1.jpeg
                file_path = root_path / filename
                
                # .touch() - це команда "створити порожній файл". 
                # Якщо файл є, вона просто оновить час його зміни.
                file_path.touch()

    # 4. ГЕНЕРАЦІЯ ВКЛАДЕНИХ ПАПОК
    # ----------------------------
    # Створимо список шляхів, які потрібно створити всередині головної папки
    nested_structure = [
        "Downloads/Old",      # Папка Old всередині Downloads
        "DCIM/Vacation",      # Папка Vacation всередині DCIM
        "Work/Docs/2023"      # Папка 2023 всередині Docs, яка всередині Work
    ]

    print("Генерую вкладені папки...")
    for subfolder in nested_structure:
        # Склеємо головний шлях + підпапку
        path = root_path / subfolder
        
        # parents=True дозволить створити весь ланцюжок папок одразу (наприклад, і Work, і Docs, і 2023)
        path.mkdir(parents=True, exist_ok=True)
        
        # Створио кілька файлів у цих глибоких папках, щоб перевірити, чи знайде їх програма
        (path / "deep_nested_doc.txt").touch()
        (path / "deep_nested_img.png").touch()
        (path / "holiday_movie.mkv").touch()

    # 5. ГЕНЕРАЦІЯ "СМІТТЯ"
    # ---------------------
    # Створимо файли, які не підпадають під наші категорії (для тесту папки 'other')
    print("Генерую файли для категорії 'other'...")
    
    (root_path / "unknown_config.ini").touch() # Невідоме розширення .ini
    (root_path / "program.xyz").touch()        # Вигадане розширення .xyz
    (root_path / "README").touch()             # Файл взагалі без розширення

    # 6. ФІНАЛ
    # --------
    print("-" * 40)
    print("✅ Готово! Тестове середовище створено.")
    print(f"Тепер запустіть ваш основний скрипт (task_01_sort_mothloh.py) для цієї папки:")
    # Покажемо команду для запуску
    print(f'File python: task_01_sort_mothloh.py "{root_path}"')

# Цей блок буде працювати тільки якщо запускати файл напряму, а не імпортувати його
if __name__ == "__main__":
    create_dummy_files(TARGET_FOLDER)