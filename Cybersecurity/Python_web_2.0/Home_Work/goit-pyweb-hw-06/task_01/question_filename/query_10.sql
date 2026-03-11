-- Завдання: Список курсів, які певному студенту читає певний викладач (студент=1, викладач=1).

SELECT DISTINCT sub.name
FROM subjects sub
JOIN grades g ON sub.id = g.subject_id
-- Комбінуємо умови: записи мають стосуватися конкретного студента,
-- а предмет повинен читатися конкретним викладачем.
WHERE g.student_id = 1 AND sub.teacher_id = 1;