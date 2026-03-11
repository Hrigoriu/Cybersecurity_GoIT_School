-- ДОДАТКОВЕ Завдання 1: Середній бал, який певний викладач ставить певному студентові.

SELECT ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
-- Фільтруємо за конкретним студентом ТА конкретним викладачем.
WHERE g.student_id = 1 AND sub.teacher_id = 1;