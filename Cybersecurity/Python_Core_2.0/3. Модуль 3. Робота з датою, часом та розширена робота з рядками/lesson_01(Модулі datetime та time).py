import datetime
now = datetime.datetime.now()
print(now)
print("Year:", now.year)
print("Month:", now.month)  
#====================================================================================

from datetime import datetime

current_datetime = datetime.now()

print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
print(current_datetime.tzinfo)
print(current_datetime.date())
#====================================================================================
from datetime import datetime

current_datetime = datetime.now()
print(current_datetime.date())
print(current_datetime.time())
print(current_datetime)
#====================================================================================
import datetime

# Створення об'єктів date і time
date_part = datetime.date(2023, 12, 14)
time_part = datetime.time(12, 30, 15)

# Комбінування дати і часу в один об'єкт datetime
combined_datetime = datetime.datetime.combine(date_part, time_part)

print(combined_datetime)  # Виведе "2023-12-14 12:30:15"
#====================================================================================
import datetime

# Створення об'єкта datetime з конкретною датою
specific_date = datetime.datetime(year=2020, month=1, day=7)

print(specific_date)  # Виведе "2020-01-07 00:00:00"
#====================================================================================
import datetime

# Створення об'єкта datetime з конкретною датою і часом
specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)

print(specific_datetime)  # Виведе "2020-01-07 14:30:15"
#====================================================================================
import datetime

# Створення об'єкта datetime з конкретною датою і часом
specific_datetime = datetime.datetime(2020, 1, 7, 14, 30, 15)

print(specific_datetime)  # Виведе "2020-01-07 14:30:15"
#====================================================================================
from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Отримання номера дня тижня
day_of_week = now.weekday()

# Поверне число від 0 (понеділок) до 6 (неділя)
print(f"Сьогодні: {day_of_week}")  
#====================================================================================
from datetime import datetime

# Створення двох об'єктів datetime
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

# Порівняння дат
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)  # True, тому що datetime1 передує datetime2
print(datetime1 > datetime2)  # False, тому що datetime1 не наступає за datetime2
print(datetime1 <= datetime2)  # True, тому що datetime1 передує datetime2
print(datetime1 >= datetime2)  # False, тому що datetime1 не наступає за datetime2
#====================================================================================
from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)
# Виведе: 64 days, 8:05:27.010010
#====================================================================================
from datetime import datetime

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)  # 365 days, 0:00:00
print(difference.total_seconds())  # 31536000.0
#====================================================================================
from datetime import datetime, timedelta

now = datetime.now()
future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
print(future_date)
#====================================================================================
from datetime import datetime, timedelta

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00
#====================================================================================
from datetime import datetime

# Створення об'єкта datetime
date = datetime(year=2023, month=12, day=18)

# Отримання порядкового номера
ordinal_number = date.toordinal()
print(f"Порядковий номер дати {date} становить {ordinal_number}")
#====================================================================================
from datetime import datetime

# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# Поточна дата
current_date = datetime.now()

# Розрахунок кількості днів
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since)
#====================================================================================

