-- Спочатку видаляємо існуючі таблиці (якщо вони є), щоб уникнути помилок при повторному запуску скрипта.
-- Порядок видалення важливий: спочатку видаляємо таблиці, які посилаються на інші (grades), 
-- а в кінці - ті, на які посилаються (groups, teachers).
DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS subjects;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS groups;

-- 1. Створимо групи таблиць
CREATE TABLE groups (
    -- PRIMARY KEY - унікальний ідентифікатор рядка. AUTOINCREMENT - БД сама збільшуватиме ID (1, 2, 3...)
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    -- Назва групи, обмеження NOT NULL означає, що поле не може бути порожнім
    name VARCHAR(50) NOT NULL
);

-- 2. Створимо таблицю викладачів
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(150) NOT NULL -- Повне ім'я викладача
);

-- 3. Створимо таблицю студентів
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(150) NOT NULL,
    group_id INTEGER, -- Поле для зв'язку з таблицею груп
    -- FOREIGN KEY встановлює зв'язок між group_id у цій таблиці та id у таблиці groups
    FOREIGN KEY (group_id) REFERENCES groups (id)
      -- Якщо групу видалять, всі її студенти також будуть видалені (CASCADE)
      ON DELETE CASCADE
      -- Якщо ID групи зміниться, це оновиться і у студентів
      ON UPDATE CASCADE
);

-- 4. Створимо таблицю предметів
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(150) NOT NULL,
    teacher_id INTEGER, -- Поле для зв'язку з викладачем (хто читає предмет)
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- 5. Створимо таблицю оцінок
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER, -- Кому поставили оцінку
    subject_id INTEGER, -- З якого предмета
    -- CHECK гарантує, що в базу не запишуть оцінку < 1 або > 100
    grade INTEGER CHECK (grade >= 1 AND grade <= 100), 
    date_received DATE NOT NULL, -- Дата отримання оцінки
    
    -- Зв'язок зі студентами
    FOREIGN KEY (student_id) REFERENCES students (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
    -- Зв'язок з предметами
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);