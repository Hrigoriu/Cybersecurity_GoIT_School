"""
Метод send() використовується для взаємодії з генератором шляхом надсилання значення у генератор, яке потім може бути використане як результат виразу yield. 
Це дозволяє генератору не лише виробляти дані, але й обробляти зовнішні дані на кожній ітерації.
* Метод send() використовується для передачі значення безпосередньо в генератор, де це значення може бути використане як результат виразу yield.
"""
#==============================================================================================
def my_generator():
    received = yield "Ready"
    yield f"Received: {received}"

gen = my_generator()
print(next(gen))  
print(gen.send("Hello"))  
"""
Ready
Received: Hello
"""
#==============================================================================================
def my_generator():
    try:
        yield "Working"
    except GeneratorExit:
        print("Generator is being closed")

gen = my_generator()
print(next(gen))  # Отримуємо "Working"
gen.close()  # Викликаємо закриття генератора
""" 
Working
Generator is being closed
"""
#==============================================================================================
def square_numbers():
    try:
        while True:  # Безкінечний цикл для прийому чисел
            number = yield  # Отримання числа через send()
            square = number ** 2  # Піднесення до квадрата
            yield square  # Повернення результату
    except GeneratorExit:
        print("Generator closed")

# Створення і старт генератора
gen = square_numbers()

# Ініціалізація генератора
next(gen)  # Або gen.send(None), щоб стартувати

# Відправлення числа в генератор і отримання результату
result = gen.send(10)  # Повинно повернути 100
print(f"Square of 10: {result}")

# Перехід до наступного очікування
next(gen)

# Відправлення іншого числа
result = gen.send(5)  # Повинно повернути 25
print(f"Square of 5: {result}")

# Закриття генератора
gen.close()
"""
Square of 10: 100
Square of 5: 25
Generator closed
"""
#==============================================================================================
def filter_lines(keyword):
    print(f"Looking for {keyword}")
    try:
        while True:  # Нескінченний цикл, де генератор чекає на вхідні дані
            line = yield  # Отримання рядка через send()
            if keyword in line:  # Перевірка на наявність ключового слова
                yield f"Line accepted: {line}"
            else:
                yield None
    except GeneratorExit:
        print("Generator closed")

if __name__ == "__main__":
    # Створення і старт генератора
    gen = filter_lines("hello")
    next(gen)  # Потрібно для старту генератора
    messages = ["this is a test", "hello world", "another hello world line", "hello again", "goodbye"]
    hello_messages = []
    # Відправлення даних у генератор
    for message in messages:
        result = gen.send(message)  # Відправляємо повідомлення в генератор
        if result:  # Додаємо результат тільки якщо він не None
            hello_messages.append(result)
        next(gen)  # Продовжуємо до наступного yield: інструкція line = yield

    # Закриття генератора
    gen.close()
    print(hello_messages)
"""
Looking for hello
Line accepted: hello world
Line accepted: hello again
['Line accepted: hello world', 'Line accepted: hello again']
"""
#==============================================================================================
