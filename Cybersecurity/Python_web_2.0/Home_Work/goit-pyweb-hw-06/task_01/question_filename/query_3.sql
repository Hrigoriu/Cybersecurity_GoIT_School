-- Завдання: Знайти середній бал у групах з певного предмета (наприклад, ID=3).

SELECT gr.name, ROUND(AVG(g.grade), 2) AS avg_grade
FROM groups gr
    -- Щоб дістатися від групи до оцінок, нам потрібні 2 JOIN-и:
    -- 1. Приєднуємо студентів цієї групи
    JOIN students s ON gr.id = s.group_id
    -- 2. Приєднуємо оцінки цих студентів
    JOIN grades g ON s.id = g.student_id
-- Враховуємо лише конкретний предмет
WHERE g.subject_id = 3
-- Групуємо за ID групи, щоб показати середній бал для кожної групи окремо.
GROUP BY gr.id;