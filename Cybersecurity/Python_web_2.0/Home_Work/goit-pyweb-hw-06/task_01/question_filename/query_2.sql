-- Завдання: Знайти студента із найвищим середнім балом з певного предмета (наприклад, предмет з ID=1).

SELECT s.fullname, ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
-- Фільтруємо дані: залишаємо лише оцінки, що належать предмету з ID 1.
WHERE g.subject_id = 1
GROUP BY s.id
ORDER BY avg_grade DESC
-- Нам потрібен лише 1 студент (з найвищим балом), тому ліміт = 1.
LIMIT 1;