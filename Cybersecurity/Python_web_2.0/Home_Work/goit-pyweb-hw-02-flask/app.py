from flask import Flask, render_template, request, redirect, url_for, flash
from address_book import AddressBook
from models import Record

app = Flask(__name__)
app.secret_key = 'secret_key_for_flash_messages'  # Потрібно для повідомлень

# Завантажуємо книгу при старті сервера
book = AddressBook.load()

@app.route('/')
def index():
    """Головна сторінка: список контактів"""
    contacts = list(book.data.values())
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    """Сторінка додавання контакту"""
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        
        if name and phone:
            # Використовуємо вашу логіку
            record = book.find(name) or Record(name)
            try:
                record.add_phone(phone)
                book.add_record(record)
                book.save()  # Зберігаємо одразу
                flash(f"Контакт {name} додано!", "success")
                return redirect(url_for('index'))
            except ValueError as e:
                flash(str(e), "danger")
        
    return render_template('add_contact.html')

@app.route('/delete/<name>')
def delete_contact(name):
    """Видалення контакту"""
    book.delete(name)
    book.save()
    flash(f"Контакт {name} видалено.", "warning")
    return redirect(url_for('index'))

@app.route('/birthdays')
def show_birthdays():
    """Сторінка найближчих днів народжень"""
    upcoming = book.get_upcoming_birthdays()
    return render_template('birthdays.html', birthdays=upcoming)

if __name__ == '__main__':
    # Запускаємо веб-сервер
    app.run(debug=True, host='0.0.0.0', port=5000)