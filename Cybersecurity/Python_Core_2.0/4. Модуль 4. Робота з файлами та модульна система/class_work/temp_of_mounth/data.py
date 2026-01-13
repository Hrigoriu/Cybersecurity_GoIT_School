from pathlib import Path


def load_data(filename):
    """
    Завантажує сирі дані з файлу.
    Використовує Path для уникнення помилок FileNotFoundError.
    """
    # Визначаємо шлях до папки, де лежить цей скрипт data.py
    folder_path = Path(__file__).parent
    file_path = folder_path / filename

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено за адресою {file_path}")
        return []


def clean_data(raw_data):
    """
    Очищує дані: видаляє переноси рядків та порожні елементи.
    Повертає список чисел (або очищених рядків).
    """
    cleaned_list = []
    
    for line in raw_data:
        # Видаляємо пробіли та переноси рядків (\n)
        stripped_line = line.strip()
        
        # Якщо рядок не порожній - додаємо в список
        if stripped_line:
            # Спробуємо перетворити на число (якщо це температури)
            # Якщо у вас там просто текст, приберіть try/except
            try:
                # Якщо дані це числа (наприклад: "23.5"), перетворюємо на float
                cleaned_list.append(float(stripped_line))
            except ValueError:
                # Якщо це не число, просто додаємо як текст
                cleaned_list.append(stripped_line)
                
    return cleaned_list
