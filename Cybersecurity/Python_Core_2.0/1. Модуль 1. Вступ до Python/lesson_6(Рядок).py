game_string = 'My favorite "Game"'
print(game_string)  # Output: My favorite "Game"
#==============================================================
s = "Hello world!"
print(s[0])  # H
print(s[-1])  # !
print(s[0:5])  # Hello
#==============================================================
s = "Hello world!"
s[0] = "Q"  # Тут буде викликано виняток (помилка) TypeError
print(s)  # TypeError: 'str' object does not support item assignment
#==============================================================
s = "Hello" 
print(s.upper())  # Виведе 'HELLO'
print(s.lower())  # Виведе 'hello'
#==============================================================
s = "Some Text"
print(s.lower())  # Виведе 'some text'

#==============================================================
s = "Bill Jons"
print(s.startswith("Bi"))  # Виведе True

#==============================================================
s = "hello.jpg"
print(s.endswith("jpg"))  # Виведе True

#==============================================================
s = "hello world".capitalize()  # Результат: "Hello world"
print(s)  # Виведе 'Hello world'
#==============================================================
s = "hello world".title()  # Результат: "Hello World"
print(s)  # Виведе 'Hello World'
#==============================================================
s = "123".isdigit()  # True
s = "hello".isalpha()  # True
s = " ".isspace()  # True
print(s)

#==============================================================
# Просте форматування рядка
name = 'John'
print('Hello, {}!'.format(name))
# Форматування з декількома аргументами
age = 25
print('Hello, {}. You are {} years old.'.format(name, age))
# Використання іменованих аргументів
print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))
# Використання індексів для вказівки порядку аргументів
print('Hello, {1}. You are {0} years old.'.format(age, name))
"""
Hello, John ! 
Hello, John. You are 25 years old.
Hello, Jane. You are 30 years old.
Hello, John. You are 25 years old.
"""
