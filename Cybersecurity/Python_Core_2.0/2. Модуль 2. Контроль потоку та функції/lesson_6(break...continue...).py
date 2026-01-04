#============================================================================
a = 0
while True:
    print(a)
    if a >= 20:
        break
    a = a + 1

#============================================================================
while True:
    user_input = input("Введіть рядок: ")
    print(user_input)
    if user_input == "exit":
        break

#============================================================================
a = 0
while a < 6:
    a = a + 1
    if not a % 2:
        continue
    print(a)

#============================================================================
for i in range(1, 10):
    if i % 2 == 0:
        print(f"{i} є парним числом.")
        
    else:
        print(f"{i} є непарним числом.")

#============================================================================
while True:
    number = input("number = ")
    number = int(number)
    while True:
        print(number)
        number = number - 1
        if number < 0:
            break
