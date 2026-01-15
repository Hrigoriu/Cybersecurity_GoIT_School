"""
Замикання (closure) в програмуванні — це потужна концепція, особливо в мовах, що підтримують функції вищого порядку, як наприклад Python. Замикання відбувається, коли внутрішня функція запам'ятовує стан свого оточення в момент свого створення і може використовувати ці змінні навіть після того, як зовнішня функція завершила своє виконання.

Ключові аспекти замикань:
*Внутрішня функція має доступ до змінних, визначених у області видимості зовнішньої функції.
*Зовнішня функція повертає внутрішню функцію як результат своєї роботи.
*Після завершення роботи зовнішньої функції, внутрішня функція зберігає доступ до цих змінних, що відіграє важливу роль у певних програмних патернах та алгоритмах.
"""
#===========================================================================================
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function


# Створення замикання
my_func = outer_function("Hello, world!")
my_func()

#===========================================================================================
from typing import Callable

def counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        # використовуємо nonlocal, щоб змінити змінну в замиканні
        nonlocal count  
        count += 1
        return count

    return increment

# Створення лічильника
count_calls = counter()

# Виклики лічильника
print(count_calls())  # Виведе 1
print(count_calls())  # Виведе 2
print(count_calls())  # Виведе 3

#===========================================================================================
"""
Каррінг (currying) — це техніка в програмуванні, коли функція, яка приймає кілька аргументів, перетворюється на послідовність функцій, кожна з яких приймає один аргумент.
"""
#===========================================================================================
def add(a):

    def add_b(b):
        return a + b

    return add_b


# Використання:
add_5 = add(5)
result = add_5(10)
print(result)

#===========================================================================================
def apply_discount(price: float, discount_percentage: int) -> float:
    return price * (1 - discount_percentage / 100)


# Використання
discounted_price = apply_discount(500, 10)  # Знижка 10% на ціну 500
print(discounted_price)

discounted_price = apply_discount(500, 20)  # Знижка 20% на ціну 500
print(discounted_price)

#===========================================================================================
from typing import Callable


def discount(discount_percentage: int) -> Callable[[float], float]:

    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)

    return apply_discount

# Каррінг в дії
ten_percent_discount = discount(10)
twenty_percent_discount = discount(20)

# Застосування знижок
discounted_price = ten_percent_discount(500)  # 450.0
print(discounted_price)

discounted_price = twenty_percent_discount(500)  # 400.0
print(discounted_price)
#===========================================================================================
from typing import Callable, Dict


def discount(discount_percentage: int) -> Callable[[float], float]:

    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)

    return apply_discount


# Створення словника з функціями знижок
discount_functions: Dict[str, Callable] = {
    "10%": discount(10),
    "20%": discount(20),
    "30%": discount(30)
}

# Використання функції зі словника
price = 500
discount_type = "20%"

discounted_price = discount_functions[discount_type](price)
print(f"Ціна зі знижкою {discount_type}: {discounted_price}")
