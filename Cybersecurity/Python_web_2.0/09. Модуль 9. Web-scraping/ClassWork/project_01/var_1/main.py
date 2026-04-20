import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Book, Base


def parse_data():
    rate_to_number = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    url = 'https://books.toscrape.com/'
    store_ = []

    html_doc = requests.get(url)

    if html_doc.status_code == 200:
        soup = BeautifulSoup(html_doc.content, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        for book in books:
            img_src = book.find('img')['src']
            img_url = urljoin(url, img_src)

            rating = rate_to_number.get(
                book.find('p', class_='star-rating')['class'][1]
            )

            title = book.find('h3').find('a')['title']

            price_text = book.find('p', class_='price_color').text
            price = float(''.join(ch for ch in price_text if ch.isdigit() or ch == '.'))

            store_.append({
                'img_url': img_url,
                'rating': rating,
                'title': title,
                'price': price
            })
    else:
        print(f"Помилка запиту: {html_doc.status_code}")

    return store_


if __name__ == '__main__':
    store = parse_data()
    print(f"Знайдено книг: {len(store)}")

    engine = create_engine("sqlite:///books.db")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for el in store:
        book = Book(
            img_url=el.get('img_url'),
            rating=el.get('rating'),
            title=el.get('title'),
            price=el.get('price')
        )
        session.add(book)

    session.commit()

    books = session.query(Book).all()
    for b in books:
        print(vars(b))

    session.close()
