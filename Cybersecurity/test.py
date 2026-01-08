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
