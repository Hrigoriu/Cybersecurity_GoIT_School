import sqlite3
import faker
from random import randint

# Налаштуємо кількість записів для генерації
NUMBER_GROUPS = 3
NUMBER_STUDENTS = 40
NUMBER_TEACHERS = 4
NUMBER_SUBJECTS = 6
MAX_GRADES_PER_STUDENT = 15


def generate_fake_data() -> tuple:
    """Створимо функцію для генерації випадкових даних для таблиць бази даних.
    Використовуємо генератор даних з допомогою бібліотеки Faker."""
    # Ініціалізуємо Faker з українською локалізацією для створення реалістичних імен
    fake = faker.Faker("uk_UA")

    # 1. Створюємо список кортежів для груп. Кожен кортеж містить 1 елемент: (назва_групи,)
    groups = [("Група А",), ("Група Б",), ("Група В",)]

    # 2. Генеруємо викладачів. Викликаємо fake.name() вказану кількість разів.
    teachers = [(fake.name(),) for _ in range(NUMBER_TEACHERS)]

    # 3. Генеруємо предмети.
    subject_names = [
        "Вища математика",
        "Програмування",
        "Фізика",
        "Історія України",
        "Англійська мова",
        "Бази даних",
    ]
    # Для кожного предмета випадково обираємо ID викладача (від 1 до NUMBER_TEACHERS)
    subjects = [
        (subject_names[i], randint(1, NUMBER_TEACHERS)) for i in range(NUMBER_SUBJECTS)
    ]

    # 4. Генеруємо студентів. Призначаємо їм випадковий ID групи (від 1 до NUMBER_GROUPS)
    students = [
        (fake.name(), randint(1, NUMBER_GROUPS)) for _ in range(NUMBER_STUDENTS)
    ]

    # 5. Генеруємо оцінки
    grades = []
    # Проходимо по кожному студенту (їхні ID від 1 до NUMBER_STUDENTS)
    for student_id in range(1, NUMBER_STUDENTS + 1):
        # Вирішуємо, скільки оцінок матиме цей студент
        num_grades = randint(1, MAX_GRADES_PER_STUDENT)
        for _ in range(num_grades):
            # Обираємо випадковий предмет (ID від 1 до NUMBER_SUBJECTS)
            subject_id = randint(1, NUMBER_SUBJECTS)
            # Ставимо оцінку від 60 до 100 балів
            grade = randint(60, 100)
            # Генеруємо дату за останній рік
            date_received = fake.date_between(start_date="-1y", end_date="today")
            # Додаємо кортеж у загальний список
            grades.append((student_id, subject_id, grade, date_received))

    return groups, teachers, subjects, students, grades


def insert_data_to_db(groups, teachers, subjects, students, grades):
    """Створимо функцію, яка буде зберігати згенеровані дані у базу даних."""
    with sqlite3.connect("university.db") as con:
        cur = con.cursor()

        # executemany виконує один SQL-запит багато разів для кожного кортежу у списку.
        # Знаки питання (?) - це плейсхолдери, що захищають від SQL-ін'єкцій.
        cur.executemany("INSERT INTO groups (name) VALUES (?)", groups)
        cur.executemany("INSERT INTO teachers (fullname) VALUES (?)", teachers)
        cur.executemany(
            "INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", subjects
        )
        cur.executemany(
            "INSERT INTO students (fullname, group_id) VALUES (?, ?)", students
        )
        cur.executemany(
            "INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)",
            grades,
        )

        # Зберігаємо транзакцію
        con.commit()
    print("Базу даних успішно наповнено випадковими даними!")


if __name__ == "__main__":
    # Отримуємо дані і відразу передаємо їх у функцію запису
    groups, teachers, subjects, students, grades = generate_fake_data()
    insert_data_to_db(groups, teachers, subjects, students, grades)
