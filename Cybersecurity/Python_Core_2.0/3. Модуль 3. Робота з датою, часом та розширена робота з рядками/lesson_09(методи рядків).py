s = "Hi there!"
start = 0
end = 7

print(s.find("er", start, end))  # 5
print(s.find("q"))  # -1
#====================================================================================
s = 'Some words'

print(s.find("o"))  #1
print(s.rfind('o')) #6
#====================================================================================

s = 'Some words'

print(s.index("o")) #1
print(s.rindex('o')) #6   #====================================================================================
#====================================================================================
str.split(separator=None, maxsplit=-1)
#====================================================================================
#====================================================================================
text = "hello world"
result = text.split()
print(result)  # Виведе: ['hello', 'world']
#====================================================================================
text = "apple,banana,cherry"
result = text.split(',')
print(result)  # Виведе: ['apple', 'banana', 'cherry']
#====================================================================================
#====================================================================================
string.join(iterable)
#====================================================================================
#====================================================================================
list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings)
print(result)  # Виведе: 'Hello world'
#====================================================================================
elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)  # Виведе: 'earth, air, fire, water'
#====================================================================================
clean = '   spacious   '.strip()
print(clean)  # spacious
#====================================================================================
#====================================================================================
str.replace(old, new, count=-1)
#====================================================================================
#====================================================================================
text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text) # Виведе: Hello Python
#====================================================================================
text = "one fish, two fish, red fish, blue fish"
new_text = text.replace("fish", "bird", 2)
print(new_text)  # Виведе: one bird, two bird, red fish, blue fish
#====================================================================================
text = "Hello, world!"
new_text = text.replace(" world", "")
print(new_text) # Виведе: Hello!
#====================================================================================
print('TestHook'.removeprefix('Test'))  # Hook
print('TestHook'.removeprefix('Hook'))  # TestHook
#====================================================================================
print('TestHook'.removesuffix('Test'))  # TestHook
print('TestHook'.removesuffix('Hook'))  # Test
#====================================================================================
url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)  # Виведе: q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t
#====================================================================================
url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)
# Виведе: {'q': 'Cat and dog', 'ie': 'utf-8', 'oe': 'utf-8', 'aq': 't'}
#====================================================================================
number = "12345"
print(number.isdigit())  # Виведе: True

text = "Number123"
print(text.isdigit())  # Виведе: False
#====================================================================================
user_input = input("Введіть число: ")
if user_input.isdigit():
    print("Це дійсно число!")
else:
    print("Це не число!")
#====================================================================================
for char in "Hello 123":
    if char.isdigit():
        print(f"'{char}' - це цифра")
    else:
        print(f"'{char}' - не цифра")
#====================================================================================
