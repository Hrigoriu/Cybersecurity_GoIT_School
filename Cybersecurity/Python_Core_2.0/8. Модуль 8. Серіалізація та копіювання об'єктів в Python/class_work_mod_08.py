import pickle

def write_contacts_to_file(filename, contacts):
    """
    Серіалізує список контактів та записує його у бінарний файл.
    
    :param filename: Ім'я файлу для запису.
    :param contacts: Список словників з контактами.
    """
    # Використовуємо режим 'wb' (write binary), бо pickle працює з байтами
    with open(filename, 'wb') as file:
        pickle.dump(contacts, file)


def read_contacts_from_file(filename):
    """
    Читає та десеріалізує список контактів з бінарного файлу.
    
    :param filename: Ім'я файлу для читання.
    :return: Список контактів.
    """
    try:
        # Використовуємо режим 'rb' (read binary)
        with open(filename, 'rb') as file:
            contacts = pickle.load(file)
        return contacts
    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено.")
        return []
    except pickle.UnpicklingError:
        print("Помилка: Не вдалося відновити дані (файл пошкоджено або не є pickle-файлом).")
        return []

# --- Блок перевірки ---
if __name__ == "__main__":
    # 1. Створюємо тестовий список контактів
    my_contacts = [
        {
            "name": "Allen Raymond",
            "email": "nulla.ante@vestibul.co.uk",
            "phone": "(992) 914-3792",
            "favorite": False,
        },
        {
            "name": "Chaim Lewis",
            "email": "dui.in@egetlacus.ca",
            "phone": "(294) 840-6685",
            "favorite": False,
        }
    ]

    file_name = "data.bin"

    # 2. Записуємо дані у файл
    print(f"Записуємо контакти у файл '{file_name}'...")
    write_contacts_to_file(file_name, my_contacts)

    # 3. Читаємо дані з файлу
    print(f"Читаємо контакти з файлу '{file_name}'...")
    restored_contacts = read_contacts_from_file(file_name)

    # 4. Перевіряємо результат
    print("\nВідновлені дані:")
    for contact in restored_contacts:
        print(contact)
        
    # Перевірка на ідентичність
    print(f"\nДані ідентичні? {my_contacts == restored_contacts}")
#====================================================================================================
import json

def write_contacts_to_file(filename, contacts):
    """
    Серіалізує список контактів у JSON файл.
    Дані зберігаються у структурі словник {"contacts": [список]}.
    
    :param filename: Ім'я файлу для запису.
    :param contacts: Список словників з контактами.
    """
    # Створюємо необхідну структуру згідно з ТЗ
    data = {"contacts": contacts}
    
    # Відкриваємо файл у текстовому режимі ('w') з кодуванням utf-8
    with open(filename, 'w', encoding='utf-8') as file:
        # indent=4 додає відступи для читабельності людиною
        json.dump(data, file, indent=4)


