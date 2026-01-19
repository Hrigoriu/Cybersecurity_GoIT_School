# 1. Створюємо клас (креслення або інструкцію) з назвою Animal
class Animal:
    # Ключове слово pass використовується, коли синтаксично блок коду необхідний,
    # але ми поки що не хочемо нічого виконувати (порожній клас).
    pass 

# 2. Створюємо екземпляр (конкретний об'єкт) класу Animal
# Дужки () означають, що ми "викликаємо" клас, щоб створити новий об'єкт.
animal = Animal()

# Перевірка (не обов'язково для завдання, але корисно бачити):
print(f"Ми створили змінну animal, яка є: {animal}")
print(f"Чи є це екземпляром Animal? {isinstance(animal, Animal)}")
#======================================================================================
class Animal:
    # Конструктор (__init__) - це метод, який запускається автоматично при створенні нового об'єкта.
    # self вказує на конкретний об'єкт, який ми створюємо.
    def __init__(self, nickname, weight):
        self.nickname = nickname  # Зберігаємо кличку у "пам'яті" конкретного об'єкта
        self.weight = weight      # Зберігаємо вагу

    # Метод класу - це дія, яку може виконувати об'єкт.
    def say(self):
        pass  # Поки що дія не визначена (порожня)

# Створюємо екземпляр класу, передаючи аргументи для конструктора (кличку та вагу)
animal = Animal("Simon", 10)

# Перевірка (не обов'язково, але для наочності):
print(f"Тварина: {animal.nickname}, Вага: {animal.weight}")

#======================================================================================
class Animal:
    # Конструктор (__init__) - це метод, який запускається автоматично при створенні нового об'єкта.
    # self вказує на конкретний об'єкт, який ми створюємо.
    def __init__(self, nickname, weight):
        self.nickname = nickname  # Зберігаємо кличку у "пам'яті" конкретного об'єкта
        self.weight = weight      # Зберігаємо вагу

    # Метод класу - це дія, яку може виконувати об'єкт.
    def say(self):
        pass  # Поки що дія не визначена (порожня)

    # Метод для зміни ваги тварини
    def change_weight(self, new_weight):
        self.weight = new_weight

# Створюємо екземпляр класу, передаючи аргументи для конструктора (кличку та вагу)
animal = Animal("Simon", 10)

# Змінюємо вагу з 10 на 12
animal.change_weight(12)

# Перевірка (не обов'язково, але для наочності):
print(f"Тварина: {animal.nickname}, Вага: {animal.weight}")

#======================================================================================
class Animal:
    # Змінна класу - спільна для всіх об'єктів цього класу
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname  # Змінна екземпляра
        self.weight = weight      # Змінна екземпляра

    def say(self):
        pass

    def change_weight(self, new_weight):
        self.weight = new_weight

    # Метод для зміни кольору (змінної класу)
    def change_color(self, color):
        Animal.color = color  # Змінюємо колір для ВСЬОГО класу Animal

# Створюємо екземпляри об'єкта
first_animal = Animal("Simon", 10)
second_animal = Animal("Rex", 20)

# Викликаємо функцію change_color для одного екземпляра
first_animal.change_color("red")

# Перевірка:
print(f"First animal color: {first_animal.color}")   # Виведе red
print(f"Second animal color: {second_animal.color}") # Також виведе red, бо змінилася змінна класу

#======================================================================================
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

# Створюємо клас Cat, який є спадкоємцем (дочірнім класом) від Animal
class Cat(Animal):
    # Перевизначаємо метод say. Це і є поліморфізм:
    # метод називається так само, але поводиться інакше для котів.
    def say(self):
        return "Meow"

# Створюємо екземпляр класу Cat
cat = Cat("Simon", 10)

# Перевірка (не обов'язково, але для наочності):
print(f"Кіт: {cat.nickname}, Вага: {cat.weight}")
print(f"Голос: {cat.say()}")

#======================================================================================
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

# Створюємо клас Cat, який є спадкоємцем (дочірнім класом) від Animal
class Cat(Animal):
    # Перевизначаємо метод say. Це і є поліморфізм:
    # метод називається так само, але поводиться інакше для котів.
    def say(self):
        return "Meow"

# Створюємо клас Dog, який також успадковується від Animal
class Dog(Animal):
    def __init__(self, nickname, weight, breed):
        # super().__init__ викликає конструктор батьківського класу Animal,
        # щоб ми не писали знову self.nickname = nickname
        super().__init__(nickname, weight)
        self.breed = breed  # Додаємо нову властивість, якої немає у звичайного Animal

    def say(self):
        return "Woof"

