-- Завдання: Знайти оцінки студентів у окремій групі з певного предмета (наприклад, група=1, предмет=1).

SELECT s.fullname, g.grade, g.date_received
FROM students s
JOIN grades g ON s.id = g.student_id
-- Використовуємо оператор AND, щоб застосувати одразу дві умови:
-- 1. Студент з групи 1
-- 2. Оцінка з предмета 1
WHERE s.group_id = 1 AND g.subject_id = 1
-- Сортуємо від найновіших оцінок до найстаріших.
ORDER BY g.date_received DESC;