class Point:
    """
    Клас, що відповідає за відображення геометричної точки на площині.
    """
    def __init__(self, x, y):
        """
        Конструктор класу Point.
        Ініціалізує координати x та y.
        """
        self.x = x
        self.y = y

# --- Приклад використання ---
if __name__ == "__main__":
    point = Point(5, 10)

    print(point.x)  # 5
    print(point.y)  # 10

#======================================================================================
class Point:
    """
    Клас, що відповідає за відображення геометричної точки на площині.
    """
    def __init__(self, x, y):
        """
        Конструктор класу Point.
        Ініціалізує координати x та y як приватні атрибути.
        """
        self.__x = x
        self.__y = y

    @property
    def x(self):
        """Геттер для координати x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Сеттер для координати x."""
        self.__x = value

    @property
    def y(self):
        """Геттер для координати y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Сеттер для координати y."""
        self.__y = value

# --- Приклад використання ---
if __name__ == "__main__":
    point = Point(5, 10)

    print(point.x)  # 5
    print(point.y)  # 10
    
    # Перевірка роботи сеттерів
    point.x = 15
    point.y = 20
    print(f"Нові координати: x={point.x}, y={point.y}")        
#======================================================================================
class Point:
    """
    Клас для представлення точки на площині.
    """

    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            self.__x = value
        else:
            self.__x = None

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            self.__y = value
        else:
            self.__y = None


# --- Приклад ---
point = Point("a", 10)

print(point.x)  # None
print(point.y)  # 10

#======================================================================================
class Point:
    """
    Клас, що відповідає за відображення геометричної точки на площині.
    """
    def __init__(self, x, y):
        """
        Конструктор класу Point.
        Ініціалізує координати x та y як приватні атрибути.
        Важливо спочатку встановити None, щоб атрибути існували, 
        навіть якщо валідація в сеттерах не пройде.
        """
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        """Геттер для координати x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Сеттер для координати x. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            self.__x = value
        # Якщо значення невалідне, ми просто ігноруємо його. 
        # При створенні об'єкта self.__x залишиться None.

    @property
    def y(self):
        """Геттер для координати y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Сеттер для координати y. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            self.__y = value

# --- Приклад використання ---
if __name__ == "__main__":
    point = Point("a", 10)

    print(f"x: {point.x}")  # None, бо "a" не пройшло валідацію
    print(f"y: {point.y}")  # 10, бо 10 - це число
    
    # Перевірка роботи сеттерів з правильними даними
    point.x = 15
    point.y = 20
    print(f"Нові координати: x={point.x}, y={point.y}")
#======================================================================================
class Point:
    """
    Клас, що відповідає за відображення геометричної точки на площині.
    """
    def __init__(self, x, y):
        """
        Конструктор класу Point.
        Ініціалізує координати x та y як приватні атрибути.
        Важливо спочатку встановити None, щоб атрибути існували, 
        навіть якщо валідація в сеттерах не пройде.
        """
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        """Геттер для координати x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Сеттер для координати x. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)):
            self.__x = value
        # Якщо значення невалідне, ми просто ігноруємо його. 
        # При створенні об'єкта self.__x залишиться None.

    @property
    def y(self):
        """Геттер для координати y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Сеттер для координати y. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)):
            self.__y = value


class Vector:
    """
    Клас, що відповідає за вектор (спрямований відрізок).
    Координати вектора визначаються екземпляром класу Point.
    """
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        """
        Дозволяє встановлювати координати через індекс (vector[0] = x, vector[1] = y).
        """
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Vector index out of range (use 0 for x, 1 for y)")

    def __getitem__(self, index):
        """
        Дозволяє отримувати координати через індекс (vector[0] -> x, vector[1] -> y).
        """
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Vector index out of range (use 0 for x, 1 for y)")


# --- Приклад використання ---
if __name__ == "__main__":
    # Робота з точкою
    point = Point("a", 10)
    print(f"Point x: {point.x}")  # None
    print(f"Point y: {point.y}")  # 10
    
    point.x = 15
    point.y = 20
    print(f"New Point coords: x={point.x}, y={point.y}")

    # Робота з вектором
    vector = Vector(Point(1, 10))

    print(f"Vector x via property: {vector.coordinates.x}")  # 1
    print(f"Vector y via property: {vector.coordinates.y}")  # 10

    vector[0] = 10  # Встановлюємо координату x вектора через індекс
    
    print(f"Vector x via index: {vector[0]}")  # 10
    print(f"Vector y via index: {vector[1]}")  # 10
