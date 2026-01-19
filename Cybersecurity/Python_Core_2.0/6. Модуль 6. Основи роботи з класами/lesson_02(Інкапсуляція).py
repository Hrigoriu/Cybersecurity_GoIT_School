"""
ООП має чотири основні концепції, які відрізняють його від інших методологій програмування:

Абстракція
Інкапсуляція
Наслідування
Поліморфізм

Абстракція - це модель якогось об'єкта або явища з реального світу, що відкидає незначні деталі, які не грають істотну роль в контексті розгляду концепції ООП.
"""
#================================================================================================
"""
        ! Інкапсуляція !
Полягає в приховуванні внутрішньої структури класу та захисті його даних від прямого доступу ззовні. 
Цей принцип дозволяє обмежити доступ до певних компонентів класу (полів і методів), забезпечуючи контроль над тим, як ці дані використовуються та змінюються.
"""
#================================================================================================
"""
За допомогою атрибутів та методів класу ми виконуємо інкапсуляцію — приховуємо деталі реалізації під інтерфейсом класу.
"""
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greeting(self) -> str:
        return f"Hi {self.name}"

p = Person("Boris", 34)
print(p.greeting())  # Hi Boris
#================================================================================================
"""
Інкапсуляція в ООП реалізується через використання публічних (public), захищених (protected) і приватних (private) атрибутів та методів.

Public -    елемент доступний з будь-якого місця в програмі.
Protected - елемент доступний з класу, в якому він оголошений, а також з класів-похідних.
Private -   елемент доступний лише з класу, в якому він оголошений.
"""
#================================================================================================
"""
    ! Захищені (Protected) атрибути та методи. !

Вони позначаються одним підкресленням _ на початку імені. 
Це лише конвенція, і захищені атрибути все ще можуть бути доступні ззовні, але це вважається поганою практикою змінювати їх ззовні.
"""
#================================================================================================
class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active

    def greeting(self):
        return f"Hi {self.name}"

p = Person("Boris", 34, True)
print(p.name, p.age, p._is_active)  # Boris 34 True
print(p.greeting())                 # Hi Boris

#================================================================================================
class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active

    def greeting(self):
        return f"Hi {self.name}"
    
    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

p = Person("Boris", 34, True)
print(p.name, p.age, p.is_active()) # Boris 34 True
print(p.greeting())                 # Hi Boris

#================================================================================================
class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active

    def greeting(self):
        return f"Hi {self.name}"
    
    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

p = Person("Boris", 34, True)       
print(p.name, p.age, p.is_active()) # Boris 34 True
print(p.greeting())                 # Hi Boris
p.set_active(False)
print(p.is_active())                # False 
#================================================================================================
"""
    ! Приватні (Private) атрибути та методи !
    
Атрибути, що вважаються приватними позначаються двома підкресленнями __ і не можуть бути доступні безпосередньо ззовні класу.
"""
#================================================================================================
class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

p = Person("Boris", 34, True, False)
print(p.__is_admin)  # AttributeError: 'Person' object has no attribute '__is_admin'

#================================================================================================
class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

p = Person("Boris", 34, True, False)
print(p._Person__is_admin)  # False
"""
отримати доступ до поля __is_admin можливо через вираз p._Person__is_admin
"""

#================================================================================================
class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

    def get_is_admin(self):
        return self.__is_admin

    def set_is_admin(self, is_admin: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = is_admin

        
p = Person("Boris", 34, True, False)
print(p.get_is_admin())  # False
p.set_is_admin(True)
print(p.get_is_admin())  # True
"""
У цьому прикладі, метод get_is_admin дозволяє отримати значення поля __is_admin, 
а метод set_is_admin дозволяє його змінити.
"""
