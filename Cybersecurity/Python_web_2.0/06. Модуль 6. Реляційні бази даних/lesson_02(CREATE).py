# ====================================================================================================
# !Створення бази даних!
# ====================================================================================================
#! CREATE TABLE: Створюємо таблицю !
# ====================================================================================================
"""
CREATE TABLE genders (
  id INT PRIMARY KEY,
  name VARCHAR(30),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
# ====================================================================================================
"""
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(30),
  email VARCHAR(30),
  password VARCHAR(30),
  age TINYINT UNSIGNED,
  gender_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (gender_id) REFERENCES genders (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
"""
# ====================================================================================================
"""
CREATE TABLE contacts (
  id INT PRIMARY KEY,
  name VARCHAR(30),
  email VARCHAR(30),
  phone VARCHAR(30),
  favorite BOOLEAN,
  user_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""
# ====================================================================================================