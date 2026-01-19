"""
    ! Перелічуваний тип даних (Enumeration), Enum - 
Це спосіб визначення набору іменованих констант у мовах програмування, що дозволяє використовувати більш зрозумілі імена для цих констант замість простих числових значень. 
Enum визначає символічні імена для набору пов'язаних значень, полегшуючи читання та розуміння коду.
"""
#================================================================================================
from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
today = Day.MONDAY
print(today)  # Виведе: Day.MONDAY
print(today.value)  # Виведе: 1 
day_from_value = Day(1)
print(day_from_value)  # Виведе: Day.MONDAY
print(day_from_value.value)  # Виведе: 1
#================================================================================================
from enum import Enum, auto

class OrderStatus(Enum):
    NEW = auto()
    PROCESSING = auto() #"В обробці"
    SHIPPED = auto()    #"Відправлено"
    DELIVERED = auto()  #"Доставлено"

class Order:
    def __init__(self, name: str, status: OrderStatus):
        self.name = name
        self.status = status

    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")

    def display_status(self):
        print(f"Статус замовлення '{self.name}': {self.status.name}.")

order1 = Order("Ноутбук", OrderStatus.NEW)
order2 = Order("Книга", OrderStatus.NEW)

order1.display_status()
order2.display_status()

order1.update_status(OrderStatus.PROCESSING)
order2.update_status(OrderStatus.SHIPPED)

order1.display_status()
order2.display_status()
"""
Статус замовлення 'Ноутбук': NEW.
Статус замовлення 'Книга': NEW.

Замовлення 'Ноутбук' оновлено до статусу PROCESSING.
Замовлення 'Книга' оновлено до статусу SHIPPED.

Статус замовлення 'Ноутбук': PROCESSING.
Статус замовлення 'Книга': SHIPPED.
"""
#================================================================================================
from enum import Enum, auto

class OrderStatus(Enum):
    NEW = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELED = auto()
