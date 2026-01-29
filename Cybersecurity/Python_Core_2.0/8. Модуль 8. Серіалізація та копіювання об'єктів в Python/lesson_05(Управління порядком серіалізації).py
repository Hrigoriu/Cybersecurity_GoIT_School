"""
Серіалізація - це процес перетворення об'єкта у потік байтів для зберігання або передачі.
Десеріалізація - це зворотний процес, коли потік байтів перетворюється назад у об'єкт. 
Але не всі об'єкти Python можна серіалізувати. 
Наприклад, не можна серіалізувати файловий дескриптор або системний ресурс. 
"""
#===================================================================================================
"""
Коли викликається pickle.dump() або pickle.dumps() для серіалізації об'єкта, Python шукає метод __getstate__ у класі об'єкта. 
Якщо метод існує, він використовується для отримання стану об'єкта для серіалізації. 
При десеріалізації, за допомогою pickle.load() або pickle.loads(), Python шукає метод __setstate__ у класі. 
Якщо метод існує, він використовується для відновлення стану об'єкта з даних, отриманих під час десеріалізації.
"""
#===================================================================================================
import pickle

class Robot:
    def __init__(self, name, battery_life):
        self.name = name
        self.battery_life = battery_life
        # Цей атрибут ми не збираємось серіалізувати
        self.is_active = False  

    def __getstate__(self):
        state = self.__dict__
        # Видаляємо is_active з серіалізованого стану
        del state['is_active']
        return state

    def __setstate__(self, state):
        # Відновлюємо об'єкт при десеріалізації
        self.__dict__.update(state)
        # Задаємо значення is_active за замовчуванням
        self.is_active = False  

# Створення об'єкта Robot
robot = Robot("Robo1", 100)

# Серіалізація об'єкта
serialized_robot = pickle.dumps(robot)

# Десеріалізація об'єкта
deserialized_robot = pickle.loads(serialized_robot)

print(deserialized_robot.__dict__)
# Виведе {'name': 'Robo1', 'battery_life': 100, 'is_active': False}
#===================================================================================================
class Example:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Example("Gupalo Vasyl", 30)
{'name': 'Gupalo Vasyl', 'age': 30}

obj.__dict__['city'] = 'Poltava'  # Додавання нового атрибута
print(obj.city)  # Виведення: Poltava

del obj.__dict__['age']  # Видалення атрибута age
print(obj.__dict__)  # Виведення: {'name': 'Gupalo Vasyl', 'city': 'Poltava'}

#===================================================================================================
class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.fh = open(self.filename, "r", encoding="utf-8")

    def close(self):
        self.fh.close()

    def read(self):
        data = self.fh.read()
        return data

if __name__ == "__main__":
    reader = Reader("data.txt")
    data = reader.read()
    print(data)
    reader.close()

#===================================================================================================
import pickle

class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.fh = open(self.filename, "r", encoding="utf-8")

    def close(self):
        self.fh.close()

    def read(self):
        data = self.fh.read()
        return data

if __name__ == "__main__":
    reader = Reader("data.txt")
    # Приклад серіалізації об'єкта Reader
    with open("reader.pkl", "wb") as f:
        pickle.dump(reader, f)
    
#===================================================================================================
import pickle

class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.fh = open(self.filename, "r", encoding="utf-8")

    def close(self):
        self.fh.close()

    def read(self):
        data = self.fh.read()
        return data

    def __getstate__(self):
        attributes = {**self.__dict__, "fh": None}
        return attributes

    def __setstate__(self, state):
        # Відновлюємо стан об'єкта
        self.__dict__ = state
        self.fh = open(state["filename"], "r", encoding="utf-8")

if __name__ == "__main__":
    reader = Reader("data.txt")
    data = reader.read()
    print(data)
    reader.close()

    # Приклад серіалізації об'єкта Reader
    with open("reader.pkl", "wb") as f:
        pickle.dump(reader, f)

    # Приклад десеріалізації об'єкта Reader
    with open("reader.pkl", "rb") as f:
        loaded_reader = pickle.load(f)
        print(loaded_reader.read())
        loaded_reader.close()

#===================================================================================================
