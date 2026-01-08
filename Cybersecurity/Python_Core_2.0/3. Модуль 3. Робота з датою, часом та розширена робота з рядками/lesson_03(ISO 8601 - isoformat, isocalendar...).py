"""
Формат дати в ISO 8601 виглядає як "YYYY-MM-DD", де:

YYYY - це рік (наприклад, 2023),
MM - місяць (наприклад, 01 для січня),
DD - день (наприклад, 31).

Формат часу в ISO 8601 виглядає як "HH:MM:SS", де:

HH - години (від 00 до 23),
MM - хвилини (від 00 до 59),
SS - секунди (від 00 до 59, іноді з додатковими десятковими частинами для мікросекунд).
"""
#====================================================================================
from datetime import datetime

# Поточна дата та час
now = datetime.now()

# Конвертація у формат ISO 8601
iso_format = now.isoformat()
print(iso_format)
#====================================================================================
from datetime import datetime

iso_date_string = "2023-03-14T12:39:29.992996"

# Конвертація з ISO формату
date_from_iso = datetime.fromisoformat(iso_date_string)
print(date_from_iso)
#====================================================================================
from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Використання isoweekday() для отримання дня тижня
day_of_week = now.isoweekday()

print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня
#====================================================================================
from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Отримання ISO календаря
iso_calendar = now.isocalendar()

print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")
#====================================================================================

