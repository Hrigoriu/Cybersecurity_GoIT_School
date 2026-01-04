is_next = None

# введення балів
num = int(input("Enter the number of points: "))

# перевірка умови
if num >= 83:
    is_next = True
else:
    is_next = False

# вивід результату
print("Does the candidate pass to the next round?", is_next)
#============================================================================
work_experience = int(input("Enter your full work experience in years: "))

if work_experience <= 1:
    developer_type = "Junior"
elif 1 < work_experience <= 5:
    developer_type = "Middle"
else:
    developer_type = "Senior"

print("Developer level:", developer_type)
#============================================================================
num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        result = "Positive even number"
    else:
        result = "Positive odd number"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"

print(result)
#============================================================================
# Запитуємо число від користувача
num = int(input("Enter the integer (0 to 100): "))

# Ініціалізуємо суму
sum = 0

# Використовуємо цикл while
while num > 0:
    sum += num
    num -= 1

# Виводимо результат
print("Sum =", sum)
#============================================================================
message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0

for char in message:  # перебираємо кожен символ у рядку message
    if char == search:  # перевіряємо, чи символ співпадає з тим, що шукаємо
        result += 1  # якщо так – додаємо 1

print("Кількість входжень:", result)
#============================================================================
pool = 1000
quantity = int(input("Enter the number of mailings: "))

try:
    chunk = pool // quantity  # використовуємо цілий поділ, щоб отримати "розмір пакета"
    print("SMS per mailing:", chunk)
except ZeroDivisionError:
    print("Помилка: неможливо ділити на нуль!")
#============================================================================
def greeting():
    print("Hello world!")

# виклик функції
greeting()
#============================================================================
def invite_to_event(username):
    return f"Dear {username}, we have the honour to invite you to our event"

# приклад виклику
print(invite_to_event("Anna"))
#============================================================================
def discount_price(price, discount):

    def apply_discount():
        nonlocal price
        price = price * (1 - discount)
    
    apply_discount()
    return price

# приклад використання
print(discount_price(100, 0.2))  # очікуваний результат: 80.0
print(discount_price(200, 0.15))  # очікуваний результат: 170.0
#============================================================================
def get_fullname(first_name, last_name, middle_name=""):
    if middle_name:  # якщо middle_name не порожній
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"

# приклади викликів
print(get_fullname("Григорій", "Шаров"))  
print(get_fullname("Григорій", "Шаров", "Олександрович"))  
#============================================================================
def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        spaces = (length - len(string)) // 2
        return " " * spaces + string

# приклади викликів
print(f"'{format_string('Python', 10)}'")  
# 👉 '  Python'
print(f"'{format_string('Hello, world!', 5)}'")  
# 👉 'Hello, world!' (рядок довший за length, повертається без змін)
#============================================================================
# Функція для позиційних аргументів
def first(size, *args):
    return size + len(args)

# Функція для ключових аргументів
def second(size, **kwargs):
    return size + len(kwargs)

# Приклади викликів
print(first(5, "first", "second", "third"))  # 👉 8
print(first(1, "Alex", "Boris"))  # 👉 3

print(second(3, comment_one="first", comment_two="second", comment_third="third"))  # 👉 6
print(second(10, comment_one="Alex", comment_two="Boris"))  # 👉 12
#============================================================================
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

def number_of_groups(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Приклад виклику
n = 50
k = 7
print(number_of_groups(n, k))  # 👉 99884400
#============================================================================