#======================================================================================
class Point:
    """
    Клас, що відповідає за відображення геометричної точки на площині.
    """
    def __init__(self, x, y):
        """
        Конструктор класу Point.
        Ініціалізує координати x та y як приватні атрибути.
        Важливо спочатку встановити None, щоб атрибути існували, 
        навіть якщо валідація в сеттерах не пройде.
        """
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        """Геттер для координати x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Сеттер для координати x. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)):
            self.__x = value
        # Якщо значення невалідне, ми просто ігноруємо його. 
        # При створенні об'єкта self.__x залишиться None.

    @property
    def y(self):
        """Геттер для координати y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Сеттер для координати y. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)):
            self.__y = value

    def __str__(self):
        """Повертає рядкове представлення точки у форматі Point(x,y)."""
        return f"Point({self.x},{self.y})"


class Vector:
    """
    Клас, що відповідає за вектор (спрямований відрізок).
    Координати вектора визначаються екземпляром класу Point.
    """
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        """
        Дозволяє встановлювати координати через індекс (vector[0] = x, vector[1] = y).
        """
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Vector index out of range (use 0 for x, 1 for y)")

    def __getitem__(self, index):
        """
        Дозволяє отримувати координати через індекс (vector[0] -> x, vector[1] -> y).
        """
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Vector index out of range (use 0 for x, 1 for y)")

    def __str__(self):
        """Повертає рядкове представлення вектора у форматі Vector(x,y)."""
        return f"Vector({self.coordinates.x},{self.coordinates.y})"


# --- Приклад використання ---
if __name__ == "__main__":
    point = Point(1, 10)
    vector = Vector(point)

    print(point)   # Point(1,10)
    print(vector)  # Vector(1,10)
#======================================================================================
class Point:
    """
    Клас, що відповідає за відображення геометричної точки на площині.
    """
    def __init__(self, x, y):
        """
        Конструктор класу Point.
        Ініціалізує координати x та y як приватні атрибути.
        Важливо спочатку встановити None, щоб атрибути існували, 
        навіть якщо валідація в сеттерах не пройде.
        """
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        """Геттер для координати x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Сеттер для координати x. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)):
            self.__x = value
        # Якщо значення невалідне, ми просто ігноруємо його. 
        # При створенні об'єкта self.__x залишиться None.

    @property
    def y(self):
        """Геттер для координати y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Сеттер для координати y. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)):
            self.__y = value

    def __str__(self):
        """Повертає рядкове представлення точки у форматі Point(x,y)."""
        return f"Point({self.x},{self.y})"


class Vector:
    """
    Клас, що відповідає за вектор (спрямований відрізок).
    Координати вектора визначаються екземпляром класу Point.
    """
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        """
        Дозволяє встановлювати координати через індекс (vector[0] = x, vector[1] = y).
        """
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Vector index out of range (use 0 for x, 1 for y)")

    def __getitem__(self, index):
        """
        Дозволяє отримувати координати через індекс (vector[0] -> x, vector[1] -> y).
        """
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Vector index out of range (use 0 for x, 1 for y)")

    def __call__(self, value=None):
        """
        Функтор: дозволяє викликати об'єкт як функцію.
        Якщо value не передано -> повертає кортеж координат (x, y).
        Якщо value передано -> повертає кортеж координат, помножених на value (x*value, y*value).
        """
        if value is None:
            return (self.coordinates.x, self.coordinates.y)
        else:
            return (self.coordinates.x * value, self.coordinates.y * value)

    def __str__(self):
        """Повертає рядкове представлення вектора у форматі Vector(x,y)."""
        return f"Vector({self.coordinates.x},{self.coordinates.y})"


# --- Приклад використання ---
if __name__ == "__main__":
    point = Point(1, 10)
    vector = Vector(point)

    print(f"Об'єкт: {vector}")       # Vector(1,10)
    print(f"Виклик vector(): {vector()}")     # (1, 10)
    print(f"Виклик vector(5): {vector(5)}")   # (5, 50)