def read_contacts_from_file(filename):
    """
    Читає та десеріалізує список контактів з JSON файлу.
    
    :param filename: Ім'я файлу для читання.
    :return: Список контактів або порожній список у разі помилки.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # Повертаємо список, що лежить за ключем "contacts"
            return data.get("contacts", [])
            
    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено.")
        return []
    except json.JSONDecodeError:
        print("Помилка: Не вдалося декодувати JSON (файл пошкоджено).")
        return []


# --- Блок перевірки ---
if __name__ == "__main__":
    # 1. Тестові дані
    my_contacts = [
        {
            "name": "Allen Raymond",
            "email": "nulla.ante@vestibul.co.uk",
            "phone": "(992) 914-3792",
            "favorite": False,
        },
        {
            "name": "Chaim Lewis",
            "email": "dui.in@egetlacus.ca",
            "phone": "(294) 840-6685",
            "favorite": False,
        }
    ]

    file_name = "contacts.json"

    # 2. Запис
    print(f"Записуємо контакти у JSON файл '{file_name}'...")
    write_contacts_to_file(file_name, my_contacts)

    # 3. Читання
    print(f"Читаємо контакти з файлу '{file_name}'...")
    restored_contacts = read_contacts_from_file(file_name)

    # 4. Перевірка
    print("\nВідновлені дані:")
    for contact in restored_contacts:
        print(contact)
        
    print(f"\nДані ідентичні? {my_contacts == restored_contacts}")

#====================================================================================================
import csv

def write_contacts_to_file(filename, contacts):
    """
    Серіалізує список контактів у CSV файл.
    
    :param filename: Ім'я файлу для запису.
    :param contacts: Список словників з контактами.
    """
    # Якщо список порожній, нічого не робимо або створюємо порожній файл з заголовками
    if not contacts:
        return

    # Відкриваємо файл у режимі запису ('w').
    # newline='' важливий для csv модуля, щоб уникнути зайвих порожніх рядків у Windows
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        # Визначаємо заголовки (ключі словника)
        fieldnames = ["name", "email", "phone", "favorite"]
        
        # Створюємо об'єкт writer
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Записуємо заголовки (перший рядок)
        writer.writeheader()
        
        # Записуємо всі рядки даних
        writer.writerows(contacts)


def read_contacts_from_file(filename):
    """
    Читає контакти з CSV файлу та перетворює дані у відповідні типи.
    
    :param filename: Ім'я файлу для читання.
    :return: Список контактів.
    """
    contacts = []
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Важливий момент: CSV зберігає все як рядки.
                # Нам потрібно вручну перетворити рядок 'True'/'False' назад у булеве значення.
                if "favorite" in row:
                    # Якщо рядок дорівнює "True", отримаємо True, інакше False
                    row["favorite"] = row["favorite"] == "True"
                
                contacts.append(row)
                
    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено.")
        return []
    
    return contacts


# --- Блок перевірки ---
if __name__ == "__main__":
    # 1. Тестові дані
    my_contacts = [
        {
            "name": "Allen Raymond",
            "email": "nulla.ante@vestibul.co.uk",
            "phone": "(992) 914-3792",
            "favorite": False,
        },
        {
            "name": "Chaim Lewis",
            "email": "dui.in@egetlacus.ca",
            "phone": "(294) 840-6685",
            "favorite": False,
        },
        {
            "name": "Kennedy Lane",
            "email": "mattis.Cras@nonenimMauris.net",
            "phone": "(542) 451-7038",
            "favorite": True,
        }
    ]

    file_name = "contacts.csv"

    # 2. Запис
    print(f"Записуємо контакти у CSV файл '{file_name}'...")
    write_contacts_to_file(file_name, my_contacts)

    # 3. Читання
    print(f"Читаємо контакти з файлу '{file_name}'...")
    restored_contacts = read_contacts_from_file(file_name)

    # 4. Перевірка
    print("\nВідновлені дані:")
    for contact in restored_contacts:
        print(contact)
        
    # Перевірка типів даних (чи відновився bool)
    print(f"\nТип поля 'favorite' першого елемента: {type(restored_contacts[0]['favorite'])}")
    print(f"Дані ідентичні? {my_contacts == restored_contacts}")

#====================================================================================================
import pickle

class Person:
    """
    Клас, що представляє інформацію про окрему особу.
    """
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __str__(self):
        return f"{self.name} ({self.email}, {self.phone}, Favorite: {self.favorite})"


class Contacts:
    """
    Клас-контейнер для списку контактів (екземплярів Person).
    Має методи для збереження себе у файл та зчитування з файлу.
    """
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts

    def save_to_file(self):
        """
        Зберігає поточний екземпляр класу Contacts у файл за допомогою pickle.
        """
        with open(self.filename, 'wb') as file:
            # Зберігаємо весь об'єкт 'self' (включно зі списком контактів та ім'ям файлу)
            pickle.dump(self, file)

    def read_from_file(self):
        """
        Зчитує екземпляр класу Contacts з файлу.
        
        :return: Завантажений об'єкт класу Contacts.
        """
        try:
            with open(self.filename, 'rb') as file:
                # Відновлюємо об'єкт
                content = pickle.load(file)
            return content
        except FileNotFoundError:
            print(f"Помилка: Файл {self.filename} не знайдено.")
            return None
        except pickle.UnpicklingError:
            print("Помилка: Не вдалося відновити дані.")
            return None


# --- Блок перевірки ---
if __name__ == "__main__":
    # 1. Створюємо список контактів
    contacts_list = [
        Person(
            "Allen Raymond",
            "nulla.ante@vestibul.co.uk",
            "(992) 914-3792",
            False,
        ),
        Person(
            "Chaim Lewis",
            "dui.in@egetlacus.ca",
            "(294) 840-6685",
            False,
        ),
    ]

    # 2. Створюємо об'єкт Contacts
    persons = Contacts("user_class.dat", contacts_list)

    # 3. Зберігаємо об'єкт у файл
    print("Зберігаємо об'єкт Contacts у файл...")
    persons.save_to_file()

    # 4. Відновлюємо об'єкт з файлу
    print("Зчитуємо об'єкт з файлу...")
    # Зверніть увагу: ми викликаємо метод на старому об'єкті, щоб отримати новий
    person_from_file = persons.read_from_file()

    # 5. Перевірка результатів
    print("\nРезультати перевірки:")
    
    # Це різні об'єкти в пам'яті, тому False
    print(f"Чи це той самий об'єкт у пам'яті? {persons is person_from_file}") 
    
    # Перевіряємо дані всередині
    if person_from_file:
        first_original = persons.contacts[0]
        first_restored = person_from_file.contacts[0]
        
        print(f"Ім'я співпадає? {first_original.name == first_restored.name}")
        print(f"Email співпадає? {first_original.email == first_restored.email}")
        
        print("\nВідновлені контакти:")
        for p in person_from_file.contacts:
            print(p)

#====================================================================================================
import pickle

class Person:
    """
    Клас, що представляє інформацію про окрему особу.
    """
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __str__(self):
        return f"{self.name} ({self.email}, {self.phone}, Favorite: {self.favorite})"


class Contacts:
    """
    Клас-контейнер для списку контактів (екземплярів Person).
    Має методи для збереження себе у файл та зчитування з файлу.
    """
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0  # Лічильник збережень

    def save_to_file(self):
        """
        Зберігає поточний екземпляр класу Contacts у файл за допомогою pickle.
        """
        with open(self.filename, 'wb') as file:
            # Зберігаємо весь об'єкт 'self' (включно зі списком контактів та ім'ям файлу)
            pickle.dump(self, file)

    def read_from_file(self):
        """
        Зчитує екземпляр класу Contacts з файлу.
        
        :return: Завантажений об'єкт класу Contacts.
        """
        try:
            with open(self.filename, 'rb') as file:
                # Відновлюємо об'єкт
                content = pickle.load(file)
            return content
        except FileNotFoundError:
            print(f"Помилка: Файл {self.filename} не знайдено.")
            return None
        except pickle.UnpicklingError:
            print("Помилка: Не вдалося відновити дані.")
            return None

    def __getstate__(self):
        """
        Магічний метод, який викликається модулем pickle перед збереженням об'єкта.
        Ми використовуємо його, щоб збільшити лічильник збережень у серіалізованих даних.
        """
        # Копіюємо поточний стан об'єкта (щоб не змінювати оригінал у пам'яті)
        attributes = self.__dict__.copy()
        # Збільшуємо лічильник на 1 для збереженої версії
        attributes['count_save'] += 1
        return attributes


# --- Блок перевірки ---
if __name__ == "__main__":
    # 1. Створюємо список контактів
    contacts_list = [
        Person(
            "Allen Raymond",
            "nulla.ante@vestibul.co.uk",
            "(992) 914-3792",
            False,
        ),
        Person(
            "Chaim Lewis",
            "dui.in@egetlacus.ca",
            "(294) 840-6685",
            False,
        ),
    ]

    # 2. Створюємо об'єкт Contacts
    persons = Contacts("user_class.dat", contacts_list)

    # 3. Демонстрація роботи лічильника збережень (__getstate__)
    print("Зберігаємо об'єкт persons...")
    persons.save_to_file()
    
    first = persons.read_from_file()
    print("Зчитали first. Зберігаємо first...")
    first.save_to_file()
    
    second = first.read_from_file()
    print("Зчитали second. Зберігаємо second...")
    second.save_to_file()
    
    third = second.read_from_file()
    print("Зчитали third.")

    # 4. Перевірка значень лічильника
    print(f"\npersons.count_save: {persons.count_save}")  # Має бути 0
    print(f"first.count_save: {first.count_save}")      # Має бути 1
    print(f"second.count_save: {second.count_save}")    # Має бути 2
    print(f"third.count_save: {third.count_save}")      # Має бути 3

#====================================================================================================
import pickle

class Person:
    """
    Клас, що представляє інформацію про окрему особу.
    """
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __str__(self):
        return f"{self.name} ({self.email}, {self.phone}, Favorite: {self.favorite})"


class Contacts:
    """
    Клас-контейнер для списку контактів (екземплярів Person).
    Має методи для збереження себе у файл та зчитування з файлу.
    """
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0  # Лічильник збережень
        self.is_unpacking = False  # Чи розпакований об'єкт

    def save_to_file(self):
        """
        Зберігає поточний екземпляр класу Contacts у файл за допомогою pickle.
        """
        with open(self.filename, 'wb') as file:
            # Зберігаємо весь об'єкт 'self' (включно зі списком контактів та ім'ям файлу)
            pickle.dump(self, file)

    def read_from_file(self):
        """
        Зчитує екземпляр класу Contacts з файлу.
        
        :return: Завантажений об'єкт класу Contacts.
        """
        try:
            with open(self.filename, 'rb') as file:
                # Відновлюємо об'єкт
                content = pickle.load(file)
            return content
        except FileNotFoundError:
            print(f"Помилка: Файл {self.filename} не знайдено.")
            return None
        except pickle.UnpicklingError:
            print("Помилка: Не вдалося відновити дані.")
            return None

    def __getstate__(self):
        """
        Магічний метод, який викликається модулем pickle перед збереженням об'єкта.
        Ми використовуємо його, щоб збільшити лічильник збережень у серіалізованих даних.
        """
        # Копіюємо поточний стан об'єкта (щоб не змінювати оригінал у пам'яті)
        attributes = self.__dict__.copy()
        # Збільшуємо лічильник на 1 для збереженої версії
        attributes['count_save'] += 1
        return attributes

    def __setstate__(self, value):
        """
        Магічний метод, який викликається модулем pickle після відновлення об'єкта.
        Ми використовуємо його, щоб встановити прапорець is_unpacking в True.
        """
        # Відновлюємо стан об'єкта (value - це словник атрибутів, збережений через __getstate__)
        self.__dict__ = value
        # Встановлюємо прапорець, що об'єкт був розпакований
        self.is_unpacking = True


# --- Блок перевірки ---
if __name__ == "__main__":
    # 1. Створюємо список контактів
    contacts_list = [
        Person(
            "Allen Raymond",
            "nulla.ante@vestibul.co.uk",
            "(992) 914-3792",
            False,
        ),
        Person(
            "Chaim Lewis",
            "dui.in@egetlacus.ca",
            "(294) 840-6685",
            False,
        ),
    ]

    # 2. Створюємо об'єкт Contacts
    persons = Contacts("user_class.dat", contacts_list)

    # 3. Демонстрація роботи лічильника збережень (__getstate__) та розпакування (__setstate__)
    print("Зберігаємо об'єкт persons...")
    persons.save_to_file()
    
    first = persons.read_from_file()
    print("Зчитали first. Зберігаємо first...")
    first.save_to_file()
    
    second = first.read_from_file()
    print("Зчитали second. Зберігаємо second...")
    second.save_to_file()
    
    third = second.read_from_file()
    print("Зчитали third.")

    # 4. Перевірка значень лічильника
    print(f"\npersons.count_save: {persons.count_save}")  # Має бути 0
    print(f"first.count_save: {first.count_save}")      # Має бути 1
    print(f"second.count_save: {second.count_save}")    # Має бути 2
    print(f"third.count_save: {third.count_save}")      # Має бути 3

    # 5. Перевірка прапорця розпакування
    print(f"\npersons.is_unpacking: {persons.is_unpacking}")  # Має бути False
    print(f"first.is_unpacking: {first.is_unpacking}")      # Має бути True
    print(f"second.is_unpacking: {second.is_unpacking}")    # Має бути True

#====================================================================================================
import copy

class Person:
    """
    Клас, що представляє інформацію про окрему особу.
    """
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __str__(self):
        return f"{self.name} ({self.email}, {self.phone}, Favorite: {self.favorite})"


def copy_class_person(person):
    """
    Створює поверхневу копію екземпляра класу Person.
    
    :param person: Об'єкт класу Person.
    :return: Новий об'єкт (копія).
    """
    return copy.copy(person)


# --- Блок перевірки ---
if __name__ == "__main__":
    person = Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    )

    # Створюємо копію
    copy_person = copy_class_person(person)

    print(f"Оригінал: {person}")
    print(f"Копія:    {copy_person}")

    # Перевірки з завдання
    print(f"copy_person == person? {copy_person == person}")  # False (це різні об'єкти в пам'яті)
    print(f"copy_person is person? {copy_person is person}")  # False
    print(f"copy_person.name == person.name? {copy_person.name == person.name}")  # True

#====================================================================================================
import copy
import pickle

class Person:
    """
    Клас, що представляє інформацію про окрему особу.
    """
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __str__(self):
        return f"{self.name} ({self.email}, {self.phone}, Favorite: {self.favorite})"


def copy_class_person(person):
    """
    Створює поверхневу копію екземпляра класу Person.
    
    :param person: Об'єкт класу Person.
    :return: Новий об'єкт (копія).
    """
    return copy.copy(person)


class Contacts:
    """
    Клас-контейнер для списку контактів.
    Підтримує серіалізацію через pickle.
    """
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True


def copy_class_contacts(contacts):
    """
    Створює глибоку копію екземпляра класу Contacts.
    Це гарантує, що список контактів та самі контакти також будуть скопійовані,
    а не передані за посиланням.
    
    :param contacts: Об'єкт класу Contacts.
    :return: Новий об'єкт (глибока копія).
    """
    return copy.deepcopy(contacts)


# --- Блок перевірки ---
if __name__ == "__main__":
    # 1. Підготовка даних
    contacts_list = [
        Person(
            "Allen Raymond",
            "nulla.ante@vestibul.co.uk",
            "(992) 914-3792",
            False,
        ),
        Person(
            "Chaim Lewis",
            "dui.in@egetlacus.ca",
            "(294) 840-6685",
            False,
        ),
    ]

    persons = Contacts("user_class.dat", contacts_list)

    # 2. Створення глибокої копії
    new_persons = copy_class_contacts(persons)

    # 3. Зміна даних у копії
    new_persons.contacts[0].name = "Another name"

    # 4. Перевірка незалежності об'єктів
    print(f"Оригінал (перший контакт): {persons.contacts[0].name}")       # Має залишитися "Allen Raymond"
    print(f"Копія    (перший контакт): {new_persons.contacts[0].name}")   # Має стати "Another name"

    print(f"persons is new_persons? {persons is new_persons}") # False
    print(f"persons.contacts is new_persons.contacts? {persons.contacts is new_persons.contacts}") # False

#====================================================================================================
import copy
import pickle

class Person:
    """
    Клас, що представляє інформацію про окрему особу.
    """
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __str__(self):
        return f"{self.name} ({self.email}, {self.phone}, Favorite: {self.favorite})"


def copy_class_person(person):
    """
    Створює поверхневу копію екземпляра класу Person.
    
    :param person: Об'єкт класу Person.
    :return: Новий об'єкт (копія).
    """
    return copy.copy(person)


class Contacts:
    """
    Клас-контейнер для списку контактів.
    Підтримує серіалізацію через pickle.
    """
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True


def copy_class_contacts(contacts):
    """
    Створює глибоку копію екземпляра класу Contacts.
    Це гарантує, що список контактів та самі контакти також будуть скопійовані,
    а не передані за посиланням.
    
    :param contacts: Об'єкт класу Contacts.
    :return: Новий об'єкт (глибока копія).
    """
    return copy.deepcopy(contacts)


# --- Блок перевірки ---
if __name__ == "__main__":
    # Коментуємо код перевірки, щоб уникнути затримок при автоматичному тестуванні
    pass
    # contacts_list = [
    #     Person(
    #         "Allen Raymond",
    #         "nulla.ante@vestibul.co.uk",
    #         "(992) 914-3792",
    #         False,
    #     ),
    #     Person(
    #         "Chaim Lewis",
    #         "dui.in@egetlacus.ca",
    #         "(294) 840-6685",
    #         False,
    #     ),
    # ]

    # persons = Contacts("user_class.dat", contacts_list)

    # # Створення глибокої копії
    # new_persons = copy_class_contacts(persons)

    # # Зміна даних у копії
    # new_persons.contacts[0].name = "Another name"

    # # Перевірка незалежності об'єктів
    # print(f"Оригінал (перший контакт): {persons.contacts[0].name}")
    # print(f"Копія    (перший контакт): {new_persons.contacts[0].name}")

    # print(f"persons is new_persons? {persons is new_persons}")
    # print(f"persons.contacts is new_persons.contacts? {persons.contacts is new_persons.contacts}")

#====================================================================================================
import copy
import pickle

class Person:
    """
    Клас, що представляє інформацію про окрему особу.
    """
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __str__(self):
        return f"{self.name} ({self.email}, {self.phone}, Favorite: {self.favorite})"

    def __copy__(self):
        """
        Реалізація поверхневого копіювання для Person.
        Створює новий об'єкт Person з копіюванням посилань на атрибути.
        Оскільки атрибути (рядки, булеві) є незмінними, це безпечно.
        """
        copy_obj = Person(self.name, self.email, self.phone, self.favorite)
        return copy_obj


class Contacts:
    """
    Клас-контейнер для списку контактів.
    Підтримує серіалізацію через pickle та копіювання.
    """
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        """Зберігає об'єкт у файл."""
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        """Відновлює об'єкт з файлу."""
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        """Викликається перед серіалізацією (pickle)."""
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        """Викликається після десеріалізації (unpickle)."""
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        """
        Реалізація поверхневого копіювання (Shallow Copy).
        
        Що відбувається:
        1. Створюється новий об'єкт Contacts.
        2. Створюється новий список для contacts (copy.copy(self.contacts)).
        3. АЛЕ елементи всередині цього списку (об'єкти Person) залишаються ТИМИ САМИМИ.
           Тобто original.contacts[0] is copy.contacts[0] поверне True.
        """
        # Створюємо новий екземпляр
        new_instance = Contacts(self.filename, copy.copy(self.contacts))
        # Копіюємо інші службові атрибути
        new_instance.is_unpacking = self.is_unpacking
        new_instance.count_save = self.count_save
        return new_instance

    def __deepcopy__(self, memo):
        """
        Реалізація глибокого копіювання (Deep Copy).
        
        Що відбувається:
        1. Створюється новий об'єкт Contacts.
        2. Рекурсивно створюється повна копія списку contacts і ВСІХ об'єктів Person всередині.
        3. Зміни в об'єктах Person у копії НЕ вплинуть на оригінал.
        
        memo - це словник, який використовується copy.deepcopy для відстеження вже скопійованих об'єктів
        (щоб уникнути нескінченної рекурсії при циклічних посиланнях).
        """
        # Глибоке копіювання списку контактів (створює нові об'єкти Person)
        new_contacts = copy.deepcopy(self.contacts, memo)
        
        # Створення нового екземпляра Contacts
        new_instance = Contacts(self.filename, new_contacts)
        
        # Додаємо новий об'єкт в memo, щоб уникнути зациклення
        memo[id(self)] = new_instance
        
        # Копіюємо прості атрибути
        new_instance.is_unpacking = self.is_unpacking
        new_instance.count_save = self.count_save
        
        return new_instance


