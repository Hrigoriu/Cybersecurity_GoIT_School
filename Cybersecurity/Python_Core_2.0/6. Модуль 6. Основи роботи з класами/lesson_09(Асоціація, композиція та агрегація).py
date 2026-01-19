"""
    ! Асоціація в ООП !
Це концепція, яка описує відносини між класами через їх об'єкти. 
У цьому контексті, клас може включати в себе інший клас як одне зі своїх полів, що описується словом "має".
Асоціація поділяється на два основних типи: композиція та агрегація
    Композиція вказує на сильну залежність, а агрегація на слабку
"""
#================================================================================================
"""
    ! Агрегація !
Це тип відношення між об'єктами, яке також представляє відносини "ціле" до "частини", але в цьому випадку "частини" можуть існувати незалежно від "цілого". 
Це означає, що якщо "ціле" буде знищено, "частини" можуть продовжувати існувати самостійно. 
"""
#================================================================================================
class Owner:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"

class Cat(Owner):
    def __init__(self, nickname, age, name, phone):
        super().__init__(name, phone)
        self.nickname = nickname
        self.age = age

    def cat_info(self):
        return f"Cat Name: {self.nickname}, Age: {self.age}"

    def sound(self):
		        return "Meow"

cat = Cat('Simon', 4, 'Boris', '+380503002010')
print(cat.info())
print(cat.cat_info())
print(cat.sound())
"""
Boris: +380503002010
Cat Name: Simon, Age: 4
Meow
"""
#================================================================================================
class Owner:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"

class Cat:
    def __init__(self, nickname: str, age: int, owner: Owner):
        self.nickname = nickname
        self.age = age
        self.owner = owner

    def get_info(self):
        return f"Cat Name: {self.nickname}, Age: {self.age}"

    def sound(self):
        return "Meow"

owner = Owner("Boris", "+380503002010")
cat = Cat("Simon", 4, owner)

print(cat.owner.info())
print(cat.get_info())
"""
Boris: +380503002010
Cat Name: Simon, Age: 4
Meow
"""
#================================================================================================
"""
    ! Композиція !
Це тип відношення між об'єктами, де один об'єкт є частиною іншого. 
У відношенні композиції "частина" не може існувати без "цілого". 
Це означає, що якщо "ціле" буде знищено або видалено, то "частина" також буде знищена або видалена.
Композиція дозволяє інкапсулювати поведінку та дані, пов'язані з управлінням задачами, всередині класу.
"""
#================================================================================================
class Task:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def display_info(self):
        print(f"Задача: {self.name}, Опис: {self.description}")

class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list(Task) = []

    def add_task(self, name: str, description: str):
        self.tasks.append(Task(name, description))

    def remove_task(self, name: str):
        self.tasks = [task for task in self.tasks if task.name != name]

    def display_project_info(self):
        print(f"Проект: {self.name}")
        for task in self.tasks:
            task.display_info()

# Створення проекту
my_project = Project("Веб-розробка")

# Додавання задач
my_project.add_task("Дизайн інтерфейсу", "Створити макет головної сторінки.")
my_project.add_task("Розробка API", "Реалізувати ендпоінти для користувачів.")

# Відображення інформації про проект
my_project.display_project_info()

# Видалення задачі
my_project.remove_task("Розробка API")

# Перевірка видалення задачі
my_project.display_project_info()
"""
Проект: Веб-розробка
Задача: Дизайн інтерфейсу, Опис: Створити макет головної сторінки.
Задача: Розробка API, Опис: Реалізувати ендпоінти для користувачів.
Проект: Веб-розробка
Задача: Дизайн інтерфейсу, Опис: Створити макет головної сторінки.
"""
