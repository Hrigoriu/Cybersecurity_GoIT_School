-- Завдання: Знайти оцінки студентів у окремій групі з певного предмета (наприклад, група=3, предмет=4).

SELECT s.fullname, g.grade, g.date_received
FROM students s
    JOIN grades g ON s.id = g.student_id
-- Використовуємо оператор AND, щоб застосувати одразу дві умови:
-- 1. Студент з групи 3
-- 2. Оцінка з предмета 4
WHERE s.group_id = 3 AND g.subject_id = 4
-- Сортуємо від найновіших оцінок до найстаріших.
ORDER BY g.date_received DESC;