# --- Блок перевірки ---
if __name__ == "__main__":
    print("--- Підготовка даних ---")
    person1 = Person("Allen Raymond", "allen@example.com", "(992) 914-3792", False)
    person2 = Person("Chaim Lewis", "chaim@example.com", "(294) 840-6685", False)
    
    initial_contacts = [person1, person2]
    original_book = Contacts("user_class.dat", initial_contacts)
    
    print(f"Оригінал: {original_book.contacts[0]}")

    # ---------------------------------------------------------
    print("\n--- Тест 1: Поверхневе копіювання (copy) ---")
    # ---------------------------------------------------------
    shallow_copy_book = copy.copy(original_book)
    
    print(f"Це різні об'єкти Contacts? -> {original_book is not shallow_copy_book}")
    print(f"Це різні списки контактів? -> {original_book.contacts is not shallow_copy_book.contacts}")
    
    # ПЕРЕВІРКА СУТІ copy: елементи всередині списку ті самі
    is_same_person = original_book.contacts[0] is shallow_copy_book.contacts[0]
    print(f"Чи це той самий об'єкт Person всередині? -> {is_same_person} (Має бути True)")
    
    # Зміна в копії вплине на оригінал (бо об'єкт спільний)
    print(">> Змінюємо ім'я в поверхневій копії...")
    shallow_copy_book.contacts[0].name = "Shallow Name Changed"
    print(f"Ім'я в оригіналі: {original_book.contacts[0].name} (Змінилося!)")

    # Повертаємо ім'я назад для чистоти наступного тесту
    original_book.contacts[0].name = "Allen Raymond"

    # ---------------------------------------------------------
    print("\n--- Тест 2: Глибоке копіювання (deepcopy) ---")
    # ---------------------------------------------------------
    deep_copy_book = copy.deepcopy(original_book)
    
    print(f"Це різні об'єкти Contacts? -> {original_book is not deep_copy_book}")
    
    # ПЕРЕВІРКА СУТІ deepcopy: елементи всередині списку РІЗНІ (нові)
    is_same_person_deep = original_book.contacts[0] is deep_copy_book.contacts[0]
    print(f"Чи це той самий об'єкт Person всередині? -> {is_same_person_deep} (Має бути False)")
    
    # Зміна в копії НЕ вплине на оригінал
    print(">> Змінюємо ім'я в глибокій копії...")
    deep_copy_book.contacts[0].name = "Deep Name Changed"
    
    print(f"Ім'я в копії:    {deep_copy_book.contacts[0].name}")
    print(f"Ім'я в оригіналі: {original_book.contacts[0].name} (НЕ змінилося!)")


