"""
☝      !@dataclass!      ☝

Використання @dataclass дозволяє зменшити кількість коду, необхідного для створення класів, які в основному зберігають дані. 
Це робить код більш читабельним і легшим для розуміння, а також автоматично створює конструктор класу __init__.
"""
#================================================================================================
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
# Старий варіант
#================================================================================================
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
# Новий варіант
#================================================================================================
@dataclass
class Article:
    title: str
    author: str
    views: int = 0

#================================================================================================
from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height

rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)
rect3 = Rectangle(8, 6)

print(f"Площа прямокутника 1: {rect1.area()}")
print(f"Площа прямокутника 2: {rect2.area()}")
print(f"Площа прямокутника 3: {rect3.area()}")
"""
Площа прямокутника 1: 50
Площа прямокутника 2: 21
Площа прямокутника 3: 48
"""
