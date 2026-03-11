import sqlite3
import os


def execute_query_from_file(filename):
    """
    Створимо функцію, яка отримує шлях до SQL-файлу, зчитує з нього запит
    і виконує його в базі даних, гарно виводячи результати.
    """
    # 1. Захист від помилок: перевіряємо, чи взагалі існує вказаний файл.
    if not os.path.exists(filename):
        print(f"Помилка: Файл '{filename}' не знайдено. Перевірте правильність шляху!")
        return  # Якщо файлу немає, перериваємо виконання функції

    # 2. Відкриваємо знайдений файл для читання ("r").
    # Вказуємо encoding="utf-8", щоб правильно читати український текст у коментарях.
    with open(filename, "r", encoding="utf-8") as f:
        sql = f.read()  # Зберігаємо весь текст запиту у змінну

    # 3. Підключаємося до нашої бази даних.
    with sqlite3.connect("university.db") as con:
        cur = con.cursor()

        try:
            cur.execute(sql)  # Виконуємо запит
            results = cur.fetchall()  # Забираємо всі результати (список кортежів)

            print(f"\n--- Результати для файлу: {filename} ---")

            # cur.description містить інформацію про колонки, які повернув запит.
            # description - це список кортежів, де 0-й елемент - це назва колонки.
            if cur.description:
                col_names = [desc[0] for desc in cur.description]
                # Виводимо назви колонок, з'єднавши їх символом "|"
                print(" | ".join(col_names))
                print("-" * 50)  # Лінія для відділення заголовка від даних

            # 4. Перевірка наявності даних
            if not results:
                print(
                    "Дані відсутні. Можливо, згенеровані випадкові дані не відповідають заданим ID (наприклад, студент не має оцінок з цього предмета)."
                )
            else:
                # Виводимо кожен рядок результату
                for row in results:
                    print(row)

        except sqlite3.Error as e:
            # Якщо у SQL-файлі є синтаксична помилка, програма не "впаде", а виведе текст помилки.
            print(f"Помилка виконання SQL: {e}")


# Точка входу в програму
if __name__ == "__main__":
    # Папка в якій лежать запити
    directory_name = "question_filename"

    # Цикл від 1 до 12 включно
    for i in range(1, 13):
        # os.path.join - це найкращий спосіб зшити шляхи.
        # Він автоматично поставить правильний слеш ( / для Mac/Linux або \ для Windows).
        # Результат буде по типу: question_filename/query_1.sql, question_filename/query_2.sql тощо.
        filepath = os.path.join(directory_name, f"query_{i}.sql")

        # Виконуємо запит за сформованим шляхом
        execute_query_from_file(filepath)