# Створюємо екземпляр класу Cat
cat = Cat("Simon", 10)

# Створюємо екземпляр класу Dog
dog = Dog("Barbos", 23, "labrador")

# Перевірка (не обов'язково, але для наочності):
print(f"Кіт: {cat.nickname}, Вага: {cat.weight}, Голос: {cat.say()}")
print(f"Пес: {dog.nickname}, Вага: {dog.weight}, Порода: {dog.breed}, Голос: {dog.say()}")

#======================================================================================
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

class Owner:
    # 1. Створюємо конструктор для власника з ім'ям, віком та адресою
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    # 2. Метод, що повертає "візитівку" власника у вигляді словника
    def info(self):
        return {'name': self.name, 'age': self.age, 'address': self.address}

# Створюємо клас Cat (залишаємо без змін з минулого завдання)
class Cat(Animal):
    def say(self):
        return "Meow"

class Dog(Animal):
    # 3. Додаємо owner в аргументи конструктора
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner  # Зберігаємо власника всередині об'єкта собаки
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    # 4. Метод, щоб дізнатися інформацію про власника собаки
    def who_is_owner(self):
        return self.owner.info()

# --- Приклад використання ---

# Створюємо екземпляр власника
owner = Owner("Ivan", 25, "Kyiv")

# Створюємо собаку і передаємо їй цього власника
dog = Dog("Barbos", 23, "labrador", owner)

# Перевірка:
print(f"Пес: {dog.nickname}, Порода: {dog.breed}")
print(f"Власник собаки: {dog.who_is_owner()}") 
# Виведе: {'name': 'Ivan', 'age': 25, 'address': 'Kyiv'}

#======================================================================================
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

class Cat(Animal):
    def say(self):
        return "Meow"

class Dog(Animal):
    def say(self):
        return "Woof"

# Створюємо клас CatDog, що наслідується від Cat та Dog.
# Першим йде Cat, тому метод say() візьметься саме від кота.
class CatDog(Cat, Dog):
    def info(self):
        return f"{self.nickname}-{self.weight}"

# Створюємо клас DogCat, що наслідується від Dog та Cat.
# Першим йде Dog, тому метод say() візьметься саме від собаки.
class DogCat(Dog, Cat):
    def info(self):
        return f"{self.nickname}-{self.weight}"

# --- Перевірка ---

# Створюємо диво-звірів
cat_dog = CatDog("Kotopes", 15)
dog_cat = DogCat("Pesokot", 20)

# Перевіряємо, як вони говорять (поліморфізм + порядок спадкування MRO)
print(f"CatDog каже: {cat_dog.say()}")  # Виведе "Meow"
print(f"DogCat каже: {dog_cat.say()}")  # Виведе "Woof"

# Перевіряємо метод info
print(f"Info CatDog: {cat_dog.info()}")
print(f"Info DogCat: {dog_cat.info()}")

#======================================================================================
from collections import UserDict

class LookUpKeyDict(UserDict):
    # Додаємо метод для пошуку ключів за значенням
    def lookup_key(self, value):
        keys = []
        # У класі UserDict всі дані зберігаються в атрибуті self.data
        # Ми перебираємо ключі нашого словника
        for key in self.data:
            # Якщо значення за цим ключем співпадає з тим, що ми шукаємо (value)
            if self.data[key] == value:
                keys.append(key)
        return keys

# --- Перевірка роботи ---
# Створюємо наш словник
my_dict = LookUpKeyDict({'a': 1, 'b': 2, 'c': 1, 'd': 3})

# Шукаємо ключі, де значення дорівнює 1
found_keys = my_dict.lookup_key(1)

print(f"Словник: {my_dict}")
print(f"Ключі зі значенням 1: {found_keys}") # Має вивести ['a', 'c']

#======================================================================================
from collections import UserList

class AmountPaymentList(UserList):
    # Метод для розрахунку суми платежів (враховуються лише борги > 0)
    def amount_payment(self):
        total_sum = 0
        # Оскільки ми успадкували UserList, self поводиться як звичайний список.
        # Ми можемо перебирати елементи прямо з self.
        for value in self:
            if value > 0:
                total_sum = total_sum + value
        return total_sum

# --- Перевірка роботи ---
# Створюємо список: 50 (борг), -10 (переплата), 100 (борг)
my_payments = AmountPaymentList([50, -10, 100])

# Викликаємо наш метод
total_debt = my_payments.amount_payment()

print(f"Платежі: {my_payments}")
print(f"Сума до сплати: {total_debt}") # Має вивести 150

#======================================================================================
from collections import UserString

