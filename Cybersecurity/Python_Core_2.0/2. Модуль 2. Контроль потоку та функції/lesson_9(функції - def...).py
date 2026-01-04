def say_hello():
		# тіло функції
    print('Привіт, Світ!')

# Кінець функції say_hello()

# виклик функції
say_hello()

# ще один виклик функції
say_hello()

#============================================================================
"""
!!!
Зверніть увагу на термінологію: 
імена, вказані при оголошенні функції, називаються параметрами, 
тоді як значення, які ви передаєте у функцію при її виклику, – аргументами.

Наприклад, у наведеній нижче функції name є параметром, а 'Alice' – аргументом.
def greet(name):  # name - параметр
    print(f"Hello, {name}!")    
greet('Alice')  # 'Alice' - аргумент
!!!
"""
#============================================================================
def print_max(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')


print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних як аргументів

#============================================================================
def print_max(a: int, b: int):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних як аргументів

#============================================================================
def my_function() -> ReturnType:
    # виконати дії
    return result

#============================================================================
def add_numbers(num1: int, num2: int) -> int:
    sum = num1 + num2
    return sum

result = add_numbers(5, 10)
print(result)  # Виведе: 15

#============================================================================
def greet(name: str) -> str:
    return f"Привіт, {name}!"

greeting = greet("Олексій")
print(greeting)  # Виведе: Привіт, Олексій!

#============================================================================
def is_even(num: int) -> bool:
    return num % 2 == 0

check_even = is_even(4)
print(check_even)  # Виведе: True

#============================================================================
def modify_string(original: str) -> str:
    original = "змінено"
    return original


str_var = "оригінал"
print(modify_string(str_var))  # виведе: змінено
print(str_var)  # виведе: оригінал

#============================================================================
def modify_list(lst: list) -> None:
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3, 4]

#============================================================================
def modify_list(lst: list) -> None:
    lst = lst.copy()
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3]

#============================================================================
def string_to_codes(string: str) -> dict:
    # Ініціалізація словника для зберігання кодів
    codes = {}  
    # Перебір кожного символу в рядку
    for ch in string: 
        # Перевірка, чи символ вже є в словнику
        if ch not in codes:
            # Додавання пари символ-код в словник  
            codes[ch] = ord(ch)  
    return codes

result = string_to_codes("Hello world!")
print(result)

