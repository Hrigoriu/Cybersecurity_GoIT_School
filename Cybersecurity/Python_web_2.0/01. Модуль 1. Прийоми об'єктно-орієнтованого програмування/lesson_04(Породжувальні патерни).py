#=====================================================================================================
    # *Породжувальні патерни
# Породжувальні патерни турбуються про гнучке створення об'єктів без внесення до програми зайвих залежностей.
#=====================================================================================================
    #! Абстрактна фабрика (Abstract Factory) !
"""
Паттерн проектування, який дозволяє створювати сімейства пов'язаних об'єктів, не прив'язуючись до конкретних класів об'єктів, що створюються.
"""
#=====================================================================================================
from abc import ABC, abstractmethod


class AbstractReport(ABC):
    @abstractmethod
    def create_month_report(self):
        pass

    @abstractmethod
    def create_quarter_report(self):
        pass

    @abstractmethod
    def create_year_report(self):
        pass

class PdfReport(AbstractReport):
    def create_month_report(self):
        return PdfMonthReport()

    def create_quarter_report(self):
        return PdfQuarterReport()

    def create_year_report(self):
        return PdfYearReport()

class HtmlReport(AbstractReport):
    def create_month_report(self):
        return HtmlMonthReport()

    def create_quarter_report(self):
        return HtmlQuarterReport()

    def create_year_report(self):
        return HtmlYearReport()

class CsvReport(AbstractReport):
    def create_month_report(self):
        return CsvMonthReport()

    def create_quarter_report(self):
        return CsvQuarterReport()

    def create_year_report(self):
        return CsvYearReport()
#=====================================================================================================
    #! Фабричний метод (Factory Method) !
"""
Паттерн проектування, який визначає загальний інтерфейс для створення об'єктів в суперкласі, дозволяючи підкласам змінювати тип об'єктів, що створюються.
"""
#=====================================================================================================
from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def create(self):
        pass

    def send_messages(self) -> str:
        product = self.create()
        result = product.sending()
        return result

class SendingMessages(ABC):
    @abstractmethod
    def sending(self) -> str:
        pass

class CreatorPush(Creator):
    def create(self) -> SendingMessages:
        return SendingPushMessages()

class CreatorSMS(Creator):
    def create(self) -> SendingMessages:
        return SendingSMSMessages()

class SendingPushMessages(SendingMessages):
    def sending(self) -> str:
        return "Push mailing has been completed"

class SendingSMSMessages(SendingMessages):
    def sending(self) -> str:
        return "SMS mailing has been completed"

def client_code(creator: Creator) -> None:
    print("We know nothing about the creator code that works")
    result = creator.send_messages()
    print(f"Result: {result}")


if __name__ == "__main__":
    print("The application performs Push mailing lists.")
    client_code(CreatorPush())
    print("\n")

    print("The application performs SMS mailing.")
    client_code(CreatorSMS())
"""
The application performs Push mailing lists.
We know nothing about the creator code that works
Result: Push mailing has been completed


The application performs SMS mailing.
We know nothing about the creator code that works
Result: SMS mailing has been completed
"""
#=====================================================================================================
    #! Одинак (Singletone) !
"""
Паттерн проектування, який гарантує, що клас має лише один екземпляр і надає до нього глобальну точку доступу.
"""
#=====================================================================================================
import random

class Singleton:
    """Classic singleton"""
    __instance = None
    def __init__(self):
        self.number = random.randint(1, 10)

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(Singleton)
        return cls.__instance

class Regular:
    """Simple class to compare behavior"""
    def __init__(self, *args, **kwargs):
        self.number = random.randint(1, 10)

def testing():
    print("Singleton instances")
    list_singleton = [Singleton() for i in range(0, 5)]
    for index, element in enumerate(list_singleton):
        print(f"Element: {index}  number : {element.number}")

    print("Instances of a regular class")
    list_regular = [Regular() for i in range(0, 5)]
    for index, element in enumerate(list_regular):
        print(f"Element: {index}  number : {element.number}")


if __name__ == "__main__":
    testing()
"""
Singleton instances
Element: 0  number : 9
Element: 1  number : 9
Element: 2  number : 9
Element: 3  number : 9
Element: 4  number : 9
Instances of a regular class
Element: 0  number : 3
Element: 1  number : 3
Element: 2  number : 2
Element: 3  number : 6
Element: 4  number : 3
"""
#=====================================================================================================
