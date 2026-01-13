"""
Синтаксис методу:
shutil.make_archive(base_name, format, root_dir=None, base_dir=None)

Параметри:
base_name - шлях до файлу, де потрібно зберегти архів, без розширення.
format - формат архіву, наприклад 'zip', 'tar', 'gztar', 'bztar' або 'xztar'.
root_dir - директорія, з якої буде створено архів. Якщо не вказано, використовується поточна директорія.
base_dir - директорія всередині архіву, з якої почнеться архівація.
"""

#===============================================================================
import shutil

# Створення ZIP-архіву з вмістом директорії 'my_folder'
shutil.make_archive('example', 'zip', root_dir='my_folder')

#===============================================================================
import shutil

# Створення TAR.GZ-архіву
shutil.make_archive('example', 'gztar', root_dir='my_folder')

#===============================================================================
"""
Синтаксис
shutil.unpack_archive(filename, extract_dir=None, format=None)

Параметри
filename - шлях до архівного файлу, який потрібно розпакувати.
extract_dir - директорія, куди буде розпаковано вміст архіву. Якщо не вказано, використовується поточна директорія.
format - формат архіву наприклад, zip, tar, gztar, bztar, або xztar. Якщо параметр не вказано, Python намагається визначити формат автоматично.
"""
#===============================================================================
import shutil

# Розпакування ZIP-архіву в певну директорію
shutil.unpack_archive('example.zip', 'destination_folder')

#===============================================================================
import shutil

# Копіюємо файл
source_file = '/path/to/source/file.txt'
destination_dir = '/path/to/destination'
shutil.copy(source_file, destination_dir)

# Копіюємо всю директорію
source_dir = '/path/to/source/directory'
destination_dir = '/path/to/destination/directory'
shutil.copytree(source_dir, destination_dir)
