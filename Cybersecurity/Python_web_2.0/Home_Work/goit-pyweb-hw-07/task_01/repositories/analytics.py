from sqlalchemy import func, desc
from sqlalchemy.orm import Session
from database.models import Student, Grade, Group, Subject, Teacher


class AnalyticsRepository:
    """Репозиторій для виконання складних аналітичних запитів до БД."""

    def __init__(self, session: Session):
        self.session = session

    def get_top_5_students(self):
        return (
            self.session.query(
                Student.fullname,
                func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            )
            .select_from(Grade)
            .join(Student)
            .group_by(Student.id)
            .order_by(desc("avg_grade"))
            .limit(5)
            .all()
        )

    def get_best_student_by_subject(self, subject_id: int):
        return (
            self.session.query(
                Student.fullname,
                func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            )
            .select_from(Grade)
            .join(Student)
            .filter(Grade.subject_id == subject_id)
            .group_by(Student.id)
            .order_by(desc("avg_grade"))
            .limit(1)
            .first()
        )

    def get_avg_grade_by_groups_for_subject(self, subject_id: int):
        return (
            self.session.query(
                Group.name, func.round(func.avg(Grade.grade), 2).label("avg_grade")
            )
            .select_from(Grade)
            .join(Student)
            .join(Group)
            .filter(Grade.subject_id == subject_id)
            .group_by(Group.id)
            .all()
        )

    def get_overall_avg_grade(self):
        return self.session.query(func.round(func.avg(Grade.grade), 2)).scalar()

    def get_courses_by_teacher(self, teacher_id: int):
        return (
            self.session.query(Subject.name)
            .filter(Subject.teacher_id == teacher_id)
            .all()
        )

    def get_students_by_group(self, group_id: int):
        return (
            self.session.query(Student.fullname)
            .filter(Student.group_id == group_id)
            .order_by(Student.fullname)
            .all()
        )

    def get_grades_in_group_for_subject(self, group_id: int, subject_id: int):
        return (
            self.session.query(Student.fullname, Grade.grade, Grade.date_received)
            .select_from(Grade)
            .join(Student)
            .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
            .all()
        )

    def get_avg_grade_given_by_teacher(self, teacher_id: int):
        return (
            self.session.query(func.round(func.avg(Grade.grade), 2).label("avg_grade"))
            .select_from(Grade)
            .join(Subject)
            .filter(Subject.teacher_id == teacher_id)
            .scalar()
        )

    def get_courses_attended_by_student(self, student_id: int):
        return (
            self.session.query(Subject.name)
            .select_from(Grade)
            .join(Subject)
            .filter(Grade.student_id == student_id)
            .distinct()
            .all()
        )

    def get_courses_taught_to_student_by_teacher(
        self, student_id: int, teacher_id: int
    ):
        return (
            self.session.query(Subject.name)
            .select_from(Grade)
            .join(Subject)
            .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
            .distinct()
            .all()
        )

    def get_avg_grade_from_teacher_to_student(self, student_id: int, teacher_id: int):
        return (
            self.session.query(func.round(func.avg(Grade.grade), 2))
            .select_from(Grade)
            .join(Subject)
            .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
            .scalar()
        )

    def get_last_lesson_grades(self, group_id: int, subject_id: int):
        subquery = (
            self.session.query(func.max(Grade.date_received))
            .join(Student)
            .filter(Grade.subject_id == subject_id, Student.group_id == group_id)
            .scalar_subquery()
        )
        return (
            self.session.query(Student.fullname, Grade.grade, Grade.date_received)
            .select_from(Grade)
            .join(Student)
            .filter(
                Student.group_id == group_id,
                Grade.subject_id == subject_id,
                Grade.date_received == subquery,
            )
            .all()
        )
