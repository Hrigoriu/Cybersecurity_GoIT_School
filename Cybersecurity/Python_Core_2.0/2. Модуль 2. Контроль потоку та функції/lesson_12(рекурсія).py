def factorial(n):
    if n == 0:  # базовий випадок
        return 1
    else:
        return n * factorial(n - 1)  # рекурсивний випадок

print(factorial(5))  # виведе 120

#============================================================================
def fibonacci(n):
    if n <= 1:  # базовий випадок
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # рекурсивний випадок

print(fibonacci(10))  # виведе 55

#============================================================================
def factorial(n):
    print("Виклик функції factorial з n = ", n)
    if n == 1:
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial(n - 1)
        print("Повернення результату для n = ", n, ": ", result)
        return result

print(factorial(5))
