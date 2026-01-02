import calendar
from datetime import datetime

def display_current_month_calendar():
    # Отримання поточної дати
    now = datetime.now()
    # Отримання поточного року і місяця
    current_year = now.year
    current_month = now.month

    # Створення об'єкта календаря
    cal = calendar.TextCalendar()
    # Відображення календаря поточного місяця
    cal_text = cal.formatmonth(current_year, current_month)
    print(cal_text)

# Виклик функції для відображення календаря поточного місяця
display_current_month_calendar()
