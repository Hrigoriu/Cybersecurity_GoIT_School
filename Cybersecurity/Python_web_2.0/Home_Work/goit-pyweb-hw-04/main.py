# Імпортуємо необхідні інструменти (бібліотеки) для нашої програми
import mimetypes  # Допоможе зрозуміти тип файлу (чи це картинка, чи текст, чи CSS)
import pathlib  # Допоможе створити шляхи до папок та файлів
from http.server import (
    HTTPServer,
    BaseHTTPRequestHandler,
)  # Класи для створення веб-сервера, який може обробляти запити від браузера
import urllib.parse  # Допоможе розібрати складні веб-адреси та текст з форм на прості шматочки
import socket  # Допоможе створити канал зв'язку між двома частинами програми (HTTP-сервером і Socket-сервером)
import threading  # Допоможе створити потоки, щоб сервер міг робити кілька речей одночасно
import json  # Допоможе створити формат для збереження даних у вигляді словника, який легко читати і писати
from datetime import datetime  # ІнстДопоможе для роботи з точним часом

# import os         # Інструмент для роботи з операційною системою

# ==========================================
# 1. НАЛАШТУВАННЯ (КОНСТАНТИ)
# ==========================================
HTTP_PORT = 3000  # Порт, де працює наш веб-сервер (куди ми будемо заходити через браузер, наприклад, http://localhost:3000)
SOCKET_PORT = (
    5000  # Порт, де працює наш Socket-сервер (куди ми будемо відправляти дані з форми)
)
SOCKET_HOST = "127.0.0.1"  # Локальна адреса (означає "на цьому ж самому комп'ютері")
STORAGE_DIR = pathlib.Path(
    "storage"
)  # Шлях до папки, де будуть зберігатися наші записи
DATA_FILE = (
    STORAGE_DIR / "data.json"
)  # Точний шлях до файлу з даними (storage/data.json)

# ==========================================
# 2. ПІДГОТОВКА РОБОЧОГО МІСЦЯ
# ==========================================
# Створимо папку 'storage', якщо її ще немає.
# exist_ok=True означає "якщо папка вже є, не сварися і не видавай помилку".
STORAGE_DIR.mkdir(parents=True, exist_ok=True)

# Перевіримо, чи існує файл data.json. Якщо ні — створюємо порожній.
if not DATA_FILE.exists():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        # Запишемо туди порожній словник {}, щоб файл не був зовсім пустим
        json.dump({}, f)


# ==========================================
# 3. HTTP-СЕРВЕР (ЯКИЙ ОБСЛУГОВУЄ БРАУЗЕР)
# ==========================================
class HttpHandler(BaseHTTPRequestHandler):
    """
    Створимо клас, який буде вказувати веб-серверу, як реагувати на запити від браузера.
    Браузер може просити сторінку (GET) або відправляти дані форми (POST).
    """

    def do_GET(self):
        """
        Створимо функцію do_GET, який спрацьовує, коли користувач просто вводить адресу або переходить за посиланням.
        """
        # Розбираємо адресу, яку попросив браузер (наприклад, http://localhost:3000/message.html)
        pr_url = urllib.parse.urlparse(self.path)

        # Маршрутизація (вирішуємо, куди направити клієнта)
        if pr_url.path == "/":
            # Якщо адреса пуста (корінь) - даємо головну сторінку
            self.send_html_file("index.html")
        elif pr_url.path == "/message.html":
            # Якщо попросили форму - даємо сторінку з формою
            self.send_html_file("message.html")
        else:
            # Якщо це не головна і не форма, це картинка або CSS-стилі
            if pathlib.Path().joinpath(pr_url.path[1:]).exists():
                self.send_static()  # Віддаємо файл (картинку/стилі)
            else:
                # Якщо такого файлу взагалі немає, віддаємо сторінку помилки 404
                self.send_html_file("error.html", 404)

    def do_POST(self):
        """
        Створимо функцію do_POST, який спрацьовує, коли клієнт натискає кнопку "Send" у формі.
        Тобто клієнт передає нам заповнену анкету.
        """
        # Спочатку дізнаємося, якого розміру прийшла посилка (скільки там літер)
        content_length = int(self.headers["Content-Length"])
        # Читаємо ці дані (отримуємо "байт-рядок", тобто сирі дані)
        data = self.rfile.read(content_length)

        # Передаємо ці дані нашому другому серверу
        self.send_data_to_socket(data)

        # Повертаємося на головну сторінку" (Редирект 302)
        self.send_response(302)
        self.send_header("Location", "/")
        self.end_headers()

    def send_html_file(self, filename, status=200):
        """
        Створимо функцію, яка гарно пакує HTML-сторінку і відправляє браузеру
        filename - це назва файлу, який ми хочемо віддати (наприклад, index.html)
        """
        self.send_response(status)  # Кажемо, що все добре (200) або що помилка (404)
        self.send_header(
            "Content-type", "text/html"
        )  # Попереджаємо, що це саме HTML-текст
        self.end_headers()  # Завершуємо підготовку пакування

        # Відкриваємо файл на комп'ютері і читаємо його по байтах ('rb')
        with open(filename, "rb") as fd:
            # Відправляємо вміст файлу прямо у вікно браузера
            self.wfile.write(fd.read())

    def send_static(self):
        """
        Створимо функцію, яка буде відправляти картинки або CSS файли
        (наприклад, коли браузер просить logo.png або styles.css)"""
        self.send_response(200)  # Відповідаємо "Все ок, файл знайдено"
        # Програма сама вгадує тип файлу (чи це .png, чи .css)
        mt = mimetypes.guess_type(self.path)[0]
        if mt:
            self.send_header("Content-type", mt)
        else:
            self.send_header(
                "Content-type", "text/plain"
            )  # Якщо не вгадали, кажемо, що це просто текст
        self.end_headers()

        # Відкриваємо і відправляємо сам файл (наприклад, logo.png)
        with open(f".{self.path}", "rb") as file:
            self.wfile.write(file.read())

    def send_data_to_socket(self, data):
        """Створимо функцію, яка бере дані і кидає їх через 'вікно' (UDP) до Socket-сервера"""
        try:
            # Створюємо спеціальний канал зв'язку - UDP (без встановлення з'єднання, просто кидаємо дані)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Відправляємо сирі дані на адресу 127.0.0.1 та порт 5000
            sock.sendto(data, (SOCKET_HOST, SOCKET_PORT))
            sock.close()  # Закриваємо канал
        except Exception as e:
            # Якщо щось пішло не так, просто друкуємо помилку в консоль
            print(f"Помилка відправки даних на socket: {e}")