#======================================================================================
class Point:
    """
    Клас, що відповідає за відображення геометричної точки на площині.
    """
    def __init__(self, x, y):
        """
        Конструктор класу Point.
        Ініціалізує координати x та y як приватні атрибути.
        Важливо спочатку встановити None, щоб атрибути існували, 
        навіть якщо валідація в сеттерах не пройде.
        """
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        """Геттер для координати x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Сеттер для координати x. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)):
            self.__x = value
        # Якщо значення невалідне, ми просто ігноруємо його. 
        # При створенні об'єкта self.__x залишиться None.

    @property
    def y(self):
        """Геттер для координати y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Сеттер для координати y. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)):
            self.__y = value

    def __str__(self):
        """Повертає рядкове представлення точки у форматі Point(x,y)."""
        return f"Point({self.x},{self.y})"


class Vector:
    """
    Клас, що відповідає за вектор (спрямований відрізок).
    Координати вектора визначаються екземпляром класу Point.
    """
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        """
        Дозволяє встановлювати координати через індекс (vector[0] = x, vector[1] = y).
        """
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Vector index out of range (use 0 for x, 1 for y)")

    def __getitem__(self, index):
        """
        Дозволяє отримувати координати через індекс (vector[0] -> x, vector[1] -> y).
        """
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Vector index out of range (use 0 for x, 1 for y)")

    def __call__(self, value=None):
        """
        Функтор: дозволяє викликати об'єкт як функцію.
        Якщо value не передано -> повертає кортеж координат (x, y).
        Якщо value передано -> повертає кортеж координат, помножених на value (x*value, y*value).
        """
        if value is None:
            return (self.coordinates.x, self.coordinates.y)
        else:
            return (self.coordinates.x * value, self.coordinates.y * value)

    def __add__(self, vector):
        """
        Перевизначення оператора додавання (+).
        Повертає новий Vector з координатами (x1+x2, y1+y2).
        """
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        """
        Перевизначення оператора віднімання (-).
        Повертає новий Vector з координатами (x1-x2, y1-y2).
        """
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __str__(self):
        """Повертає рядкове представлення вектора у форматі Vector(x,y)."""
        return f"Vector({self.coordinates.x},{self.coordinates.y})"


# --- Приклад використання ---
if __name__ == "__main__":
    vector1 = Vector(Point(1, 10))
    vector2 = Vector(Point(10, 10))

    vector3 = vector2 + vector1
    vector4 = vector2 - vector1

    print(f"Vector 1: {vector1}")
    print(f"Vector 2: {vector2}")
    print(f"Sum (v2 + v1): {vector3}")  # Vector(11,20)
    print(f"Sub (v2 - v1): {vector4}")  # Vector(9,0)
    
#======================================================================================
class Point:
    """
    Клас, що відповідає за відображення геометричної точки на площині.
    """
    def __init__(self, x, y):
        """
        Конструктор класу Point.
        Ініціалізує координати x та y як приватні атрибути.
        Важливо спочатку встановити None, щоб атрибути існували, 
        навіть якщо валідація в сеттерах не пройде.
        """
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        """Геттер для координати x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Сеттер для координати x. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)):
            self.__x = value
        # Якщо значення невалідне, ми просто ігноруємо його. 
        # При створенні об'єкта self.__x залишиться None.

    @property
    def y(self):
        """Геттер для координати y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Сеттер для координати y. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)):
            self.__y = value

    def __str__(self):
        """Повертає рядкове представлення точки у форматі Point(x,y)."""
        return f"Point({self.x},{self.y})"


class Vector:
    """
    Клас, що відповідає за вектор (спрямований відрізок).
    Координати вектора визначаються екземпляром класу Point.
    """
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        """
        Дозволяє встановлювати координати через індекс (vector[0] = x, vector[1] = y).
        """
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Vector index out of range (use 0 for x, 1 for y)")

    def __getitem__(self, index):
        """
        Дозволяє отримувати координати через індекс (vector[0] -> x, vector[1] -> y).
        """
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Vector index out of range (use 0 for x, 1 for y)")

    def __call__(self, value=None):
        """
        Функтор: дозволяє викликати об'єкт як функцію.
        Якщо value не передано -> повертає кортеж координат (x, y).
        Якщо value передано -> повертає кортеж координат, помножених на value (x*value, y*value).
        """
        if value is None:
            return (self.coordinates.x, self.coordinates.y)
        else:
            return (self.coordinates.x * value, self.coordinates.y * value)

    def __add__(self, vector):
        """
        Перевизначення оператора додавання (+).
        Повертає новий Vector з координатами (x1+x2, y1+y2).
        """
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        """
        Перевизначення оператора віднімання (-).
        Повертає новий Vector з координатами (x1-x2, y1-y2).
        """
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        """
        Перевизначення оператора множення (*).
        Повертає скалярний добуток векторів (число).
        Formula: x1*x2 + y1*y2
        """
        return (self.coordinates.x * vector.coordinates.x) + \
               (self.coordinates.y * vector.coordinates.y)

    def __str__(self):
        """Повертає рядкове представлення вектора у форматі Vector(x,y)."""
        return f"Vector({self.coordinates.x},{self.coordinates.y})"


