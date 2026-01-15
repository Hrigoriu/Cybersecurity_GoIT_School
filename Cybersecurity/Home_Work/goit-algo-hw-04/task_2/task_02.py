"""
        Друге завдання

У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою.

Наприклад:
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5

Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.

Вимоги до завдання:
1. Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
2. Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
3. Функція має повертати список словників, де кожен словник містить інформацію про одного кота.

Рекомендації для виконання:
1. Використовуйте with для безпечного читання файлу.
2. Пам'ятайте про встановлення кодування при відкриті файлів
3. Для кожного рядка в файлі використовуйте split(',') для отримання ідентифікатора, імені та віку кота.
4. Утворіть словник з ключами "id", "name", "age" для кожного кота та додайте його до списку, який буде повернуто.
5. Опрацьовуйте можливі винятки, пов'язані з читанням файлу.

Критерії оцінювання:
1. Функція має точно обробляти дані та повертати правильний список словників.
2. Повинна бути належна обробка винятків і помилок.
3. Код має бути чистим, добре структурованим і зрозумілим.

Приклад використання функції:
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)

Очікуваний результат:
[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]
"""

from pathlib import Path


def get_cats_info(path: str | Path) -> list[dict]:
    """
    Функція читає файл з даними про котів та повертає список словників.
    :param path: Шлях до текстового файлу.
    :return: Список словників з ключами 'id', 'name', 'age'.    
    """
    cats_list = []
    file_path = Path(path)  # Конвертуємо у Path об'єкт

    try:
        with file_path.open("r", encoding="utf-8") as file:
            for line in file:
                # Видалимо пробіли та перенос рядка
                stripped_line = line.strip()               

                # Пропустимо порожні рядки
                if not stripped_line:
                    continue

                # Розіб'ємо рядок на частини
                parts = stripped_line.split(',')

                # Перевіримо, чи є рівно 3 елементи (id, name, age)
                if len(parts) != 3:
                    print(f"Попередження: Некоректний формат рядка -> {stripped_line}")
                    continue
                
                # Розпакуємо змінні 
                cat_id, name, age = parts

                # Додамо до списку
                cats_list.append({
                    "id": cat_id,
                    "name": name,
                    "age": age 
                })

    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено за шляхом '{file_path.absolute()}'")
        return []
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
        return []

    return cats_list


# --- Блок тестування ---
if __name__ == "__main__":
    # 1. Створимо тестове середовище через pathlib
    current_dir = Path(__file__).parent
    data_dir = current_dir / "data"
    data_dir.mkdir(exist_ok=True)
    
    file_path = data_dir / "cats_file.txt"
    
    # Запишемо тестові дані (включаючи "биті" рядки для перевірки надійності)
    content = """60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
Broken line without commas
60b90c3b13067a15887e1ae4,Simon,12

60b90c4613067a15887e1ae5,Tessi,5"""

    with file_path.open("w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Файл створено: {file_path}")

    # 2. Виклик функції
    cats_info = get_cats_info(file_path)
    
    print("\nОтриманий список котів:")
    for cat in cats_info:
        print(cat)
