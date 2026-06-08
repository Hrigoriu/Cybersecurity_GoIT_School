# 📞 Contact Manager REST API

Проект розроблений з використанням багатошарової архітектури та стилізований під Retro-Tech Terminal.
Проєкт дотримується принципів SOLID та DRY, використовуючи паттерни Controller, Service та Repository.

## Асинхронний стек: FastAPI + SQLAlchemy 2.0 (asyncpg) + PostgreSQL + Pydantic v2

---

## Зміст

- [📞 Contact Manager REST API](#-contact-manager-rest-api)
  - [Асинхронний стек: FastAPI + SQLAlchemy 2.0 (asyncpg) + PostgreSQL + Pydantic v2](#асинхронний-стек-fastapi--sqlalchemy-20-asyncpg--postgresql--pydantic-v2)
  - [Зміст](#зміст)
  - [Архітектура проєкту](#архітектура-проєкту)
    - [📁 Структура проекту](#-структура-проекту)
  - [1 . Змінні оточення та залежності .env](#1--змінні-оточення-та-залежності-env)
  - [2 . Конфігурація та Логування (Retro-Tech Style)](#2--конфігурація-та-логування-retro-tech-style)
  - [3 . Робота з базою даних (ORM та Підключення)](#3--робота-з-базою-даних-orm-та-підключення)
  - [4 . Схеми Pydantic (Валідація)](#4--схеми-pydantic-валідація)
  - [5 . Шари Repository та Service](#5--шари-repository-та-service)
  - [6 . Controller (API Роутер)](#6--controller-api-роутер)
  - [7 . Точка Входу (Main)](#7--точка-входу-main)
  - [8 . Створи базу даних для цього проєкту в pgAdmin](#8--створи-базу-даних-для-цього-проєкту-в-pgadmin)
  - [9 . Онови файл .env](#9--онови-файл-env)
  - [💻10 .Запустити проект можна командою](#10-запустити-проект-можна-командою)
  - [Приклади](#приклади)
    - [🎛 Спосіб 1: Інтерактивна панель (Рекомендовано)](#-спосіб-1-інтерактивна-панель-рекомендовано)
      - [Крок 1: Створення контактів (POST /contacts/)](#крок-1-створення-контактів-post-contacts)
      - [Крок 2: Отримання списку (GET /contacts/)](#крок-2-отримання-списку-get-contacts)
      - [Крок 3: Пошук контактів (GET /contacts/search/)](#крок-3-пошук-контактів-get-contactssearch)
      - [Крок 4: Дні народження (GET /contacts/birthdays/)](#крок-4-дні-народження-get-contactsbirthdays)
      - [Крок 5: Оновлення (PATCH /contacts/{contact\_id})](#крок-5-оновлення-patch-contactscontact_id)
      - [Крок 6: Видалення (DELETE /contacts/{contact\_id})](#крок-6-видалення-delete-contactscontact_id)
    - [💻 Спосіб 2: Тест через термінал (Для хакерської атмосфери)](#-спосіб-2-тест-через-термінал-для-хакерської-атмосфери)
      - [Створити контакт](#створити-контакт)
      - [Отримати всіх](#отримати-всіх)
  - [👨‍💻 Автор](#-автор)
  - [📄 Ліцензія](#-ліцензія)

---

## Архітектура проєкту

### 📁 Структура проекту

```text
├── .env                  # Секрети та конфігурація (НІКОЛИ не комітити в Git)
├── app/
│   ├── api/
│   │   └── contacts.py   # Controller: Ендпоінти (Routing)
│   ├── core/
│   │   ├── config.py     # Налаштування (Pydantic Settings)
│   │   └── logger.py     # Retro-Tech Terminal логер
│   ├── db/
│   │   ├── database.py   # Підключення до БД (PostgreSQL)
│   │   └── models.py     # SQLAlchemy ORM моделі
│   ├── repositories/
│   │   └── contact.py    # Repository: Робота з БД (CRUD + Search)
│   ├── schemas/
│   │   └── contact.py    # Pydantic моделі (Валідація)
│   ├── services/
│   │   └── contact.py    # Service: Бізнес-логіка
│   └── main.py           # Точка входу FastAPI
```

---

## 1 . Змінні оточення та залежності .env

/.env
Використовуй Poetry для встановлення пакетів:

```text
poetry add fastapi uvicorn sqlalchemy asyncpg pydantic pydantic-settings python-dotenv email-validator
```

## 2 . Конфігурація та Логування (Retro-Tech Style)

- app/core/config.py
- app/core/logger.py

---

## 3 . Робота з базою даних (ORM та Підключення)

- app/db/database.py
- app/db/models.py

---

## 4 . Схеми Pydantic (Валідація)

app/schemas/contact.py

---

## 5 . Шари Repository та Service

- app/repositories/contact.py
- app/services/contact.py

---

## 6 . Controller (API Роутер)

app/api/contacts.py

---

## 7 . Точка Входу (Main)

app/main.py

---

## 8 . Створи базу даних для цього проєкту в pgAdmin

- Відкрий pgAdmin (або DBeaver/Datagrip).
- Натисни правою кнопкою миші на Databases -> Create -> Database...
- Назви її, наприклад, contacts_db і збережи.

---

## 9 . Онови файл .env

Твій поточний файл .env (згідно з шаблоном) має значення retro_admin та super_secret_password.
Тобі треба замінити їх на ТВОЇ реальні дані.

Відкрий файл .env у своєму проєкті та відредагуй його.
Наприклад, якщо твій користувач postgres, а пароль 123456, він має виглядати так:

```text
Code snippet
POSTGRES_USER=postgres
POSTGRES_PASSWORD=123456 (твій_реальний_пароль_сюди)
POSTGRES_DB=contacts_db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

(Переконайся, що між знаком дорівнює = та значенням немає пробілів).

---

## 💻10 .Запустити проект можна командою

```text
poetry run uvicorn app.main:app --reload
```

---

## Приклади

### 🎛 Спосіб 1: Інтерактивна панель (Рекомендовано)

Відкрий браузер і перейди за адресою: http://127.0.0.1:8000/docs
Ти побачиш гарний інтерфейс з усіма твоїми ендпоінтами.

Щоб протестувати будь-який з них, натисни на нього, потім натисни кнопку "Try it out" (Спробувати), введи дані та натисни "Execute" (Виконати).

Ось сценарій тестування (виконуй по черзі):

---

#### Крок 1: Створення контактів (POST /contacts/)

Давай створимо двох користувачів. Сьогодні 4 червня, тому одному з них зробимо день народження 8 червня (щоб перевірити пошук іменинників).

Встав цей JSON у поле contact_in і натисни Execute:

```text
{
  "first_name": "Neo",
  "last_name": "Anderson",
  "email": "neo@matrix.com",
  "phone": "+380501234567",
  "birthday": "1990-06-08",
  "additional_info": "The One"
}
```

Потім створи ще одного:

```text
{
  "first_name": "Trinity",
  "last_name": "Unknown",
  "email": "trinity@matrix.com",
  "phone": "+380671234567",
  "birthday": "1995-12-15",
  "additional_info": "Hacker"
}
```

---

#### Крок 2: Отримання списку (GET /contacts/)

Відкрий цей ендпоінт, натисни "Try it out" і просто "Execute" (ліміти можна не міняти). Ти маєш отримати масив з двома своїми контактами і побачити їхні id (швидше за все 1 та 2).

---

#### Крок 3: Пошук контактів (GET /contacts/search/)

Введи в поле q частину імені, наприклад, neo або matrix.
Натисни Execute. Ти маєш отримати лише ті контакти, які збігаються із запитом.

---

#### Крок 4: Дні народження (GET /contacts/birthdays/)

Просто натисни Execute. Система повинна повернути лише Neo, оскільки його день народження (8 червня) потрапляє у вікно наступних 7 днів.

---

#### Крок 5: Оновлення (PATCH /contacts/{contact_id})

Давай змінимо номер телефону для Neo.
У поле contact_id введи 1.
У поле contact_in введи лише ті дані, які хочеш змінити (інші можна видалити, адже ми використовували Optional у схемі):

```text
{
  "phone": "+380999999999"
}
```

Натисни Execute. Відповідь покаже оновлений контакт.

---

#### Крок 6: Видалення (DELETE /contacts/{contact_id})

Введи contact_id = 2 (Trinity) і натисни Execute.
Сервер поверне код 204 No Content (успішно видалено). Якщо ти знову викличеш список всіх контактів (Крок 2), Трініті там вже не буде.

---

### 💻 Спосіб 2: Тест через термінал (Для хакерської атмосфери)

Якщо хочеш відчути себе справжнім кібер-інженером, відкрий нову вкладку PowerShell (не зупиняючи сервер)

Натисни клавішу Win (Пуск), введи PowerShell та відкрий його.
(Його екран зазвичай синій, або шлях починається з PS C:\>).

Cпробуй відправити запит безпосередньо з командного рядка:

#### Створити контакт

```text
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/contacts/" -ContentType "application/json" -Body '{"first_name": "Morpheus", "last_name": "Captain", "email": "morpheus@nebuchadnezzar.com", "phone": "123123123", "birthday": "1970-01-01", "additional_info": "Red pill provider"}'
```

#### Отримати всіх

```text
Invoke-RestMethod -Method Get -Uri "http://127.0.0.1:8000/contacts/"
```

---

## 👨‍💻 Автор

**[SYS_ADMIN] Hrigoriu Programmer**
`Python Backend Developer (learning path)// Web 2.0 & Cyber-Security Student`

**[CORE_MODULES_LOADED]:** FastAPI | Async PostgreSQL | SQLAlchemy ORM | Layered Architecture | RESTful API

---

## 📄 Ліцензія

Цей проєкт створено для навчальних цілей та демонстрації навичок побудови архітектури.