# --- Приклад використання ---
if __name__ == "__main__":
    vector1 = Vector(Point(1, 10))
    vector2 = Vector(Point(10, 10))

    vector3 = vector2 + vector1
    vector4 = vector2 - vector1
    scalar = vector2 * vector1

    print(f"Vector 1: {vector1}")
    print(f"Vector 2: {vector2}")
    print(f"Sum (v2 + v1): {vector3}")    # Vector(11,20)
    print(f"Sub (v2 - v1): {vector4}")    # Vector(9,0)
    print(f"Scalar product (v2 * v1): {scalar}") # 110
    
#======================================================================================
class Point:
    """
    Клас, що відповідає за відображення геометричної точки на площині.
    """
    def __init__(self, x, y):
        """
        Конструктор класу Point.
        Ініціалізує координати x та y як приватні атрибути.
        Важливо спочатку встановити None, щоб атрибути існували, 
        навіть якщо валідація в сеттерах не пройде.
        """
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        """Геттер для координати x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Сеттер для координати x. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)):
            self.__x = value
        # Якщо значення невалідне, ми просто ігноруємо його. 
        # При створенні об'єкта self.__x залишиться None.

    @property
    def y(self):
        """Геттер для координати y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Сеттер для координати y. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)):
            self.__y = value

    def __str__(self):
        """Повертає рядкове представлення точки у форматі Point(x,y)."""
        return f"Point({self.x},{self.y})"


class Vector:
    """
    Клас, що відповідає за вектор (спрямований відрізок).
    Координати вектора визначаються екземпляром класу Point.
    """
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        """
        Дозволяє встановлювати координати через індекс (vector[0] = x, vector[1] = y).
        """
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Vector index out of range (use 0 for x, 1 for y)")

    def __getitem__(self, index):
        """
        Дозволяє отримувати координати через індекс (vector[0] -> x, vector[1] -> y).
        """
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Vector index out of range (use 0 for x, 1 for y)")

    def __call__(self, value=None):
        """
        Функтор: дозволяє викликати об'єкт як функцію.
        Якщо value не передано -> повертає кортеж координат (x, y).
        Якщо value передано -> повертає кортеж координат, помножених на value (x*value, y*value).
        """
        if value is None:
            return (self.coordinates.x, self.coordinates.y)
        else:
            return (self.coordinates.x * value, self.coordinates.y * value)

    def __add__(self, vector):
        """
        Перевизначення оператора додавання (+).
        Повертає новий Vector з координатами (x1+x2, y1+y2).
        """
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        """
        Перевизначення оператора віднімання (-).
        Повертає новий Vector з координатами (x1-x2, y1-y2).
        """
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        """
        Перевизначення оператора множення (*).
        Повертає скалярний добуток векторів (число).
        Formula: x1*x2 + y1*y2
        """
        return (self.coordinates.x * vector.coordinates.x) + \
               (self.coordinates.y * vector.coordinates.y)

    def len(self):
        """
        Обчислює довжину вектора.
        Formula: sqrt(x^2 + y^2)
        """
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __str__(self):
        """Повертає рядкове представлення вектора у форматі Vector(x,y)."""
        return f"Vector({self.coordinates.x},{self.coordinates.y})"


# --- Приклад використання ---
if __name__ == "__main__":
    vector1 = Vector(Point(1, 10))
    vector2 = Vector(Point(10, 10))

    vector3 = vector2 + vector1
    vector4 = vector2 - vector1
    scalar = vector2 * vector1

    print(f"Vector 1: {vector1}")
    print(f"Vector 2: {vector2}")
    
    print(f"Length of vector1: {vector1.len()}") # 10.049...
    print(f"Length of vector2: {vector2.len()}") # 14.142...
    