#====================================================================================================
import copy
import pickle

class Person:
    """
    Клас, що представляє інформацію про окрему особу.
    """
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __str__(self):
        return f"{self.name} ({self.email}, {self.phone}, Favorite: {self.favorite})"

    def __copy__(self):
        """
        Реалізація поверхневого копіювання для Person.
        """
        return Person(self.name, self.email, self.phone, self.favorite)


def copy_class_person(person):
    """
    Створює поверхневу копію екземпляра класу Person.
    
    :param person: Об'єкт класу Person.
    :return: Новий об'єкт (копія).
    """
    return copy.copy(person)


class Contacts:
    """
    Клас-контейнер для списку контактів.
    Підтримує серіалізацію через pickle.
    """
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        """
        Реалізація поверхневого копіювання для Contacts.
        Створює новий об'єкт Contacts та новий список contacts, 
        але елементи списку залишаються посиланнями на оригінали.
        """
        new_instance = Contacts(self.filename, copy.copy(self.contacts))
        new_instance.is_unpacking = self.is_unpacking
        new_instance.count_save = self.count_save
        return new_instance

    def __deepcopy__(self, memo):
        """
        Реалізація глибокого копіювання для Contacts.
        Створює повну незалежну копію об'єкта та всіх його вкладених елементів.
        """
        new_contacts = copy.deepcopy(self.contacts, memo)
        new_instance = Contacts(self.filename, new_contacts)
        memo[id(self)] = new_instance
        new_instance.is_unpacking = self.is_unpacking
        new_instance.count_save = self.count_save
        return new_instance


