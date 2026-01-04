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