class NumberString(UserString):
    # Метод для підрахунку кількості цифр у рядку
    def number_count(self):
        count = 0
        # self у класі UserString поводиться як звичайний рядок
        for char in self:
            # Перевіряємо, чи є символ цифрою (0-9)
            if char.isdigit():
                count += 1
        return count

# --- Перевірка роботи ---
# Створюємо наш "розумний" рядок з текстом і цифрами
my_string = NumberString("Python 3.12 is great! 100%")

# Викликаємо метод підрахунку
digits = my_string.number_count()

print(f"Рядок: '{my_string}'")
print(f"Кількість цифр: {digits}") 
# Очікуємо 6 цифр (3, 1, 2, 1, 0, 0)    
#======================================================================================
# 1. Створюємо власний клас винятку (помилки)
# Він успадковується від стандартного класу Exception
class IDException(Exception):
    pass

# 2. Функція для додавання ID до списку
def add_id(id_list, employee_id):
    # Перевіряємо, чи починається ID з '01'
    if not employee_id.startswith('01'):
        # Якщо ні - "підіймаємо" (raise) нашу власну помилку
        raise IDException(f"ID '{employee_id}' не починається з '01'")
    
    # Якщо все добре, додаємо ID до списку
    id_list.append(employee_id)
    
    # Повертаємо оновлений список
    return id_list

# --- Перевірка роботи (Example Usage) ---

ids = []

try:
    # Спробуємо додати правильний ID
    add_id(ids, '01001')
    print(f"Список після успішного додавання: {ids}")
    
    # Спробуємо додати неправильний ID
    add_id(ids, '12345') # Тут виникне помилка

except IDException as e:
    # Цей блок спрацює, якщо виникне помилка IDException
    print(f"Спіймали помилку: {e}")

print(f"Фінальний список: {ids}")

#======================================================================================
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

class Cat(Animal):
    def say(self):
        return "Meow"

# Цей клас НЕ успадковується від Animal або Cat,
# але він повністю копіює їхню поведінку (інтерфейс).
class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    # Реалізуємо метод say, як у кота, щоб "вдати", що це кіт
    def say(self):
        return "Meow"

    # Реалізуємо метод зміни ваги, як у Animal
    def change_weight(self, weight):
        self.weight = weight

# --- Перевірка роботи ---

# Створюємо справжнього кота
real_cat = Cat("Simon", 10)

# Створюємо CatDog, який прикидається котом
fake_cat = CatDog("Chupakabra", 15)

# Перевірка:
print(f"Справжній кіт каже: {real_cat.say()}")
print(f"CatDog каже: {fake_cat.say()}")

# Змінюємо вагу
fake_cat.change_weight(20)
print(f"Нова вага CatDog: {fake_cat.weight}")

# Доказ того, що вони різні типи, але працюють однаково
print(f"Тип real_cat: {type(real_cat)}")
print(f"Тип fake_cat: {type(fake_cat)}")

#======================================================================================
class Contacts:
    # Змінна класу, яка зберігає поточний номер для наступного контакту.
    # Вона спільна для всіх екземплярів, але ми будемо використовувати її
    # для генерації унікальних ID.
    current_id = 1

    def __init__(self):
        # При створенні нової книжки контактів, список спочатку порожній
        self.contacts = []

    def list_contacts(self):
        # Повертаємо весь список контактів
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        # Створюємо словник з даними нового контакту
        new_contact = {
            "id": Contacts.current_id, # Беремо поточний номер з лічильника класу
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite,
        }
        
        # Додаємо створений контакт у наш список
        self.contacts.append(new_contact)
        
        # Збільшуємо лічильник на 1, щоб наступний контакт отримав наступний номер
        Contacts.current_id += 1
        
#======================================================================================
class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        new_contact = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite
        }
        self.contacts.append(new_contact)
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        # Перебираємо кожен контакт у нашому списку
        for contact in self.contacts:
            # Якщо ID контакту збігається з тим, що ми шукаємо
            if contact["id"] == id:
                return contact
        # Якщо пройшли весь список і нічого не знайшли, повертаємо None
        return None
    
#======================================================================================
class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        # Проходимо по всьому списку контактів
        for contact in self.contacts:
            # Якщо знайшли контакт із потрібним id
            if contact["id"] == id:
                # Видаляємо цей словник зі списку
                self.contacts.remove(contact)
                # Перериваємо цикл, бо контакт знайдено і видалено
                return
#======================================================================================

#======================================================================================

#======================================================================================

#======================================================================================

#======================================================================================

#======================================================================================

#======================================================================================