def copy_class_contacts(contacts):
    """
    Створює глибоку копію екземпляра класу Contacts.
    Це гарантує, що список контактів та самі контакти також будуть скопійовані,
    а не передані за посиланням.
    
    :param contacts: Об'єкт класу Contacts.
    :return: Новий об'єкт (глибока копія).
    """
    return copy.deepcopy(contacts)


# --- Блок перевірки ---
if __name__ == "__main__":
    # Коментуємо код перевірки, щоб уникнути затримок при автоматичному тестуванні
    pass
    # contacts_list = [
    #     Person(
    #         "Allen Raymond",
    #         "nulla.ante@vestibul.co.uk",
    #         "(992) 914-3792",
    #         False,
    #     ),
    #     Person(
    #         "Chaim Lewis",
    #         "dui.in@egetlacus.ca",
    #         "(294) 840-6685",
    #         False,
    #     ),
    # ]

    # persons = Contacts("user_class.dat", contacts_list)

    # # Створення глибокої копії
    # new_persons = copy_class_contacts(persons)

    # # Зміна даних у копії
    # new_persons.contacts[0].name = "Another name"

    # # Перевірка незалежності об'єктів
    # print(f"Оригінал (перший контакт): {persons.contacts[0].name}")
    # print(f"Копія    (перший контакт): {new_persons.contacts[0].name}")

    # print(f"persons is new_persons? {persons is new_persons}")
    # print(f"persons.contacts is new_persons.contacts? {persons.contacts is new_persons.contacts}")
#===================================================================================================