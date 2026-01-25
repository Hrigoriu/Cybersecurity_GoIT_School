"""
    ! Гетери (від англ. get - отримувати) ! @property !
* Це методи, які дозволяють отримати значення поля. 
Вони використовуються, коли доступ до поля потребує якоїсь додаткової обробки або коли безпосередній доступ до поля не бажаний з міркувань інкапсуляції. 
* Наприклад, якщо потрібно завжди повертати значення поля у вигляді рядка, навіть якщо воно зберігається як число.
Вони використовуються для отримання значення поля і можуть виконувати додаткову обробку цього значення перед поверненням його користувачеві

Вбудований декоратор @property в Python дозволяє легко створювати гетери. 
Використання цього декоратора робить метод класу доступним як поле, тобто його можна буде викликати без дужок. 
"""
#==============================================================================================
"""
    ! Сетери (від англ. set - встановлювати) ! @property.setter !
* Це методи, які дозволяють встановити значення поля. 
Вони найчастіше використовуються для валідації даних, які намагаються присвоїти полю. 
* Наприклад, якщо ми маємо поле, яке повинно приймати значення лише додатні числа, можна в сетері додати перевірку, яка буде викидати виняток або повертати помилку, якщо намагатися присвоїти йому від'ємне число.
Вони використовуються для встановлення значення поля і часто використовуються для валідації даних перед призначенням їх полю.

Для створення сетера для того ж поля, що і гетер, використовується декоратор @property.setter, який застосовується до методу з тим же ім'ям, що і властивість.
"""
#==============================================================================================
class Person:
    def __init__(self, age):
        self.__age = age  # Пряме присвоєння значення атрибуту в конструкторі

    @property
    def age(self):
        return self.__age  # Геттер повертає значення приватного поля

    @age.setter
    def age(self, value):
        if value < 0:
            # Валідація вхідного значення
            raise ValueError("Вік не може бути від'ємним")  
        # Присвоєння валідного значення приватному полю
        self.__age = value  

if __name__ == "__main__":
    person = Person(10)
    print(person.age)
    person.age = -5

"""
10
Traceback (most recent call last):
  File "d:\IT school\Projects\Projects_GoIT\Cybersecurity\test.py", line 39, in <module>
    person.age = -5
    ^^^^^^^^^^
  File "d:\IT school\Projects\Projects_GoIT\Cybersecurity\test.py", line 32, in age
    raise ValueError("Вік не може бути від'ємним")
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: Вік не може бути від'ємним
"""
#==============================================================================================
class Person:
    def __init__(self, age):
        # Спочатку встановлюємо __age як None
        self.__age = None
        # Використовуємо сеттер для встановлення віку, що дозволяє валідацію вхідного значення
        self.age = age

    @property
    def age(self):
        # Геттер повертає значення приватного поля
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            # Валідація вхідного значення
            raise ValueError("Вік не може бути від'ємним")
        # Присвоєння валідного значення приватному полю
        self.__age = value

if __name__ == "__main__":
    person = Person(-10)
    print(person.age)

"""
Traceback (most recent call last):
  File "d:\IT school\Projects\Projects_GoIT\Cybersecurity\test.py", line 74, in <module>
    person = Person(-10)
             ^^^^^^^^^^^
  File "d:\IT school\Projects\Projects_GoIT\Cybersecurity\test.py", line 58, in __init__
    self.age = age
    ^^^^^^^^
  File "d:\IT school\Projects\Projects_GoIT\Cybersecurity\test.py", line 69, in age
    raise ValueError("Вік не може бути від'ємним")
ValueError: Вік не може бути від'ємним
"""
#==============================================================================================
class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = None
        self.__is_admin = None
        self._is_active = is_active
        self.__is_admin = is_admin

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self._is_active = value

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = value

    def greeting(self):
        return f"Hi {self.name}"

if __name__ == "__main__":
    p = Person("Boris", 34, True, False)
    print(p.is_admin)  # Використовуємо геттер
    p.is_admin = True  # Використовуємо сеттер
    print(p.is_admin)  # Використовуємо геттер знову

"""
False
True
"""
#==============================================================================================


