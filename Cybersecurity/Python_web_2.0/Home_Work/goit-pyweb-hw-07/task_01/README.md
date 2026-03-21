# 🎓 University Data Management System (PostgreSQL + SQLAlchemy)

Цей проєкт — це комплексна система управління даними університету, побудована з використанням сучасного стеку Python. Проєкт використовує **PostgreSQL** як основну базу даних, **SQLAlchemy** як ORM (Об'єктно-реляційне відображення) для взаємодії з даними та **Alembic** для керування міграціями.

Застосунок реалізує багаторівневу архітектуру (Layered Architecture) з дотриманням принципів **SOLID**, **DRY** та стандартів **PEP 8**, а також містить повноцінний консольний інтерфейс (CLI) для виконання CRUD-операцій у стилі Retro-Tech Terminal.

---

## 🚀 Основні можливості

- CRUD-операції для:
  - груп
  - студентів
  - викладачів
  - предметів
- аналітичні SQLAlchemy ORM-запити:
  - `JOIN`
  - `GROUP BY`
  - підзапити
  - агрегати
- генерація тестових даних
- підтримка міграцій через Alembic
- консольний інтерфейс у стилі **Retro-Tech Terminal**

---

## 🛠 Технологічний стек

 **Мова програмування:** Python 3.10+
 **СУБД:** PostgreSQL (у Docker-контейнері)
 **ORM:** SQLAlchemy 2.0+
 **Керування міграціями:** Alembic
 **Генерація тестових даних:** Faker

---

## 🧱 Архітектура проєкту

Проєкт побудований за принципом **багатошарової архітектури (Layered Architecture)**.

Проєкт розділено на логічні шари для забезпечення легкості підтримки та масштабування:

## Шари

- **Config Layer** — конфігурація застосунку, змінні оточення
- **Database Layer** — engine, session factory, базові ORM-компоненти
- **Model Layer** — ORM-моделі таблиць
- **Repository Layer** — доступ до даних (CRUD, запити)
- **Service Layer** — бізнес-логіка
- **Controller Layer** — CLI-контролери / сценарії запуску
- **Utility Layer** — логування, допоміжні інструменти

---

```text
university_project/
│
├── README.md               # Документація проєкту
├── requirements.txt        # Список залежностей Python
├── config.py               # Конфігураційний шар (завантаження змінних оточення)
├── main.py                 # Головний CLI-контролер для CRUD-операцій
├── run_analytics.py        # Скрипт для демонстрації 12 аналітичних вибірок
│
├── alembic.ini             # Головний конфігураційний файл Alembic
├── alembic/                # Директорія міграцій
│   ├── env.py              # Файл налаштування середовища Alembic
│   └── versions/           # Згенеровані файли міграцій
│
├── database/               # Шар роботи з базою даних
│   ├── db.py               # Налаштування з'єднання (Engine, Session)
│   └── models.py           # Опис ORM-моделей (структура таблиць)
│
├── repositories/           # Шар доступу до даних (Data Access Layer)
│   ├── base.py             # Базовий репозиторій для CRUD-операцій
│   └── analytics.py        # Репозиторій зі складними аналітичними запитами
│
├── services/               # Шар бізнес-логіки
│   └── seeder.py           # Скрипт-генератор фейкових даних (Faker)
│
└── utils/                  # Шар утиліт
    └── logger.py           # Утиліта для стилізованого консольного виводу (Retro-Tech) логування  
```

🚀 Покрокова інструкція з розгортання

1. Запуск бази даних (Docker)
Для ізоляції бази даних використовується Docker. Відкрийте термінал та виконайте команду для створення та запуску контейнера з PostgreSQL:
docker run --name pg-university \
  -p 5433:5432 \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=your_strong_password_here \
  -e POSTGRES_DB=university_db \
  -d postgres:16

---

## Пояснення

 --name pg-university — ім’я контейнера
 -p 5433:5432 — порт контейнера PostgreSQL
 POSTGRES_USER — користувач БД
 POSTGRES_PASSWORD — пароль БД
 POSTGRES_DB — база даних, яка створиться автоматично
 -d — запуск у фоновому режимі

---

Запустіть Docker
    Bash: docker run --name pg-university -p 5433:5432 -e POSTGRES_PASSWORD=supermysecretpassword -d postgres

Примітка: Контейнер працюватиме у фоновому режимі (-d), прокидаючи стандартний порт PostgreSQL 5432 на ваш локальний комп'ютер.

---

2.Встановлення залежностей
Встановлення необхідних бібліотек

 **Через pip
    Bash: pip install -r requirements.txt

 **Вручну
    Bash: pip install sqlalchemy psycopg2-binary alembic faker

---

3.Ініціалізація та налаштування Alembic (Міграції)
Alembic відповідає за перенесення структури ваших Python-моделей у реальні таблиці бази даних.
Ініціалізуйте Alembic у проєкті (виконується один раз):
    Bash: alembic init alembic

---

Після цього буде створено:
*папку alembic/
*файл alembic.ini

---

Якщо не має файлу alembic.ini, то:
щоб Alembic згенерував його сам "з нуля", ви можете використати такий трюк у терміналі:
  Виконайте команду: alembic init temp_folder (це створить тимчасову папку і новий файл .ini).
  Перемістіть створений файл temp_folder/alembic.ini у корінь вашого проєкту.
  Видаліть папку temp_folder.
  
  ---

Потім пропиши У файлі alembic.ini:
sqlalchemy.url = postgresql://postgres:supermysecretpassword@127.0.0.1:5433/postgres

---

4.Налаштуйте файл alembic/env.py згідно з архітектурою проєкту (імпорт Base та settings), щоб Alembic мав доступ до моделей та рядка підключення.

alembic/env.py має:
*імпортувати Base з database.db
*імпортувати settings з config.py
*підставляти settings.database_url
*імпортувати database.models, щоб Alembic бачив метадані

``` text
import sys
from pathlib import Path
from logging.config import fileConfig

from sqlalchemy import create_engine, pool
from alembic import context

# Налаштування шляхів до проєкту
root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root))

# Імпортуємо наші налаштування та моделі
from config import settings
from database.models import Base

...

target_metadata = Base.metadata
...
def run_migrations_offline() -> None:
    """Offline режим"""
    url = settings.database_url
...
def run_migrations_online() -> None:
    """Online режим. Використовуємо Engine напряму з config.py, щоб уникнути помилки авторизації"""
    connectable = create_engine(
        settings.database_url,
        poolclass=pool.NullPool,
    )
....

```

---

Концептуально:
*target_metadata = Base.metadata
*config.set_main_option("sqlalchemy.url", settings.database_url)

---

5.Виконання міграцій
*Згенеруйте першу міграцію на основі ваших моделей:
    Bash
alembic revision --autogenerate -m "Init tables"
alembic revision --autogenerate -m "Second tables"

*Застосуйте міграцію до бази даних (фізичне створення таблиць):
    Bash
alembic upgrade head

---

6.Наповнення бази даних (Seeding)
Щоб застосунок мав з чим працювати, наповніть його випадковими даними (студенти, викладачі, предмети, групи, оцінки).
    Bash
python -m services.seeder

Очікуваний результат:
створені групи
створені викладачі
створені студенти
створені предмети
створені оцінки

У консолі має з'явитися повідомлення від RetroLogger про успішне заповнення бази даних.

---

📊 Використання застосунку
**1. Аналітичні вибірки
У файлі repositories/analytics.py реалізовано 12 складних запитів через SQLAlchemy ORM (з використанням JOIN, GROUP BY, Subqueries).
Щоб перевірити їхню роботу та побачити результати, запустіть контролер аналітики:
    Bash
python run_analytics.py

**2. Управління даними (CLI Застосунок)
Проєкт включає зручний консольний інтерфейс (main.py) для виконання CRUD-операцій (Створення, Читання, Оновлення, Видалення) над будь-якою моделлю бази даних.

Синтаксис команд:
```python main.py -a <action> -m <model> [-i <id>] [-n <name>]```

Доступні дії (-a): create, list, update, remove
Доступні моделі (-m): Group, Teacher, Student, Subject

Приклади використання:
*Створити нового викладача:
    Bash
python main.py -a create -m Teacher -n "Борис Джонсонюк"
python main.py -a create -m Teacher -n "Ілон Маск"

*Отримати список всіх студентів:
    Bash
python main.py -a list -m Student

Переглянути список усіх груп:
    Bash
python main.py -a list -m Group

Оновити ім'я студента з ID 5:
    Bash
python main.py -a update -m Student -i 5 -n "Нове Ім'я Студента"
python main.py -a update -m Student -i 7 -n "Дональд Трамп"

Видалити предмет з ID 2:
    Bash
python main.py -a remove -m Subject -i 2

Увага: Завдяки налаштуванню cascade="all, delete-orphan", видалення сутності (наприклад, викладача) призведе до автоматичного каскадного видалення пов'язаних з нею даних (предметів та оцінок з цих предметів), забезпечуючи цілісність бази даних.

Приклади наслідків
*видалення Teacher → може видалити Subject
*видалення Subject → може видалити Grade
*видалення Group → може видалити Student
*видалення Student → може видалити Grade

🖥️✨ Розроблено як демонстрацію передових практик програмування на Python та взаємодії з реляційними базами даних !
