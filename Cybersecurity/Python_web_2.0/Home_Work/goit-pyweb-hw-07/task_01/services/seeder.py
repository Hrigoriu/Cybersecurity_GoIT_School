# Шлях до файлу: services/seeder.py
import sys
import os

# Додаємо корінь проєкту до PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import faker
import random
from sqlalchemy.orm import Session
from database.models import Group, Teacher, Student, Subject, Grade
from utils.logger import RetroLogger


class DatabaseSeeder:
    """Сервісний шар для наповнення бази даних (Seeding)."""

    def __init__(self, session: Session):
        self.session = session
        self.fake = faker.Faker("uk_UA")

    def execute(self):
        RetroLogger.info("Ініційовано протокол Seed...")
        try:
            # Генерація Груп
            groups = [Group(name=f"Група-{i}") for i in ["А", "Б", "В"]]
            self.session.add_all(groups)
            self.session.commit()

            # Генерація Викладачів
            teachers = [Teacher(fullname=self.fake.name()) for _ in range(5)]
            self.session.add_all(teachers)
            self.session.commit()

            # Генерація Предметів
            subject_names = [
                "Rust Програмування",
                "Штучний Інтелект",
                "Комп'ютерне бачення",
                "DevOps",
                "Бази Даних",
            ]
            subjects = [
                Subject(name=name, teacher_id=random.choice(teachers).id)
                for name in subject_names
            ]
            self.session.add_all(subjects)
            self.session.commit()

            # Генерація Студентів
            students = [
                Student(fullname=self.fake.name(), group_id=random.choice(groups).id)
                for _ in range(40)
            ]
            self.session.add_all(students)
            self.session.commit()

            # Генерація Оцінок
            grades = []
            for student in students:
                for _ in range(random.randint(10, 20)):
                    grades.append(
                        Grade(
                            student_id=student.id,
                            subject_id=random.choice(subjects).id,
                            grade=random.randint(60, 100),
                            date_received=self.fake.date_between(
                                start_date="-1y", end_date="today"
                            ),
                        )
                    )
            self.session.add_all(grades)
            self.session.commit()

            RetroLogger.data("Протокол Seed завершено успішно. БД наповнена.")
        except Exception as e:
            RetroLogger.error(f"Помилка Seed: {e}")
            self.session.rollback()
            raise


if __name__ == "__main__":
    from database.db import get_db_session

    with get_db_session() as session:
        seeder = DatabaseSeeder(session)
        seeder.execute()
