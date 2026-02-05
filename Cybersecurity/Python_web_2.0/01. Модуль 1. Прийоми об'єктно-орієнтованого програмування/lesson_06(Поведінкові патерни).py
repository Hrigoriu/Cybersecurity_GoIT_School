    # *Поведінкові патерни
# Поведінкові патерни піклуються про ефективну комунікацію між об'єктами.
# Ці патерни вирішують завдання ефективної та безпечної взаємодії між об'єктами програми.
#====================================================================================================
    #! Команда (Command) !
"""
Паттерн проектування, який перетворює запити на об'єкти, дозволяючи передавати їх як аргументи під час виклику методів, ставити запити в чергу, логувати їх, а також підтримувати скасування операцій.
"""
#====================================================================================================
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class CommandCreateXMLOrder(Command):
    def __init__(self, receiver, text: str) -> None:
        self._receiver = receiver
        self._text = text

    def execute(self) -> None:
        self._receiver.createXMLOrder(self._text)


class CommandSendEmail(Command):
    def __init__(self, receiver, html: str) -> None:
        self._receiver = receiver
        self._html = html

    def execute(self) -> None:
        self._receiver.send_email(self._html)


class Receiver:
    def createXMLOrder(self, text: str) -> None:
        print(f"Create XML order: {text} ")

    def send_email(self, text: str) -> None:
        print(f"Send email: {text} ")


class Invoker:
    def __init__(self) -> None:
        self._on_order = None
        self._on_email = None


    def set_on_order(self, command: Command):
        self._on_order = command

    def set_on_email(self, command: Command):
        self._on_email = command

    def generate_general_order(self) -> None:
        self._on_order.execute()
        self._on_email.execute()


def client():
    invoker = Invoker()
    invoker.set_on_order(CommandSendEmail(Receiver(), "Send email"))
    invoker.set_on_email(CommandCreateXMLOrder(Receiver(), "Save report"))
    invoker.generate_general_order()


if __name__ == "__main__":
    client()
"""
Send email: Send email 
Create XML order: Save report
"""
#====================================================================================================
    #! Спостерігач (Observer) !
"""
Паттерн проектування, який створює механізм підписки, що дозволяє одним об'єктам стежити і реагувати на події, що відбуваються в інших об'єктах.
"""
#====================================================================================================
from abc import ABC, abstractmethod


class Publisher(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class PublisherMessages(Publisher):
    _observers = []
    _indicator = 0

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def business_logic_execution(self):
        print(f"Application logic is being executed. Indicator: {self._indicator}")
        self._indicator += 1
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, publisher):
        pass


class ObserverA(Observer):
    def update(self, publisher):
        if publisher._indicator <= 3:
            print("ObserverA: reacts to the indicator less than 2")


class ObserverB(Observer):
    def update(self, publisher):
        if publisher._indicator > 2:
            print("ObserverB: reacts to the indicator greater than 2")


def client():
    publisher = PublisherMessages()

    observer_a = ObserverA()
    publisher.attach(observer_a)

    observer_b = ObserverB()
    publisher.attach(observer_b)

    publisher.business_logic_execution()
    publisher.business_logic_execution()
    publisher.detach(observer_a)
    publisher.business_logic_execution()


if __name__ == "__main__":

    client()

"""
Application logic is being executed. Indicator: 0
ObserverA: reacts to the indicator less than 2

Application logic is being executed. Indicator: 1
ObserverA: reacts to the indicator less than 2

Application logic is being executed. Indicator: 2
ObserverB: reacts to the indicator greater than 2
"""
#====================================================================================================
