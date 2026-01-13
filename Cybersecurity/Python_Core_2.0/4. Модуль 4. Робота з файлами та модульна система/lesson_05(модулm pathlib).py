"""
Модуль pathlib в Python є сучасним інструментом для роботи з файловою системою, що надає об'єктно-орієнтований інтерфейс для роботи з шляхами. Він прийшов на заміну застарілому модулю os.path і забезпечує більш зручний та інтуїтивно зрозумілий спосіб маніпулювання шляхами до файлів і директорій.
"""
#===============================================================================
from pathlib import PurePath

p = PurePath("/usr/bin/simple.jpg")
print("Name:", p.name)  
print("Suffix:", p.suffix) 
print("Parent:", p.parent)

#===============================================================================
from pathlib import Path

p = Path("example.txt")
p.write_text("Hello, world!")
print(p.read_text()) 
print("Exists:", p.exists()) 

#===============================================================================
from pathlib import Path

# Для Unix/Linux
path_unix = Path("/usr/bin/python3")

# Для Windows
path_windows = Path("C:/Users/Username/Documents/file.txt")
print("Unix Path:", path_unix)
print("Windows Path:", path_windows)
#===============================================================================
from pathlib import Path

# Початковий шлях
base_path = Path("/usr/bin")

# Додавання додаткових частин до шляху
full_path = base_path / "subdir" / "script.py"

print(full_path)  # Виведе: /usr/bin/subdir/script.py

#===============================================================================
"""
Приклад на Unix/Linux: /home/user/documents/example.txt
Приклад на Windows: C:\Users\user\documents\example.txt
Абсолютний шлях - це повний шлях до файлу або директорії від кореня файлової системи. 
Відносний шлях - це шлях до файлу або директорії відносно поточного робочого каталогу. 
"""
#===============================================================================
from pathlib import Path

# Перетворення відносного шляху в абсолютний
relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()
print(absolute_path)
#===============================================================================
from pathlib import Path

# Перетворення відносного шляху в абсолютний
relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()

current_working_directory = Path("E:\WebDir\Works\Python\python-help-solution\example_for_new_core\l04")
relative_path = absolute_path.relative_to(current_working_directory)
print(relative_path)

#===============================================================================
from pathlib import Path

# Початковий шлях до файлу
original_path = Path("documents/example.txt")

# Зміна імені файлу
new_path = original_path.with_name("report.txt")
print(new_path)

#===============================================================================
from pathlib import Path

# Початковий шлях до файлу
original_path = Path("documents/example.txt")

# Зміна імені файлу
new_path = original_path.with_suffix(".md")
print(new_path)

#===============================================================================
"""
Треба розуміти, що методи with_name і with_suffix в класі Path модуля pathlib в Python не змінюють фізичне ім'я файлу на диску. Замість цього, вони використовуються для створення нового об'єкта Path, який відображає змінений шлях.
"""
#===============================================================================
from pathlib import Path

original_path = Path("documents/example.txt")

# Створює новий об'єкт Path з іншим ім'ям файлу
new_path = original_path.with_name("report.txt")

print(original_path)  # Виведе: documents/example.txt
print(new_path)       # Виведе: documents/report.txt

#===============================================================================
from pathlib import Path

original_path = Path("documents/example.txt")

# Створює новий об'єкт Path з іншим ім'ям файлу
new_path = original_path.with_name("report.txt")
original_path.rename(new_path)
print("File renamed successfully.") # 

#===============================================================================
from pathlib import Path

# Створення об'єкту Path для файлу
file_path = Path("example.txt")

# Запис тексту у файл
file_path.write_text("Привіт світ!", encoding="utf-8")

#===============================================================================
from pathlib import Path

# Створення об'єкту Path для файлу
file_path = Path("example.txt")

# Читання тексту з файлу
text = file_path.read_text(encoding="utf-8")
print(text)

#===============================================================================
from pathlib import Path

# Створення об'єкту Path для бінарного файлу
file_path = Path("example.bin")

# Бінарні дані для запису
data = b"Python is great!"

# Запис байтів у файл
file_path.write_bytes(data)

#===============================================================================
from pathlib import Path

# Створення об'єкту Path для бінарного файлу
file_path = Path("example.bin")

# Читання байтів з файлу
binary_data = file_path.read_bytes()
print(binary_data)

#===============================================================================
from pathlib import Path

# Створення об'єкту Path для директорії
directory = Path("./picture")

# Виведення переліку всіх файлів та піддиректорій
for path in directory.iterdir():
    print(path)
"""
📦core_course
 ┣ 📂picture
 ┃ ┣ 📂Logo
 ┃ ┣ 📜bot-icon.png
 ┃ ┗ 📜mongodb.jpg
 ┗ 📜ex01.py
"""
"""
picture\bot-icon.png
picture\Logo
picture\mongodb.jpg
"""
#===============================================================================
from pathlib import Path
directory = Path('/my_directory/new_folder')
directory.mkdir(parents=True, exist_ok=True)
print(f"Directory '{directory}' created successfully.")
#===============================================================================
from pathlib import Path
directory = Path('/my_directory/new_folder')
directory.rmdir()
print(f"Directory '{directory}' removed successfully.")
#===============================================================================
from pathlib import Path

path = Path("./picture")

# Перевірка існування
if path.exists():
    print(f"{path} існує")  # picture існує

# Перевірка, чи це директорія
if path.is_dir():
    print(f"{path} є директорією") # picture є директорією

# Перевірка, чи це файл
if path.is_file():
    print(f"{path} є файлом")

#===============================================================================
import shutil
from pathlib import Path

# Вихідний і цільовий файли
source = Path('/path/to/source/file.txt')
destination = Path('/path/to/destination/file.txt')

# Копіювання файла
shutil.copy(source, destination)
print(f"File copied from {source} to {destination}")
#===============================================================================
"""
Функція shutil.copy() копіює вміст файлу, але не копіює метадані, 
тоді як shutil.copy2() копіює і вміст, і метадані.
"""
#===============================================================================
import shutil
from pathlib import Path

# Вихідний і цільовий шляхи
source = Path('/path/to/source/file.txt')
destination = Path('/path/to/destination/file.txt')

# Переміщення файла
shutil.move(source, destination)
print(f"File moved from {source} to {destination}")
#===============================================================================    
from pathlib import Path

file_path = Path("./picture/bot-icon.png")

# Отримання розміру файла
size = file_path.stat().st_size
print(f"Розмір файла: {size} байтів")  # Розмір файла: 2876 байтів

#===============================================================================
from pathlib import Path
import time

file_path = Path("./picture/bot-icon.png")

# Час створення та модифікації
creation_time = file_path.stat().st_ctime
modification_time = file_path.stat().st_mtime

print(f"Час створення: {time.ctime(creation_time)}")
print(f"Час модифікації: {time.ctime(modification_time)}")
"""
Час створення: Fri Dec 29 04:43:16 2023
Час модифікації: Thu May 17 19:59:44 2018
"""
#===============================================================================
from pathlib import Path

# Створення об'єкту Path для файлу
file_path = Path('/path/to/file.txt')

# Перевірка, чи файл існує, перш ніж видаляти
if file_path.exists():
    file_path.unlink()
    print(f'Файл {file_path} було видалено')
else:
    print(f'Файл {file_path} не існує')

#===============================================================================
from pathlib import Path
file_path = Path('/path/to/file.txt')
file_path.unlink(missing_ok=True)
print(f'Файл {file_path} було видалено, якщо він існував')
#===============================================================================

#===============================================================================

#===============================================================================
