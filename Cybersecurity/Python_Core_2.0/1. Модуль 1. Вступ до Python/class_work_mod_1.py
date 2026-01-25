name = 'Hrigoriu'
age = 41
print(f"Моє ім'я: {name}, мій вік :{age}")
#============================================================================
rate = 1.68
value = 330
payment = rate * value
print(f"Вартість спожитої електроенергії {payment}")
#============================================================================
rate = 1.68
rate_night = rate / 2
value_day = 120
value_night = 80
payment = (value_day * rate) + (value_night * rate_night)
print(f"Загальна вартість споживання електроенергії: {payment:.2f} грн")
#============================================================================
first_name = "Hrigoriu"
last_name = "Programmer"
print(f"Ім'я: {first_name}, Прізвище: {last_name}")
#============================================================================
first_name = "Hrigoriu"
last_name = "Programmer"
full_name = first_name + " " + last_name
print(full_name)
#============================================================================
length = 2.75
width = 1.75
area = length * width
show = f'With width {width} and length {length} of the room, its area is equal to {area}'
print(show)
#============================================================================
is_active = True
is_delete = False
#============================================================================
name = "Hrigoriu"
age = 41
is_active = True
subscription = None
#============================================================================
length = "2.75"
width = "1.75"
area = float(length) * float(width)
show = f"With width {width} and length {length} of the room, its area is equal to {area}"
print(show)
#============================================================================
name = input("Enter your name: ")
email = input("Enter your email: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
is_active = bool(input("Do you want to receive notifications? (press Enter for No): "))
print(f"Name: {name}, Email: {email}, Age: {age}, Height: {height}")
#============================================================================
length = float(input("Enter room length: "))
width = float(input("Enter room width: "))
area = length * width
print(f"With width {width} and length {length} of the room, its area is equal to {area}")
#============================================================================
my_list = []
my_list.insert(0, 2024)
my_list.insert(1, 'Python')
my_list.insert(2, 3.12)
print(my_list)
#============================================================================
my_list = [2024, 3.12]
some_data = ['Python']
my_list.extend(some_data)
my_list.insert(1, 'Python')
my_list.reverse()

print(my_list)
#============================================================================
data = {}
data['year'] = 2024
data['lang'] = 'Python'
data['version'] = 3.12

print(data)
#============================================================================
cat = {}
cat["nick"] = "Simon"
cat["age"] = 7
cat["characteristics"] = ["лагідний", "кусається"]

age = cat.get("age")

info = {"status": "vaccinated", "breed": True}
cat.update(info)

print(cat)
print("Age from get():", age)
#============================================================================

