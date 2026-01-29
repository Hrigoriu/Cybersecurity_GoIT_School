my_list = [1, 2, 3]
copy_list = my_list
copy_list.append(4)
print(my_list)
# Output: [1, 2, 3, 4]
#===================================================================================================
my_list = [1, 2, 3]

def square_list(x: list):
    for i, el in enumerate(x):
        x[i] = el**2
    return x

new_list = square_list(my_list)
print(new_list)
print(my_list)
# Output:   [1, 4, 9]
#           [1, 4, 9]
#===================================================================================================
my_list = [1, 2, 3]

def square_list(x: list):
    return [el**2 for el in x]

new_list = square_list(my_list)
print(new_list)
print(my_list)
# Output:   [1, 4, 9]
#           [1, 2, 3]
#===================================================================================================
my_list = [1, 2, 3]
copy_list = my_list[:]
copy_list.append(4)
print(my_list, copy_list)

my_dict = {1: "a"}
copy_dict = {**my_dict}
copy_dict["new_key"] = "new_value"
print(my_dict, copy_dict)
# Output:   [1, 2, 3] [1, 2, 3, 4]
#           {1: 'a'} {1: 'a', 'new_key': 'new_value'}

#===================================================================================================
"""
    !"поверхнева" копія об'єкта !
Поверхневе копіювання створює новий об'єкт, але не копіює вкладені об'єкти.
Щоб створити "поверхневу" копію об'єкта, у пакеті copy є функція copy. 
Ця функція створює новий об'єкт такого самого типу і потім створює посилання на увесь вміст старого об'єкта в новий. 
Такий механізм досить хороший для роботи з об'єктами, де вже на першому рівні вкладеності немає змінних об'єктів, і він працює досить швидко.
"""
#===================================================================================================
"""
☝ Поверхнева копія створює новий об'єкт, але не копіює вкладені об'єкти. 
Замість цього, вона копіює лише посилання на вкладені об'єкти. 
Це означає, що якщо ви змінюєте вкладені об'єкти в оригіналі, ці зміни також відобразяться у поверхневій копії.
"""
#===================================================================================================
import copy

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.copy(my_list)
copy_list.append(4)
print(my_list)
print(copy_list)

copy_list[2]["name"] = "Ivanov Ivan"
print(my_list)
print(copy_list)
"""
[1, 2, {'name': 'Gupalo Vasyl'}]
[1, 2, {'name': 'Gupalo Vasyl'}, 4]
[1, 2, {'name': 'Ivanov Ivan'}]
[1, 2, {'name': 'Ivanov Ivan'}, 4]
"""
#===================================================================================================
import copy

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.copy(my_list)
copy_list[2]["age"] = 30
print(my_list)
print(copy_list)
"""
[1, 2, {'name': 'Gupalo Vasyl', 'age': 30}]
[1, 2, {'name': 'Gupalo Vasyl', 'age': 30}]
"""
#===================================================================================================
"""
    !"глибока" копія об'єкта !
Глибока копія створює новий об'єкт та рекурсивно копіює всі вкладені об'єкти. 
В результаті, ви отримуєте повністю незалежну копію оригінального об'єкта.
Метод deepcopy() створює новий об'єкт і рекурсивно копіює всі об'єкти, до яких він має посилання.

Метод deepcopy() створює новий об'єкт і рекурсивно копіює всі об'єкти, до яких він має посилання.
Для створення глибокої копії використовуйте метод deepcopy() модуля copy. 
Ця функція рекурсивно створює нові об'єкти.
"""
#===================================================================================================
import copy

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.deepcopy(my_list)
copy_list[2]["age"] = 30
print(my_list)
print(copy_list)
"""
[1, 2, {'name': 'Gupalo Vasyl'}]
[1, 2, {'name': 'Gupalo Vasyl', 'age': 30}]
"""
#===================================================================================================
"""
Коли викликаємо copy.copy() або copy.deepcopy() на об'єкті, Python автоматично шукає і викликає ці магічні методи в класі об'єкта, якщо вони визначені.

__copy__ повинен повертати поверхневу копію об'єкта.
__deepcopy__ повинен повертати глибоку копію об'єкта. 
Він приймає додатковий аргумент memo, який є словником, що використовується для уникнення нескінченної рекурсії при копіюванні вкладених об'єктів, які посилаються самі на себе.
"""
#===================================================================================================
import copy

