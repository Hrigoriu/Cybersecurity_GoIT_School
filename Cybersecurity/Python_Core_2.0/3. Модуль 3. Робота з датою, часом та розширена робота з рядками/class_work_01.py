from datetime import datetime


def string_to_date(date_string):
    """
    Перетворює рядок дати у форматі 'YYYY.MM.DD' на об'єкт datetime.date.
    """
    # Ми використовуємо strptime (String Parse Time), щоб "розпарсити" рядок.
    # %Y - рік (4 цифри), %m - місяць, %d - день.
    # .date() в кінці перетворює результат з 'datetime' (дата+час) просто в 'date' (дата).
    target_date = datetime.strptime(date_string, "%Y.%m.%d").date()
    return target_date


def date_to_string(date):
    """
    Перетворює об'єкт datetime.date на рядок у форматі 'YYYY.MM.DD'.
    """
    # Ми використовуємо strftime (String Format Time), щоб "відформатувати" дату в рядок.
    # Аргументи ті ж самі: %Y.%m.%d вказує, як саме розставити крапки та цифри.
    return date.strftime("%Y.%m.%d")


# --- Блок перевірки (щоб ви могли бачити результат) ---
if __name__ == "__main__":
    date_string = "2024.01.01"
    
    # 1. Перетворення рядка в дату
    converted_date = string_to_date(date_string)
    print(f"Перетворена дата (об'єкт): {converted_date}")
    print(f"Тип даних: {type(converted_date)}")
    
    # 2. Перетворення дати назад в рядок
    new_date_string = date_to_string(converted_date)
    print(f"Дата назад у рядок: {new_date_string}")
    print(f"Тип даних: {type(new_date_string)}")
# =================================================================================
from datetime import datetime


# Функція з попереднього кроку
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def prepare_user_list(user_data):
    """
    Приймає список словників з рядковими датами.
    Повертає новий список, де дати перетворені на об'єкти datetime.date.
    """
    prepared_list = []  # 1. Створюємо пустий кошик для нових даних
    
    for user in user_data:
        # 2. Витягуємо старі дані
        old_date_string = user["birthday"]
        
        # 3. Перетворюємо рядок на дату (використовуючи нашу функцію з кроку 1)
        converted_date = string_to_date(old_date_string)
        
        # 4. Створюємо новий словник для користувача з правильною датою
        new_user = {
            "name": user["name"],
            "birthday": converted_date
        }
        
        # 5. Кладемо готового користувача в кошик
        prepared_list.append(new_user)
        
    return prepared_list


# --- Блок перевірки ---
if __name__ == "__main__":
    users = [
        {"name": "Bill Gates", "birthday": "1955.3.25"},
        {"name": "Steve Jobs", "birthday": "1955.3.21"},
        {"name": "John Doe", "birthday": "1985.01.23"}
    ]

    prepared_users = prepare_user_list(users)
    print(prepared_users)
# =================================================================================

from datetime import datetime, timedelta


def string_to_date(date_string):
    """Допоміжна функція з 1-го кроку."""
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def find_next_weekday(start_date, weekday):
    """
    Знаходить дату наступного конкретного дня тижня після заданої дати.
    
    :param start_date: datetime.date - початкова дата
    :param weekday: int - день тижня (0=понеділок, 6=неділя)
    :return: datetime.date - дата наступного такого дня тижня
    """
    # 1. Дізнаємось, який день тижня зараз у start_date (0=Пн, 1=Вт...)
    current_weekday = start_date.weekday()
    
    # 2. Рахуємо різницю: "ціль" мінус "зараз".
    # Наприклад, хочемо П'ятницю (4), а зараз Вівторок (1). Різниця = 3 дні.
    days_ahead = weekday - current_weekday
    
    # 3. Якщо різниця <= 0, це означає, що цей день вже минув на цьому тижні
    # (або це сьогодні). Нам треба наступний тиждень, тому додаємо 7 днів.
    if days_ahead <= 0:
        days_ahead += 7
        
    # 4. Додаємо вираховану кількість днів до нашої дати
    # timedelta - це об'єкт, який представляє "проміжок часу"
    return start_date + timedelta(days=days_ahead)


# --- Блок перевірки ---
if __name__ == "__main__":
    start_date = string_to_date("2024.03.26")  # Це був вівторок
    
    # Шукаємо наступний понеділок (0)
    next_monday = find_next_weekday(start_date, 0)
    print(f"Початкова дата: {start_date}")
    print(f"Наступний понеділок: {next_monday}")  # Очікуємо 2024-04-01
    
    # Шукаємо наступну п'ятницю (4)
    next_friday = find_next_weekday(start_date, 4)
    print(f"Наступна п'ятниця: {next_friday}")  # Очікуємо 2024-03-29
#=================================================================================

from datetime import datetime, date


# --- Допоміжні функції з попередніх кроків ---
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


# --- Основна функція цього етапу ---
def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()

    for user in users:
        # 1. Беремо оригінальну дату народження
        birthday = user["birthday"]
        
        # 2. Формуємо дату народження в ЦЬОМУ році.
        # Використовуємо try-except для обробки людей, що народилися 29 лютого.
        # Якщо зараз не високосний рік, replace викине помилку.
        try:
            birthday_this_year = birthday.replace(year=today.year)
        except ValueError:
            # Якщо випало 29 лютого у невисокосний рік, святкуємо 1 березня
            birthday_this_year = birthday.replace(year=today.year, month=3, day=1)

        # 3. Рахуємо різницю в днях між ДН і сьогоднішнім днем
        delta_days = (birthday_this_year - today).days

        # 4. Перевіряємо умову:
        # ДН має бути сьогодні або в майбутньому (>= 0)
        # ДН має бути не далі ніж за 'days' днів (<= days)
        if 0 <= delta_days <= days:
            # Формуємо красиву дату для привітання
            congratulation_date_str = date_to_string(birthday_this_year)
            
            # Додаємо в список
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })

    return upcoming_birthdays


