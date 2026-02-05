#=====================================================================================================
    # *Структурні патерни
# Структурні патерни показують різноманітні способи побудови зв'язків між об'єктами.
#=====================================================================================================
    #! Фасад (Facade) !
"""
Паттерн проектування, який надає простий інтерфейс до складної системі класів, бібліотеки або фреймворку.
"""
#=====================================================================================================
class FacadeNewsletter:
    def __init__(self, users_system, email_system) -> None:
        self._users_system = users_system
        self._email_system = email_system

    def sending(self) -> str:
        users = self._users_system.get_users()
        male, female = self._users_system.separate_users(users)
        text_for_male = self._email_system.get_text_email("male")
        text_for_female = self._email_system.get_text_email("female")
        self._email_system.send_emails(male, text_for_male)
        self._email_system.send_emails(female, text_for_female)
        return "Done"


class UsersSystem:
    def get_users(self) -> list:
        users = [
            {
                "name": "Allen Raymond",
                "email": "nulla.ante@vestibul.co.uk",
                "gender": "male",
            },
            {
                "name": "Chaim Lewis",
                "email": "dui.in@egetlacus.ca",
                "gender": "male",
            },
            {
                "name": "Kennedy Lane",
                "email": "mattis.Cras@nonenimMauris.net",
                "gender": "female",
            },
            {
                "name": "Wylie Pope",
                "email": "est@utquamvel.net",
                "gender": "female",
            },
        ]
        return users

    def separate_users(self, users) -> tuple:
        male = []
        female = []
        for person in users:
            if person.get("gender", None) == "male":
                male.append(person)
            else:
                female.append(person)
        return male, female


class EmailSystem:
    def get_text_email(self, gender) -> str:
        text = "Default text"
        if gender == "male":
            text = "Male text email"
        if gender == "female":
            text = "Female text email"

        return text

    def send_emails(self, users, text) -> str:
        for person in users:
            print(f"Send {person.get('name')} email: {text}")
        return "Done"


def client_code(newsletter) -> None:
    print(newsletter.sending(), end="")


if __name__ == "__main__":
    facade = FacadeNewsletter(UsersSystem(), EmailSystem())
    client_code(facade)
"""
Send Allen Raymond email: Male text email
Send Chaim Lewis email: Male text email
Send Kennedy Lane email: Female text email
Send Wylie Pope email: Female text email
Done
"""
#=====================================================================================================
    #! Адаптер !
"""
Патерн проектування, що дозволяє об'єктам з несумісними інтерфейсами працювати разом. 
"""
#=====================================================================================================
[
  {
    'ccy': 'EUR',
    'base_ccy': 'UAH',
    'buy': '37.89060',
    'sale': '39.06250'
  },
  {
    'ccy': 'USD',
    'base_ccy': 'UAH',
    'buy': '36.56860',
    'sale': '37.45318'
  }
]
#====================================================================================================
{
  'EUR': {
    'buy': 37.8906,
    'sale': 39.0625
  },
  'USD': {
    'buy': 36.5686,
    'sale': 37.45318
  }
}
#====================================================================================================
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
"""
| currency |   sale   |   buy    |
|   EUR    | 51.54639 |  50.84   |
|   USD    | 43.10345 |  42.65   |
"""
#====================================================================================================
    #! Заступник (Proxy) !
"""
Паттерн проектування, який дозволяє підставляти замість реальних об'єктів спеціальні об'єкти-замінники.
"""
#====================================================================================================
from abc import ABC, abstractmethod
from time import time, sleep

class Request(ABC):
    @abstractmethod
    def request(self) -> None:
        pass

class RealRequest(Request):
    def request(self) -> None:
        print("RealRequest: Handling request.")
        sleep(0.5)

class Proxy(Request):
    def __init__(self, real_request) -> None:
        self._real_request = real_request
        self.start = None

    def request(self) -> None:
        self.start = time()
        self._real_request.request()
        self.log_access()

    def log_access(self) -> None:
        print(f"Proxy: Logging the time of request. {time() - self.start}")


def client_code(subject) -> None:
    subject.request()


if __name__ == "__main__":
    proxy = Proxy(RealRequest())
    client_code(proxy)
"""
RealRequest: Handling request.
Proxy: Logging the time of request. 0.5041468143463135
"""
#====================================================================================================