"""
        ! Методи __getitem__ та __setitem__ !
 Ці методи в Python використовуються для налаштування доступу до елементів об'єкта за допомогою індексації або ключів, подібно до роботи зі списками чи словниками. 
 Ці магічні методи дозволяють нашим класам імітувати контейнерні типи даних.
"""
#==============================================================================================
"""
    ! Метод __getitem__ !
* Це метод, який визначає, як об'єкт класу повинен вести себе при доступі до його елементів за допомогою індексу або ключа. 
Він приймає ключ або індекс як аргумент і повинен повертати значення, асоційоване з цим ключем або індексом.
* визначає поведінку об'єкта при доступі до його елементів за допомогою індексу або ключа.
"""
#==============================================================================================
"""
    ! Метод __setitem__ !
* Це метод, який визначає, як об'єкт повинен поводити себе при присвоєнні значення елементу за певним індексом або ключем. 
Він приймає два аргументи: ключ (або індекс) та значення, яке потрібно асоціювати з цим ключем.
"""
#==============================================================================================
class SimpleDict:
    def __init__(self):
        self.__data = {}

    def __getitem__(self, key):
        return self.__data.get(key, "Key not found")

    def __setitem__(self, key, value):
        self.__data[key] = value

# Використання класу
simple_dict = SimpleDict()
simple_dict['name'] = 'Boris'
print(simple_dict['name']) #  Boris  
print(simple_dict['age'])  # Key not found

#==============================================================================================
class BoundedList:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value
        self.__data = []

    def __getitem__(self, index: int):
        return self.__data[index]

    def __setitem__(self, index: int, value: int):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(f"Value {value} must be between {self.min_value} and {self.max_value}")
        if index >= len(self.__data):
            # Додати новий елемент, якщо індекс виходить за межі
            self.__data.append(value)
        else:
            # Замінити існуючий елемент
            self.__data[index] = value

    def __repr__(self):
        return f"BoundedList({self.max_value}, {self.min_value})"

    def __str__(self):
        return str(self.__data)

if __name__ == '__main__':
    temperatures = BoundedList(18, 26)

    for i, el in enumerate([20, 22, 25, 27]):
        try:
            temperatures[i] = el
        except ValueError as e:
            print(e)

    print(temperatures)

"""
Value 27 must be between 18 and 26
[20, 22, 25]
"""

#==============================================================================================
from collections import UserList

class BoundedList(UserList):
    def __init__(self, min_value: int, max_value: int, initial_list=None):
        super().__init__(initial_list if initial_list is not None else [])
        self.min_value = min_value
        self.max_value = max_value
        self.__validate_list()

    def __validate_list(self):
        for item in self.data:
            self.__validate_item(item)

    def __validate_item(self, item):
        if not (self.min_value <= item <= self.max_value):
            raise ValueError(f"Item {item} must be between {self.min_value} and {self.max_value}")

    def append(self, item):
        self.__validate_item(item)
        super().append(item)

    def insert(self, i, item):
        self.__validate_item(item)
        super().insert(i, item)

    def __setitem__(self, i, item):
        self.__validate_item(item)
        super().__setitem__(i, item)

    def __repr__(self):
        return f"BoundedList({self.max_value}, {self.min_value})"

    def __str__(self):
        return str(self.data)

if __name__ == '__main__':
    temperatures = BoundedList(18, 26, [19, 21, 22])
    print(temperatures)

    for el in [20, 22, 25, 27]:
        try:
            temperatures.append(el)
        except ValueError as e:
            print(e)

    print(temperatures)

"""
[19, 21, 22]
Item 27 must be between 18 and 26
[19, 21, 22, 20, 22, 25]
"""
#==============================================================================================
def __getitem__(self, index):
        # Додати спеціальну логіку тут, наприклад, логування або перевірку
        print(f"Accessing item at index {index}")
        # Викликати оригінальний метод __getitem__
        return super().__getitem__(index)  

#==============================================================================================