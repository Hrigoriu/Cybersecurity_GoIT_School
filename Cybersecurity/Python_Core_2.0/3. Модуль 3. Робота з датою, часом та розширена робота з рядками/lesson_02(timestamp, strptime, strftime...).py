from datetime import datetime

# Поточний час
now = datetime.now()

# Конвертація datetime в timestamp
timestamp = datetime.timestamp(now)
print(timestamp)  # Виведе timestamp поточного часу
#====================================================================================
from datetime import datetime

# Припустимо, є timestamp
timestamp = 1617183600

# Конвертація timestamp назад у datetime
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)  # Виведе відповідний datetime
#====================================================================================
"""
datetime_object.strftime(format)

%Y - рік з чотирма цифрами (наприклад, 2023).
%y - рік з двома цифрами (наприклад, 23).
%m - місяць як номер (наприклад, 03 для березня).
%d - день місяця як номер (наприклад, 14).
%H - година (24-годинний формат) (наприклад, 15).
%I - година (12-годинний формат) (наприклад, 03).
%M - хвилини (наприклад, 05).
%S - секунди (наприклад, 09).
%A - повна назва дня тижня (наприклад, Tuesday).
%a - скорочена назва дня тижня (наприклад, Tue).
%B - повна назва місяця (наприклад, March).
%b або %h - скорочена назва місяця (наприклад, Mar).
%p - AM або PM для 12-годинного формату.

"""
#====================================================================================
from datetime import datetime

now = datetime.now()

# Форматування дати і часу
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date) 

# Форматування лише дати
formatted_date_only = now.strftime("%A, %d %B %Y")
print(formatted_date_only)

# Форматування лише часу
formatted_time_only = now.strftime("%I:%M %p")
print(formatted_time_only)  

# Форматування лише дати
formatted_date_only = now.strftime("%d.%m.%Y")
print(formatted_date_only)
#====================================================================================
from datetime import datetime

# Припустимо, у нас є дата у вигляді рядка
date_string = "2023.03.14"

# Перетворення рядка в об'єкт datetime
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу
#====================================================================================

