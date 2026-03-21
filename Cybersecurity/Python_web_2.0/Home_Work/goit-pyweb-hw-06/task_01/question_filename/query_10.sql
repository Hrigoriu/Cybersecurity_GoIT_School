-- Завдання: Список курсів, які певному студенту читає певний викладач (студент=24, викладач=6).

SELECT DISTINCT sub.name
FROM subjects sub
    JOIN grades g ON sub.id = g.subject_id
-- Комбінуємо умови: записи мають стосуватися конкретного студента,
-- а предмет повинен читатися конкретним викладачем.
WHERE g.student_id = 24 AND sub.teacher_id = 6;