class MyClass:
    def __init__(self, value):
        self.value = value

    def __copy__(self):
        print("Викликано __copy__")
        return MyClass(self.value)

    def __deepcopy__(self, memo=None):
        print("Викликано __deepcopy__")
        return MyClass(copy.deepcopy(self.value, memo))

# Поверхневе копіювання
obj = MyClass(5)
obj_copy = copy.copy(obj)
obj_copy.value = 10

# Глибоке копіювання
obj_deepcopy = copy.deepcopy(obj)
obj_deepcopy.value = 20
print(obj.value, obj_copy.value, obj_deepcopy.value)
""" 
Викликано __copy__
Викликано __deepcopy__
5 10 20
"""
#===================================================================================================
import copy

class SimpleObject:
    def __init__(self, greeting: str):
        self.greeting = greeting

class ComplexObject:
    def __init__(self, value: int, nested_obj: SimpleObject):
        self.value = value
        self.nested_obj = nested_obj

    def __copy__(self):
        print("Викликано __copy__ для ComplexObject")
        # Поверхневе копіювання не копіює вкладені об'єкти глибоко
        return ComplexObject(self.value, self.nested_obj)

    def __deepcopy__(self, memo=None):
        print("Викликано __deepcopy__ для ComplexObject")
        # Глибоке копіювання копіює вкладені об'єкти
        return ComplexObject(
            copy.deepcopy(self.value, memo), copy.deepcopy(self.nested_obj, memo)
        )

nested_obj = SimpleObject("Привіт")
complex_obj = ComplexObject(5, nested_obj)

# Створюємо копію та глибоку копію
complex_obj_copy = copy.copy(complex_obj)
complex_obj_deepcopy = copy.deepcopy(complex_obj)

# Змінюємо значення вкладеного об'єкту nested_obj
nested_obj.greeting = "Hello"

# Дивимось зміни у об'єктах
print(f"Copy object: {complex_obj_copy.nested_obj.greeting}")
print(f"Deepcopy object: {complex_obj_deepcopy.nested_obj.greeting}")
"""
Copy object: Hello
Deepcopy object: Привіт
"""
#===================================================================================================
import copy

class SimpleObject:
    def __init__(self, greeting: str):
        self.greeting = greeting

class ComplexObject:
    def __init__(self, value, nested_obj: SimpleObject):
        self.value = value
        self.nested_obj = nested_obj

nested_obj = SimpleObject("Привіт")
complex_obj = ComplexObject(5, nested_obj)

# Створюємо копію та глибоку копію
complex_obj_copy = copy.copy(complex_obj)
complex_obj_deepcopy = copy.deepcopy(complex_obj)

# Змінюємо значення вкладеного об'єкту nested_obj
nested_obj.greeting = "Hello"

# Дивимось зміни у об'єктах
print(f"Copy object: {complex_obj_copy.nested_obj.greeting}")
print(f"Deepcopy object: {complex_obj_deepcopy.nested_obj.greeting}")
"""
Copy object: Hello
Deepcopy object: Привіт
"""
#===================================================================================================
import copy

class UserSettings:
    def __init__(self, preferences, large_data_reference):
        self.preferences = preferences
        self.large_data_reference = large_data_reference

    def __deepcopy__(self, memo):
        print("Кастомізоване глибоке копіювання для UserSettings")
        # Припустимо, що preferences - це невеликий словник, який можна безпечно скопіювати,
        # а large_data_reference - це посилання на великий об'єкт даних, яке ми не хочемо дублювати.
        new_preferences = copy.deepcopy(self.preferences, memo)
        # Передаємо посилання на ті ж великі дані замість їх копіювання
        new_obj = UserSettings(new_preferences, self.large_data_reference)
        return new_obj

# Створення екземпляра UserSettings
original_settings = UserSettings({"language": "uk"}, large_data_reference="LargeDataID")

# Глибоке копіювання з кастомізованою логікою
settings_copy = copy.deepcopy(original_settings)
# Output:
# Кастомізоване глибоке копіювання для UserSettings
#===================================================================================================
