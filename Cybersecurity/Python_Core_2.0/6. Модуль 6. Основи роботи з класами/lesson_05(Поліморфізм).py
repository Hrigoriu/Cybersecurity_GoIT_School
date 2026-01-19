"""
    ! Поліморфізм ! 
Від грецьких слів "polys" (багато) та "morph" (форма). 
Це один із ключових концептів ООП, який дозволяє об'єктам мати різні форми або поведінку, базуючись на їх типах.
Це здатність різних класів використовувати методи з однаковою назвою, але з різною реалізацією. Це дозволяє використовувати один інтерфейс для різних типів даних.
"""
#================================================================================================
class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Dog(Animal):
    def make_sound(self):
        return "Woof"

def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())

animals = [Cat("Simon", 4), Dog("Rex", 5)]
animal_sounds(animals)
# Meow
# Woof
#================================================================================================
"""
    ! Качина типізація (Duck Typing) !
Це означає, що замість перевірки типу об'єкта перед його використанням, важливіше зосередитися на тому, чи має об'єкт потрібні методи чи властивості, які вимагаються для виконання певної функції або операції.
Головне, щоб атрибут називався так само і приймав ті самі аргументи (якщо це метод).
"""
#================================================================================================
"""
Назва терміна походить від англійського «duck test» («качиний тест»), який в оригіналі звучить так:
«If it looks like a duck, swims like a duck and quacks like a duck, then it probably is a duck».
(«Якщо воно виглядає як качка, плаває як качка і кахкає як качка, то це напевно і є качка»).
"""
#================================================================================================
class Duck:
    def quack(self):
        print("Quack, quack!")

class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")

def make_it_quack(duck):
    duck.quack()

duck = Duck()
person = Person()

make_it_quack(duck)     # Quack, quack!
make_it_quack(person)   # I'm Quacking Like a Duck!

#================================================================================================
class Dog:
    def speak(self) -> str:
        return "Woof"

class Cat:
    def speak(self) -> str:
        return "Meow"

class Robot:
    def speak(self) -> str:
        return "Beep boop"

def make_it_speak(speaker) -> None:
    print(speaker.speak())

dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop

#================================================================================================
from typing import Protocol

class Speaker(Protocol):
    def speak(self) -> str:
        pass

class Dog:
    def speak(self) -> str:
        return "Woof"

class Cat:
    def speak(self) -> str:
        return "Meow"

class Robot:
    def speak(self) -> str:
        return "Beep boop"

def make_it_speak(speaker: Speaker) -> None:
    print(speaker.speak())

dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop
