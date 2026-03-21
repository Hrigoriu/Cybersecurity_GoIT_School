from database.db import get_db_session
from repositories.analytics import AnalyticsRepository
from utils.logger import RetroLogger


def run_all_queries():
    """Контролер для демонстрації всіх 12 аналітичних запитів."""
    with get_db_session() as session:
        analytics = AnalyticsRepository(session)

        RetroLogger.info("ЗАПУСК АНАЛІТИЧНИХ ЗАПИТІВ")
        RetroLogger.data(f"1. Топ 5 студентів: {analytics.get_top_5_students()}")
        RetroLogger.data(
            f"2. Найкращий з предмета (ID 1): {analytics.get_best_student_by_subject(1)}"
        )
        RetroLogger.data(
            f"3. Середній бал у групах (Предмет 1): {analytics.get_avg_grade_by_groups_for_subject(1)}"
        )
        RetroLogger.data(
            f"4. Загальний середній бал: {analytics.get_overall_avg_grade()}"
        )
        RetroLogger.data(
            f"5. Курси викладача (ID 1): {analytics.get_courses_by_teacher(1)}"
        )
        RetroLogger.data(
            f"6. Студенти групи (ID 1): {analytics.get_students_by_group(1)}"
        )
        RetroLogger.data(
            f"7. Оцінки (Група 1, Предмет 1): {analytics.get_grades_in_group_for_subject(1, 1)}"
        )
        RetroLogger.data(
            f"8. Середній бал, що ставить викладач (ID 1): {analytics.get_avg_grade_given_by_teacher(1)}"
        )
        RetroLogger.data(
            f"9. Курси студента (ID 1): {analytics.get_courses_attended_by_student(1)}"
        )
        RetroLogger.data(
            f"10. Курси викладача (ID 1) для студента (ID 1): {analytics.get_courses_taught_to_student_by_teacher(1, 1)}"
        )
        RetroLogger.data(
            f"11. Середній бал від викладача (1) студенту (1): {analytics.get_avg_grade_from_teacher_to_student(1, 1)}"
        )
        RetroLogger.data(
            f"12. Оцінки на останньому занятті (Група 1, Предмет 1): {analytics.get_last_lesson_grades(1, 1)}"
        )


if __name__ == "__main__":
    run_all_queries()
