"""
Парсинг - це процес збирання інформації з веб-сторінок.
Це може бути корисно для збору даних, аналізу контенту або автоматизації завдань.
У цьому уроці ми розглянемо бібліотеку Beautiful Soup,
яка є потужним інструментом для парсингу HTML та XML документів.
"""
# ===============================================================================================
"""
Для парсингу використаємо такі бібліотеки:
- Beautiful Soup,
- Lxml,
- Requests.
"""
# ===============================================================================================
"""
Для швидкого збору даних з однієї сторінки BeautifulSoup підходить на 100%.
"""
# ===============================================================================================
"""
import requests
from bs4 import BeautifulSoup


url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

print(soup)
# Виведе весь HTML код сторінки
"""
# ===============================================================================================
"""
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')

print(quotes)
# Виведе список всіх цитат на сторінці
"""
# ===============================================================================================
"""
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')

for quote in quotes:
    print(quote.text)
# Виведе текст кожної цитати на сторінці
"""
# ===============================================================================================
"""
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('small', class_='author')

for quote in quotes:
    print(quote.text)
# Виведе імена авторів цитат на сторінці
"""
# ===============================================================================================
"""
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print('--' + authors[i].text)
    tagsforquote = tags[i].find_all('a', class_='tag')
    for tagforquote in tagsforquote:
        print(tagforquote.text)
    break
# Виведе першу цитату, її автора та теги
# Якщо потрібно отримати всі цитати з цієї сторінки, закоментуйте break.
"""
# ===============================================================================================
