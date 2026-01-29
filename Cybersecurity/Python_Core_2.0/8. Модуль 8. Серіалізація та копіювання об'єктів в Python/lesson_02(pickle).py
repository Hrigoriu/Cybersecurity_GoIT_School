import pickle

# Об'єкт для серіалізації
my_data = {"key": "value", "num": 42}

# Серіалізація об'єкта в байтовий рядок
serialized_data = pickle.dumps(my_data)
# Виведе байтовий рядок
print(serialized_data)  

# Десеріалізація об'єкта з байтового рядка
deserialized_data = pickle.loads(serialized_data)
# Виведе вихідний об'єкт Python
print(deserialized_data)

"""
b'\\x80\\x04\\x95\\x1b\\x00\\x00\\x00\\x00\\x00\\x00\\x00}\\x94(\\x8c\\x03key\\x94\\x8c\\x05value\\x94\\x8c\\x03num\\x94K*u.'
{'key': 'value', 'num': 42}
"""
#===================================================================================================
import pickle

# Об'єкт для серіалізації
my_data = {"key": "value", "num": 100}

# Серіалізація об'єкта в файл
with open("data.pickle", "wb") as file:
    pickle.dump(my_data, file)

#===================================================================================================
import pickle

# Десеріалізація об'єкта з файлу
with open('data.pickle', 'rb') as file:
    deserialized_data = pickle.load(file)

# Виведе вихідний об'єкт Python
print(deserialized_data) # {'key': 'value', 'num': 100}

#===================================================================================================
import pickle

class Human:
    def __init__(self, name):
        self.name = name

bob = Human("Bob")
with open("instance.pickle", "wb") as file:
    pickle.dump(bob, file)

#===================================================================================================
import pickle

class Human:
    def __init__(self, name):
        self.name = name

with open("instance.pickle", "rb") as file:
    loaded_instance = pickle.load(file)

print(loaded_instance.name) # Bob

#===================================================================================================
import pickle

with open("instance.pickle", "rb") as file:
    loaded_instance = pickle.load(file)

print(loaded_instance.name)

"""
Traceback (most recent call last):
  File "d:\IT school\Projects\Projects_GoIT\Cybersecurity\test.py", line 4, in <module>
    loaded_instance = pickle.load(file)
                      ^^^^^^^^^^^^^^^^^
AttributeError: Can't get attribute 'Human' on <module '__main__' from 'd:\\IT school\\Projects\\Projects_GoIT\\Cybersecurity\\test.py'>
To fix this, ensure that the Human class is defined in the same module where you are unpickling the object.
"""
#===================================================================================================
    # Серіалізація об'єкта Python у файл за допомогою pickle
import pickle
# Збереження налаштувань
settings = {'theme': 'dark', 'language': 'ukrainian'}
with open('settings.pickle', 'wb') as f:
    pickle.dump(settings, f)
#===================================================================================================
    # Десеріалізація об'єкта Python з файлу за допомогою pickle
with open('settings.pickle', 'rb') as f:
    loaded_settings = pickle.load(f)
print(loaded_settings)
"""
{'theme': 'dark', 'language': 'ukrainian'}
"""
#===================================================================================================