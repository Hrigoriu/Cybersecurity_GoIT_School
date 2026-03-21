-- ДОДАТКОВЕ Завдання 2: Оцінки студентів у певній групі з певного предмета на останньому занятті.

SELECT s.fullname, g.grade, g.date_received
FROM grades g
    JOIN students s ON g.student_id = s.id
-- Фільтруємо за групою та предметом.
WHERE s.group_id = 3
    AND g.subject_id = 5
    -- Вкладений підзапит (Subquery):
    -- Замість того, щоб вказувати точну дату, ми просимо БД самостійно 
    -- знайти максимальну (найновішу) дату (MAX) для цієї групи та предмета.
    AND g.date_received = (
      SELECT MAX(g2.date_received)
    FROM grades g2
        JOIN students s2 ON g2.student_id = s2.id
    WHERE s2.group_id = 3 AND g2.subject_id = 5
  );