#======================================================================================
class Point:
    """
    Клас, що відповідає за відображення геометричної точки на площині.
    """
    def __init__(self, x, y):
        """
        Конструктор класу Point.
        Ініціалізує координати x та y як приватні атрибути.
        Важливо спочатку встановити None, щоб атрибути існували, 
        навіть якщо валідація в сеттерах не пройде.
        """
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        """Геттер для координати x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Сеттер для координати x. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)):
            self.__x = value
        # Якщо значення невалідне, ми просто ігноруємо його. 
        # При створенні об'єкта self.__x залишиться None.

    @property
    def y(self):
        """Геттер для координати y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Сеттер для координати y. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)):
            self.__y = value

    def __str__(self):
        """Повертає рядкове представлення точки у форматі Point(x,y)."""
        return f"Point({self.x},{self.y})"


class Vector:
    """
    Клас, що відповідає за вектор (спрямований відрізок).
    Координати вектора визначаються екземпляром класу Point.
    """
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        """
        Дозволяє встановлювати координати через індекс (vector[0] = x, vector[1] = y).
        """
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Vector index out of range (use 0 for x, 1 for y)")

    def __getitem__(self, index):
        """
        Дозволяє отримувати координати через індекс (vector[0] -> x, vector[1] -> y).
        """
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Vector index out of range (use 0 for x, 1 for y)")

    def __call__(self, value=None):
        """
        Функтор: дозволяє викликати об'єкт як функцію.
        Якщо value не передано -> повертає кортеж координат (x, y).
        Якщо value передано -> повертає кортеж координат, помножених на value (x*value, y*value).
        """
        if value is None:
            return (self.coordinates.x, self.coordinates.y)
        else:
            return (self.coordinates.x * value, self.coordinates.y * value)

    def __add__(self, vector):
        """
        Перевизначення оператора додавання (+).
        Повертає новий Vector з координатами (x1+x2, y1+y2).
        """
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        """
        Перевизначення оператора віднімання (-).
        Повертає новий Vector з координатами (x1-x2, y1-y2).
        """
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        """
        Перевизначення оператора множення (*).
        Повертає скалярний добуток векторів (число).
        Formula: x1*x2 + y1*y2
        """
        return (self.coordinates.x * vector.coordinates.x) + \
               (self.coordinates.y * vector.coordinates.y)

    def len(self):
        """
        Обчислює довжину вектора.
        Formula: sqrt(x^2 + y^2)
        """
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __eq__(self, vector):
        """Порівняння на рівність (==) за довжиною."""
        return self.len() == vector.len()

    def __ne__(self, vector):
        """Порівняння на нерівність (!=) за довжиною."""
        return self.len() != vector.len()

    def __lt__(self, vector):
        """Порівняння менше (<) за довжиною."""
        return self.len() < vector.len()

    def __gt__(self, vector):
        """Порівняння більше (>) за довжиною."""
        return self.len() > vector.len()

    def __le__(self, vector):
        """Порівняння менше або дорівнює (<=) за довжиною."""
        return self.len() <= vector.len()

    def __ge__(self, vector):
        """Порівняння більше або дорівнює (>=) за довжиною."""
        return self.len() >= vector.len()

    def __str__(self):
        """Повертає рядкове представлення вектора у форматі Vector(x,y)."""
        return f"Vector({self.coordinates.x},{self.coordinates.y})"


# --- Приклад використання ---
if __name__ == "__main__":
    vector1 = Vector(Point(1, 10))
    vector2 = Vector(Point(3, 10))

    print(f"Vector 1 length: {vector1.len()}") # ~10.05
    print(f"Vector 2 length: {vector2.len()}") # ~10.44

    print(f"v1 == v2: {vector1 == vector2}")  # False
    print(f"v1 != v2: {vector1 != vector2}")  # True
    print(f"v1 > v2:  {vector1 > vector2}")   # False
    print(f"v1 < v2:  {vector1 < vector2}")   # True
    print(f"v1 >= v2: {vector1 >= vector2}")  # False
    print(f"v1 <= v2: {vector1 <= vector2}")  # True
    
#======================================================================================
from random import randrange


