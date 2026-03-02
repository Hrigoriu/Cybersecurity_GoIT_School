"""
AIOHTTP — це асинхронний фреймворк, в якому реалізовано web-стек на основі asyncio в Python.
В AIOHTTP реалізовані клієнтська частина та серверна частина.
Клієнтська частина дозволяє виконувати HTTP-запити асинхронно, а серверна частина дозволяє створювати асинхронні веб-сервери.
AIOHTTP підтримує WebSocket, що дозволяє створювати двонаправлені комунікації між клієнтом і сервером в реальному часі.
"""

# pip install aiohttp
# =============================================================================================
# Виконання запиту
import platform

import aiohttp
import asyncio


async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get("https://python.org") as response:

            print("Status:", response.status)
            print("Content-type:", response.headers["content-type"])

            html = await response.text()
            print("Body:", html[:15], "...")


if __name__ == "__main__":
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

"""
Status: 200
Content-type: text/html; charset=utf-8
Body: <!doctype html> ...
"""
# =============================================================================================
"""
*data — byte об'єкт із тілом запиту;
*params — словник із набором параметрів запиту;
*json — Python об'єкт, який буде перетворений на JSON і надісланий серверу в тілі запиту;
*headers — словник, значення якого буде додано у заголовок запиту;
*cookies — словник з полями для кукі.
"""
# =============================================================================================
# Отримання відповіді сервера
import platform

import aiohttp
import asyncio


async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
        ) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers["content-type"])
            print("Cookies: ", response.cookies)
            print(response.ok)
            result = await response.json()
            return result


if __name__ == "__main__":
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    print(r)

"""
Status: 200
Content-type: application/json
Cookies:
True
[{'ccy': 'EUR', 'base_ccy': 'UAH', 'buy': '50.30000', 'sale': '51.30000'}, {'ccy': 'USD', 'base_ccy': 'UAH', 'buy': '42.77000', 'sale': '43.37000'}]
"""
# =============================================================================================
"""
*status — HTTP статус код відповіді сервера;
*headers — словник із полями заголовка;
*cookies — набір http cookies, якщо вони були передані;
*ok — спеціальне поле типу bool, яке має значення True, якщо запит був успішним, тобто його статус менше 400;
*json() — метод, який перетворює відповідь сервера з формату JSON у Python об'єкт.
"""
# =============================================================================================