# --- Блок перевірки ---
if __name__ == "__main__":
    # Створюємо тестові дані.
    # УВАГА: Для коректної перевірки ми додаємо користувача з ДН "сьогодні" або "завтра"
    # залежно від того, коли ви запускаєте код. 
    # Припустимо, ми тестуємо логіку абстрактно.
    
    today = date.today()
    current_year = today.year
    
    raw_users = [
        {"name": "Sarah Lee", "birthday": "1957.03.30"},
        {"name": "John Doe", "birthday": "1985.03.28"},
        # Додамо когось, у кого ДН точно сьогодні/завтра для тесту
        {"name": "Birthday Boy", "birthday": f"2000.{today.month}.{today.day}"},
    ]
    
    # 1. Готуємо список (перетворюємо рядки в дати)
    users_prepared = prepare_user_list(raw_users)
    
    # 2. Шукаємо іменинників на найближчі 7 днів
    print(f"Сьогодні: {today}")
    results = get_upcoming_birthdays(users_prepared, 7)
    
    print("Кого вітати:")
    print(results)
#=================================================================================

from datetime import datetime, timedelta


# --- Допоміжні функції з попередніх кроків ---
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def find_next_weekday(start_date, weekday):
    """Знаходить наступний конкретний день тижня (0=Пн, ... 6=Нд)."""
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


# --- Основна функція цього етапу ---
def adjust_for_weekend(birthday):
    """
    Перевіряє, чи припадає дата на вихідний.
    Якщо так - повертає найближчий понеділок.
    Якщо ні - повертає дату без змін.
    """
    # 1. Перевіряємо день тижня.
    # У Python: 0=Понеділок ... 4=П'ятниця, 5=Субота, 6=Неділя.
    if birthday.weekday() >= 5:
        # 2. Якщо це Субота (5) або Неділя (6), шукаємо наступний Понеділок (0)
        return find_next_weekday(birthday, 0)
    
    # 3. Якщо це будній день, нічого не змінюємо
    return birthday


# --- Блок перевірки ---
if __name__ == "__main__":
    # Тест 1: Субота
    saturday_date = string_to_date("2024.03.30")  # Це була субота
    adjusted_sat = adjust_for_weekend(saturday_date)
    print(f"Субота {saturday_date} переноситься на -> {adjusted_sat} (Понеділок)")
    
    # Тест 2: Неділя
    sunday_date = string_to_date("2024.03.31")  # Це була неділя
    adjusted_sun = adjust_for_weekend(sunday_date)
    print(f"Неділя {sunday_date} переноситься на -> {adjusted_sun} (Понеділок)")

    # Тест 3: Вівторок (Будній день)
    tuesday_date = string_to_date("2024.03.26") 
    adjusted_tue = adjust_for_weekend(tuesday_date)
    print(f"Вівторок {tuesday_date} залишається -> {adjusted_tue}")
#=================================================================================

from datetime import datetime, date, timedelta

# --- Допоміжні функції (Кроки 1-5) ---


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday

# --- Основна функція (Крок 6 - Фінал) ---


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()

    for user in users:
        # 1. Конвертуємо дату народження у поточний рік
        # (Обробка виключення для 29 лютого)
        try:
            birthday_this_year = user["birthday"].replace(year=today.year)
        except ValueError:
            # Якщо 29 лютого, а рік невисокосний -> 1 березня
            birthday_this_year = user["birthday"].replace(year=today.year, month=3, day=1)

        # 2. Перевірка: чи вже минув цей день народження в цьому році?
        # Якщо так (наприклад, сьогодні грудень, а ДН був у січні),
        # то нас цікавить дата вже в НАСТУПНОМУ році.
        if birthday_this_year < today:
            try:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            except ValueError:
                 birthday_this_year = birthday_this_year.replace(year=today.year + 1, month=3, day=1)

        # 3. Перевіряємо, чи потрапляє дата у вікно "наступні N днів"
        if 0 <= (birthday_this_year - today).days <= days:
            
            # 4. Застосовуємо перенесення вихідних
            # (Якщо ДН випадає на суботу/неділю -> переносимо на понеділок)
            congratulation_date = adjust_for_weekend(birthday_this_year)

            # 5. Форматуємо результат та додаємо у список
            congratulation_date_str = date_to_string(congratulation_date)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })

    return upcoming_birthdays


# --- Блок перевірки ---
if __name__ == "__main__":
    # Список "сирих" даних
    users = [
        {"name": "Bill Gates", "birthday": "1955.03.25"},
        {"name": "Steve Jobs", "birthday": "1955.03.21"},
        {"name": "Jinny Lee", "birthday": "1956.03.22"},
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"}
    ]

    # Крок А: Готуємо список (String -> Date)
    prepared_users = prepare_user_list(users)
    
    # Крок Б: Знаходимо іменинників (наприклад, на 365 днів вперед, щоб побачити всіх)
    # Ми ставимо великий діапазон (365), щоб точно побачити роботу функції на прикладі.
    # У реальному житті тут буде days=7
    print(f"Сьогодні: {date.today()}")
    results = get_upcoming_birthdays(prepared_users, days=365) 
    
    print("\nСписок привітань (включаючи перенесення вихідних):")
    for item in results:
        print(item)
#====================================================================================

