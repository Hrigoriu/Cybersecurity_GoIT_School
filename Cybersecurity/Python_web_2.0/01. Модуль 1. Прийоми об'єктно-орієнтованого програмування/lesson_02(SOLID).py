"""
    ! SOLID ! 
Це абревіатура, складена з перших літер п'яти базових принципів об'єктно-орієнтованого програмування (Single responsibility, Open-closed, Liskov substitution, Interface segregation та Dependency inversion.) та дизайну, запропонована Робертом Мартіном.
    Single responsibility — принцип єдиної відповідальності
    Open-closed —           принцип відкритості / закритості
    Liskov substitution —   принцип підстановки Барбари Лісков
    Interface segregation — принцип розділення інтерфейсу
    Dependency inversion —  принцип інверсії залежностей
"""
#=====================================================================================================
"""
    1. Принцип єдиної відповідальності (Single Responsibility Principle, SRP)
Клас повинен мати лише одну причину для зміни, тобто виконувати лише одну відповідальність. 
Це сприяє кращій організації коду та полегшує його підтримку.
    2. Принцип відкритості/закритості (Open/Closed Principle, OCP)
Програмні сутності (класи, модулі, функції) повинні бути відкриті для розширення, але закриті для модифікації. 
Це означає, що можна додавати нову функціональність без зміни існуючого коду.    
    3. Принцип підстановки Лісков (Liskov Substitution Principle, LSP)
Об'єкти підкласів повинні бути замінними на об'єкти їхніх батьківських класів без порушення коректності програми. 
Це забезпечує правильну поведінку під час використання поліморфізму.
    4. Принцип розділення інтерфейсів (Interface Segregation Principle, ISP)
Краще мати багато спеціалізованих інтерфейсів, ніж один універсальний. 
Класи не повинні залежати від інтерфейсів, які вони не використовують. 
Це сприяє більшій гнучкості та зменшує зв'язність між компонентами.
    5. Принцип інверсії залежностей (Dependency Inversion Principle, DIP)
