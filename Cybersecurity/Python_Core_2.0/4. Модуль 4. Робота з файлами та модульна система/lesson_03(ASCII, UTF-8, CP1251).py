#===============================================================================
s = "Привіт!"

utf8 = s.encode()
print(f"UTF-8: {utf8}")

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)

#===============================================================================
print(b'Hello world!'.decode('utf-16'))

#===============================================================================
# Відкриття текстового файлу з явними вказівками UTF-8 кодування
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
#===============================================================================
byte_array = bytearray(b'Kill Bill')
byte_array[0] = ord('B')
byte_array[5] = ord('K')
print(byte_array)

#===============================================================================
byte_array = bytearray(b"Hello")
byte_array.append(ord("!"))  
print(byte_array)

#===============================================================================
byte_array = bytearray(b"Hello World")
string = byte_array.decode("utf-8")
print(string)  # Виведе: 'Hello World'

#===============================================================================
string1 = "Hello World"
string2 = "hello world"
if string1.lower() == string2.lower():
    print("Рядки однакові")
else:
    print("Рядки різні")

#===============================================================================
text = "Python Programming"
print(text.casefold())

#===============================================================================
german_word = 'straße'  # В нижньому регістрі
search_word = 'STRASSE'  # В верхньому регістрі

# Порівняння за допомогою lower()
lower_comparison = german_word.lower() == search_word.lower()

# Порівняння за допомогою casefold()
casefold_comparison = german_word.casefold() == search_word.casefold()

print(f"Порівняння з lower(): {lower_comparison}")
print(f"Порівняння з casefold(): {casefold_comparison}")

