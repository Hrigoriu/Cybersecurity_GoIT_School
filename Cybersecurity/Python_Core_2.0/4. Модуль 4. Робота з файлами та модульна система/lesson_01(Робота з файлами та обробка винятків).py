"""
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

Параметри:
file - шлях до файлу у вигляді рядка. Це може бути повний шлях або шлях відносно поточного каталогу виконання.
mode (необов'язковий) - режим, в якому буде відкрито файл. Ось основні режими які ми будемо використовувати:
'r' - читання (за замовчуванням). Файл має існувати.
'w' - запис. Створює новий файл або перезаписує той, що вже існує.
'a' - додавання. Дописує в кінець файлу, не перезаписуючи його.
'b' - бінарний режим (може бути використаний разом з іншими, наприклад 'rb' або 'wb').
'+' - оновлення (читання та запис).
buffering (необов'язковий) - визначає буферизацію: 0 для вимкненої, 1 для ввімкненої буферизації рядків, більше за 1 для вказання розміру буфера у байтах.
encoding (необов'язковий) - ім'я кодування, яке буде використовуватися для кодування або декодування файлу.
errors (необов'язковий) - вказує, як обробляти помилки кодування.
newline (необов'язковий) - контролює, як обробляються нові рядки.
closefd (необов'язковий) - має бути True (за замовчуванням); якщо вказано False, файловий дескриптор не буде закритий.
opener (необов'язковий) - визначає спеціальну функцію для відкриття файлу.
"""
#=========================================================================================
fh = open('test.txt', 'w')
symbols_written = fh.write('hello!')
print(symbols_written)  # 6
fh.close()

#=========================================================================================
fh = open('test.txt', 'w+')
fh.write('hello!')
fh.seek(0)

first_two_symbols = fh.read(2)
print(first_two_symbols)  # 'he'

fh.close()

#=========================================================================================
fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
all_file = fh.read()
print(all_file)  # 'hello!'

fh.close()

#=========================================================================================
fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)

fh.close()

#=========================================================================================
fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)

fh.close()

#=========================================================================================
fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
lines = fh.readlines()
print(lines)

fh.close()

#=========================================================================================
fh = open("test.txt", "w")
fh.write("first line\nsecond line\nthird line")
fh.close()

fh = open("test.txt", "r")
lines = [el.strip() for el in fh.readlines()]
print(lines)

fh.close()

#=========================================================================================
fh = open('test.txt', 'w+')
fh.write('hello!')

fh.seek(1)
second = fh.read(1)
print(second)  # 'e'

fh.close()

#=========================================================================================
fh = open("test.txt", "w+")
fh.write("hello!")

position = fh.tell()
print(position)  # 6

fh.seek(1)
position = fh.tell()
print(position)  # 1

fh.read(2)
position = fh.tell()
print(position)  # 3

fh.close()

#=========================================================================================
fh = open('text.txt', 'w')
try:
    # Виконання операцій з файлом
    fh.write('Some data')
finally:
    # Закриття файлу в блоці finally гарантує, що файл закриється навіть у разі помилки
    fh.close()
    
#=========================================================================================
with open('text.txt', 'w') as fh:
    # Виконання операцій з файлом
    fh.write('Some data')
# Файл автоматично закриється після виходу з блоку with

#=========================================================================================
with open("test.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open("test.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines)