Високорівневі модулі не повинні залежати від низькорівневих модулів. 
Обидва типи модулів повинні залежати від абстракцій. 
Абстракції не повинні залежати від деталей; деталі повинні залежати від абстракцій. 
Це сприяє зменшенню зв'язності та підвищенню гнучкості системи.
"""
#=====================================================================================================
    # *Принцип єдиної відповідальності (Single responsibility)
#=====================================================================================================
class Person:
    def __init__(self, name, zip, city, street):
        self.name = name
        self.zip = zip
        self.city = city
        self.street = street

    def get_address(self):
        return f'{self.zip}, {self.city}, {self.street}'


person = Person('Alexander', '36007', 'Poltava', 'European, 28')
print(person.get_address()) # 36007, Poltava, European, 28
#=====================================================================================================
class PersonAddress:
    def __init__(self, zip, city, street):
        self.zip = zip
        self.city = city
        self.street = street

    def value_of(self):
        return f'{self.zip}, {self.city}, {self.street}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_address(self):
        return self.address.value_of()


if __name__ == '__main__':
    person = Person('Alexander', PersonAddress('36007', 'Poltava', 'European, 28'))
    print(person.get_address()) # 36007, Poltava, European, 28
#=====================================================================================================
    # *Принцип відкритості-закритості (Open-closed)
#=====================================================================================================
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height


def total_area(shapes):
    sum = 0
    for el in shapes:
        sum += el.width * el.height
    return sum


if __name__ == '__main__':
    shapes = [Rect(10, 10), Rect(4, 5), Rect(3, 3)]
    area = total_area(shapes)
    print(area) # 129
#=====================================================================================================
from math import pi


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius):
        self.radius = radius


def total_area(shapes):
    sum = 0
    for el in shapes:
        if isinstance(el, Rect):
            sum += el.width * el.height
        if isinstance(el, Circle):
            sum += el.radius ** 2 * pi
    return sum


if __name__ == '__main__':
    shapes = [Rect(10, 10), Circle(5), Rect(4, 5), Rect(3, 3), Circle(3)]
    area = total_area(shapes)
    print(area) # 235.81415022205297
#=====================================================================================================
from math import pi


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area_of(self):
        return self.radius ** 2 * pi


def total_area(shapes):
    sum = 0
    for el in shapes:
        sum += el.area_of()
    return sum


if __name__ == '__main__':
    shapes = [Rect(10, 10), Circle(5), Rect(4, 5), Rect(3, 3), Circle(3)]
    area = total_area(shapes)
    print(area)
# 235.81415022205297
#=====================================================================================================
    # *Принцип підстановки Барбари Лісков (Liskov substitution)
#=====================================================================================================
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area_of(self):
        return self.width * self.height

class Square(Rect):
    def __init__(self, size):
        Rect.__init__(self, size, size)

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

def test_shape_size(shape):
    shape.set_width(10)
    shape.set_height(20)
    return shape.area_of() == 200  # умова не спрацює, якщо shape — екземпляр класу Square

#=====================================================================================================
from enum import Enum


class SideType(Enum):
    TYPE_WIDTH = 'width'
    TYPE_HEIGHT = 'height'


class Shape:
    def set_side(self, size, side):
        pass

    def area_of(self):
        pass


class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_side(self, size, side):
        if SideType.TYPE_WIDTH == side:
            self.width = size
        if SideType.TYPE_HEIGHT == side:
            self.height = size

    def set_width(self, width):
        self.set_side(width, SideType.TYPE_WIDTH)

    def set_height(self, height):
        self.set_side(height, SideType.TYPE_HEIGHT)

    def area_of(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, size):
        self.edge = size

    def set_side(self, size, side=None):
        self.edge = size

    def set_width(self, width):
        self.set_side(width)

    def area_of(self):
        return self.edge ** 2


def get_area_of_shape(figure: Shape):
    return figure.area_of()

    
if __name__ == '__main__':
    square = Square(10)
    rect = Rect(5, 10)
    print('Square area: ', get_area_of_shape(square))
    print('Rect area: ', get_area_of_shape(rect))
# Square area:  100
# Rect area:  50
#=====================================================================================================
    # *Принцип розділення інтерфейсу (Interface segregation)
#=====================================================================================================
class Programmer:
    def write_code(self):
        pass

    def eat_pizza(self, slice_count):
        pass


class OfficeProgrammer(Programmer):
    def __init__(self, name):
        self.name = name

    def eat_pizza(self, slice_count):
        print(f'{self.name} eat {slice_count} slice pizza!')

    def write_code(self):
        print(f'{self.name} write code!')

class RemoteProgrammer(Programmer):
    def __init__(self, name):
        self.name = name

    def write_code(self):
        print(f'{self.name} write code!')

    def eat_pizza(self, slice_count):
        pass
# RemoteProgrammer не повинен реалізовувати метод eat_pizza, оскільки він не їсть піцу в офісі
#=====================================================================================================
class CodeProducer:
    def write_code(self):
        pass


class PizzaConsumer:
    def eat_pizza(self, slice_count):
        pass


class OfficeProgrammer(CodeProducer, PizzaConsumer):
    def __init__(self, name):
        self.name = name

    def eat_pizza(self, slice_count):
        print(f'{self.name} eat {slice_count} slice pizza!')

    def write_code(self):
        print(f'{self.name} write code!')


class RemoteProgrammer(CodeProducer):
    def __init__(self, name):
        self.name = name

    def write_code(self):
        print(f'{self.name} write code!')
# RemoteProgrammer тепер не залежить від методу eat_pizza
#=====================================================================================================
    # *Принцип інверсії залежностей (Dependency inversion)
#=====================================================================================================
import requests


class RequestConnection:
    def __init__(self, request):
        self.request = request

    def get_json_from_url(self, url):
        return self.request.get(url).json()


class ApiClient:
    def __init__(self, fetch: RequestConnection):
        self.fetch = fetch

    def get_data(self, url):
        response = self.fetch.get_json_from_url(url)
        return response


def data_adapter(data: dict):
    return [{f"{el.get('ccy')}": {"buy": float(el.get('buy')), "sale": float(el.get('sale'))}} for el in data]


def pretty_view(data):
    pattern = '|{:^10}|{:^10}|{:^10}|'
    print(pattern.format('currency', 'sale', 'buy'))
    for el in data:
        currency, *_ = el.keys()
        buy = el.get(currency).get('buy')
        sale = el.get(currency).get('sale')
        print(pattern.format(currency, sale, buy))


if __name__ == '__main__':
    api_client = ApiClient(RequestConnection(requests))
    
    data = api_client.get_data('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11')
    pretty_view(data_adapter(data))
# | currency |   sale   |   buy    |
# |   USD    | 36.6500  | 36.2000  |
# |   EUR    | 39.2500  | 38.7000  |
#=====================================================================================================