class Point:
    """
    Клас, що відповідає за відображення геометричної точки на площині.
    """
    def __init__(self, x, y):
        """
        Конструктор класу Point.
        Ініціалізує координати x та y як приватні атрибути.
        Важливо спочатку встановити None, щоб атрибути існували, 
        навіть якщо валідація в сеттерах не пройде.
        """
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        """Геттер для координати x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Сеттер для координати x. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)):
            self.__x = value
        # Якщо значення невалідне, ми просто ігноруємо його. 
        # При створенні об'єкта self.__x залишиться None.

    @property
    def y(self):
        """Геттер для координати y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Сеттер для координати y. Приймає тільки числа (int або float)."""
        if isinstance(value, (int, float)):
            self.__y = value

    def __str__(self):
        """Повертає рядкове представлення точки у форматі Point(x,y)."""
        return f"Point({self.x},{self.y})"


class Vector:
    """
    Клас, що відповідає за вектор (спрямований відрізок).
    Координати вектора визначаються екземпляром класу Point.
    """
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        """
        Дозволяє встановлювати координати через індекс (vector[0] = x, vector[1] = y).
        """
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Vector index out of range (use 0 for x, 1 for y)")

    def __getitem__(self, index):
        """
        Дозволяє отримувати координати через індекс (vector[0] -> x, vector[1] -> y).
        """
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Vector index out of range (use 0 for x, 1 for y)")

    def __call__(self, value=None):
        """
        Функтор: дозволяє викликати об'єкт як функцію.
        Якщо value не передано -> повертає кортеж координат (x, y).
        Якщо value передано -> повертає кортеж координат, помножених на value (x*value, y*value).
        """
        if value is None:
            return (self.coordinates.x, self.coordinates.y)
        else:
            return (self.coordinates.x * value, self.coordinates.y * value)

    def __add__(self, vector):
        """
        Перевизначення оператора додавання (+).
        Повертає новий Vector з координатами (x1+x2, y1+y2).
        """
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        """
        Перевизначення оператора віднімання (-).
        Повертає новий Vector з координатами (x1-x2, y1-y2).
        """
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        """
        Перевизначення оператора множення (*).
        Повертає скалярний добуток векторів (число).
        Formula: x1*x2 + y1*y2
        """
        return (self.coordinates.x * vector.coordinates.x) + \
               (self.coordinates.y * vector.coordinates.y)

    def len(self):
        """
        Обчислює довжину вектора.
        Formula: sqrt(x^2 + y^2)
        """
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __eq__(self, vector):
        """Порівняння на рівність (==) за довжиною."""
        return self.len() == vector.len()

    def __ne__(self, vector):
        """Порівняння на нерівність (!=) за довжиною."""
        return self.len() != vector.len()

    def __lt__(self, vector):
        """Порівняння менше (<) за довжиною."""
        return self.len() < vector.len()

    def __gt__(self, vector):
        """Порівняння більше (>) за довжиною."""
        return self.len() > vector.len()

    def __le__(self, vector):
        """Порівняння менше або дорівнює (<=) за довжиною."""
        return self.len() <= vector.len()

    def __ge__(self, vector):
        """Порівняння більше або дорівнює (>=) за довжиною."""
        return self.len() >= vector.len()

    def __str__(self):
        """Повертає рядкове представлення вектора у форматі Vector(x,y)."""
        return f"Vector({self.coordinates.x},{self.coordinates.y})"


class Iterable:
    """
    Клас-ітератор.
    Відповідає за зберігання стану ітерації та генерацію наступного елемента.
    """
    def __init__(self, max_vectors, max_points):
        self.current_index = 0
        self.vectors = []
        # Генеруємо список випадкових векторів
        for _ in range(max_vectors):
            x = randrange(max_points)
            y = randrange(max_points)
            self.vectors.append(Vector(Point(x, y)))

    def __next__(self):
        """
        Повертає наступний елемент або генерує StopIteration.
        """
        if self.current_index < len(self.vectors):
            vector = self.vectors[self.current_index]
            self.current_index += 1
            return vector
        raise StopIteration


class RandomVectors:
    """
    Клас, що представляє колекцію випадкових векторів (Iterable object).
    """
    def __init__(self, max_vectors=10, max_points=50):
        self.max_vectors = max_vectors
        self.max_points = max_points

    def __iter__(self):
        """
        Повертає об'єкт-ітератор (Iterable).
        """
        return Iterable(self.max_vectors, self.max_points)


# --- Приклад використання ---
if __name__ == "__main__":
    # Створюємо генератор 5 випадкових векторів з координатами до 10
    vectors = RandomVectors(5, 10)

    print("Згенеровані випадкові вектори:")
    for vector in vectors:
        print(vector)
"""
Згенеровані випадкові вектори:
Vector(2,5)
Vector(4,7)
Vector(6,5)
Vector(8,3)
Vector(4,2)
"""
#======================================================================================

#======================================================================================