# ==========================================
# 4. ЗАПУСК СЕРВЕРІВ (ФУНКЦІЇ ДЛЯ ПОТОКІВ)
# ==========================================


def run_http_server():
    """
    Створимо функцію, яка включає HTTP-сервер (який обслуговує клієнтів)
    """
    server_address = ("", HTTP_PORT)  # Слухаємо запити звідусіль на порту 3000
    http = HTTPServer(server_address, HttpHandler)
    print(f"HTTP сервер запущено на порту {HTTP_PORT}")
    try:
        # Сервер буде працювати постійно, поки ми його не вимкнемо
        http.serve_forever()
    except KeyboardInterrupt:
        # Якщо ми натиснемо Ctrl+C в терміналі, сервер зупиниться
        http.server_close()


def run_socket_server():
    """Створимо функцію, яка включає Socket-сервер (який приймає дані від HTTP-сервера і зберігає їх у файл)"""
    # Створюємо сокет (точку прийому інформації)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = (SOCKET_HOST, SOCKET_PORT)
    sock.bind(server)  # Прив'язуємо сокет до нашої адреси і порту 5000
    print(f"Socket сервер запущено на {SOCKET_HOST}:{SOCKET_PORT}")

    try:
        while True:  # Безкінечний цикл - сервер завжди готовий приймати дані
            # Чекаємо на повідомлення. recvfrom чекає, поки не прилетить порція даних (до 1024 байт)
            data, address = sock.recvfrom(1024)
            print(f"Отримано дані від {address}")

            # Дані приходять у вигляді багатьох символів типу username=Tom&message=Hi
            # urllib.parse.unquote_plus перетворює символи (як %20) назад у нормальні пробіли
            data_parse = urllib.parse.unquote_plus(data.decode())

            # Перетворюємо цей текст на зручний словник: {'username': 'Tom', 'message': 'Hi'}
            # Ми розбиваємо текст по '&', а потім по '='
            data_dict = {
                key: value
                for key, value in [el.split("=") for el in data_parse.split("&")]
            }

            # Намагаємося прочитати, що вже є в нашому файлі data.json
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    current_data = json.load(
                        f
                    )  # Перетворюємо json-текст у словник Python
            except (FileNotFoundError, json.JSONDecodeError):
                # Якщо файл пустий або зіпсований, починаємо з чистого аркуша (порожнього словника)
                current_data = {}

            # Беремо поточний час (з мілісекундами) і робимо з нього текстовий рядок
            time_now = str(datetime.now())

            # Додаємо у наш загальний словник новий запис.
            # Ключ - це час, значення - це словник з іменем і повідомленням.
            current_data[time_now] = data_dict

            # Зберігаємо все назад у файл data.json
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                # json.dump записує словник у файл.
                # indent=2 робить гарні відступи, ensure_ascii=False дозволяє зберігати українські літери
                json.dump(current_data, f, indent=2, ensure_ascii=False)

    except KeyboardInterrupt:
        # Примусове закриття сокета, якщо ми зупинили програму
        sock.close()


# ==========================================
# 5. ГОЛОВНИЙ БЛОК (ЗАПУСК ПРОГРАМИ)
# ==========================================
if __name__ == "__main__":
    # Оскільки програма не може одночасно чекати на сторінки від браузера і на повідомлення UDP,
    # ми розділяємо її на "два потоки" (Threads).

    # Потік №1: займається веб-сторінками
    thread_http = threading.Thread(target=run_http_server)
    # Потік №2: займається збереженням повідомлень у файл
    thread_socket = threading.Thread(target=run_socket_server)

    # Даємо команду обом потокам почати роботу
    thread_http.start()
    thread_socket.start()

    # join() каже головній програмі: "не закінчуй роботу, поки ці потоки не завершать свою"
    # Оскільки потоки працюють у безкінечних циклах (serve_forever та while True),
    # програма буде працювати, поки користувач її не зупинить (наприклад, через Ctrl+C).
    thread_http.join()
    thread_socket.join()
