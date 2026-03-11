-- Завдання: Знайти середній бал, який ставить певний викладач зі своїх предметів (наприклад, викладач=1).

SELECT t.fullname, ROUND(AVG(g.grade), 2) AS avg_given_grade
FROM teachers t
-- Щоб дістатися від викладача до оцінки, робимо 2 JOIN-и:
-- 1. Знаходимо предмети цього викладача
JOIN subjects sub ON t.id = sub.teacher_id
-- 2. Знаходимо оцінки, поставлені за ці предмети
JOIN grades g ON sub.id = g.subject_id
WHERE t.id = 1
GROUP BY t.id;