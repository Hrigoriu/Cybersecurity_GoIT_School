import sys
import json
import logging
import asyncio
from datetime import datetime, timedelta
import aiohttp

# Налаштуємо логування для виводу помилок
logging.basicConfig(level=logging.ERROR, format="%(levelname)s: %(message)s")

# ==========================================
# Будемо дотримуватися приципу: S - Single Responsibility Principle
# Кожен клас виконує лише одну свою задачу.
# ==========================================


class PrivatBankAPI:
    """Стовримо клас, який відповідає ВИКЛЮЧНО за спілкування з API ПриватБанку."""

    BASE_URL = "https://api.privatbank.ua/p24api/exchange_rates"

    async def fetch_rates(self, session: aiohttp.ClientSession, date: str) -> dict:
        """
        Стовримо функція, яка асинхронно отримує сирі дані (JSON) за конкретну дату.
        """
        url = f"{self.BASE_URL}?date={date}"
        try:
            async with session.get(url) as response:  # Робимо GET-запит до API
                if response.status == 200:
                    return await response.json()  # Повертаємо розпарсений JSON
                else:
                    logging.error(f"Помилка API за {date}: Статус {response.status}")
                    return None
        except aiohttp.ClientError as e:
            # Обробка мережевих помилок (немає інтернету, сервер впав тощо)
            logging.error(f"Мережева помилка при запиті за {date}: {e}")
            return None
        except Exception as e:
            logging.error(f"Невідома помилка: {e}")
            return None


class RateParser:
    """
    Створимо клас, який відповідає ВИКЛЮЧНО за обробку сирих даних від API.
    O - Open/Closed Principle: Ми можемо легко додати нові валюти в __init__,
    не змінюючи логіку методу parse.
    """

    def __init__(self, target_currencies: tuple = ("EUR", "USD")):
        self.target_currencies = target_currencies

    def parse(self, raw_data: dict) -> dict:
        """
        Створимо функцію, яка витягує лише потрібні валюти та формує словник необхідної структури.
        """
        if not raw_data or "exchangeRate" not in raw_data:
            return {}

        date = raw_data.get("date")
        result = {date: {}}

        # Перебираємо всі валюти, які прийшли від банку
        for rate in raw_data["exchangeRate"]:
            currency = rate.get("currency")

            # Якщо ця валюта є в нашому цільовому списку (EUR або USD)
            if currency in self.target_currencies:
                # Беремо курс продажу та купівлі.
                # Використовуємо .get(), бо іноді банк може не повернути ці поля для деяких валют.
                sale = rate.get("saleRate") or rate.get("saleRateNB")
                purchase = rate.get("purchaseRate") or rate.get("purchaseRateNB")

                result[date][currency] = {"sale": sale, "purchase": purchase}

        return result


class CurrencyApp:
    """
    Створимо головний клас застосунку, який координує роботу API та Парсера.
    D - Dependency Inversion Principle: Залежить від абстракцій/інстансів,
    які ми йому передаємо, а не створює їх сам жорстко.
    """

    def __init__(self, api_client: PrivatBankAPI, parser: RateParser):
        self.api_client = api_client
        self.parser = parser

    def _generate_dates(self, days: int) -> list[str]:
        """Створимо функцію ,яка генерує список дат у форматі dd.mm.yyyy для останніх N днів."""
        dates = []
        today = datetime.today()
        for i in range(days):
            # Віднімаємо i днів від сьогоднішньої дати
            date_obj = today - timedelta(days=i)
            # Форматуємо дату як рядок (наприклад, 01.12.2014)
            dates.append(date_obj.strftime("%d.%m.%Y"))
        return dates

    async def get_rates_for_days(self, days: int) -> list[dict]:
        """
        Створимо головну функцію , яка створює сесію та запускає всі запити паралельно.
        """
        dates = self._generate_dates(days)
        final_result = []

        # Створюємо одну сесію для всіх запитів (це є швидше і правильніше)
        async with aiohttp.ClientSession() as session:
            # Створюємо список задач (coroutines)
            tasks = []
            for date in dates:
                # Додаємо задачу на виконання
                tasks.append(self.api_client.fetch_rates(session, date))

            # asyncio.gather запускає всі задачі ОДНОЧАСНО і чекає їх завершення
            raw_responses = await asyncio.gather(*tasks)

            # Обробляємо отримані відповіді
            for raw_data in raw_responses:
                if raw_data:
                    parsed_data = self.parser.parse(raw_data)
                    if parsed_data:
                        final_result.append(parsed_data)

        return final_result


# ==========================================
# Точка входу в програму (CLI)
# ==========================================
async def main():
    # 1. Логіка отримання кількості днів (через аргумент або консоль)
    if len(sys.argv) >= 2:
        # Якщо вводимо через консоль: python main.py 2
        try:
            days = int(sys.argv[1])
        except ValueError:
            print("Помилка: Кількість днів має бути цілим числом.")
            return
    else:
        # Якщо запустемо просто python main.py (або через кнопку в редакторі)
        user_input = input(
            "Введіть кількість днів для перевірки курсу (від 1 до 10): "
        ).strip()
        if not user_input:
            print("Ви не ввели кількість днів. Завершення роботи.")
            return
        try:
            days = int(user_input)
        except ValueError:
            print("Помилка: Кількість днів має бути цілим числом.")
            return

    # 2. Перевірка обмеження (не більше 10 днів)
    if days < 1 or days > 10:
        print("Помилка: Можна дізнатися курс лише за останні 1-10 днів.")
        return

    # 3. Ініціалізація компонентів (Збирання "конструктора")
    api = PrivatBankAPI()
    parser = RateParser(target_currencies=("EUR", "USD"))
    app = CurrencyApp(api_client=api, parser=parser)

    # 4. Запуск асинхронного процесу отримання даних
    try:
        results = await app.get_rates_for_days(days)
        # Виведення результату у красивому JSON форматі (з відступами)
        print(json.dumps(results, indent=2, ensure_ascii=False))
    except Exception as e:
        logging.error(f"Критична помилка виконання: {e}")


if __name__ == "__main__":
    # Спеціальна обробка для Windows, щоб уникнути помилок EventLoop
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # Запускаємо головну асинхронну функцію
    asyncio.run(main())
