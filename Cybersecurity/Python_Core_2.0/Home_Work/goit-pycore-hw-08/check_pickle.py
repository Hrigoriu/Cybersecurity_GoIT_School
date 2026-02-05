import pickle
from pathlib import Path
import sys

# Нам потрібно імпортувати класи, щоб pickle знав структуру об'єктів
# Ми імпортуємо їх з основного файлу task_01
try:
    from task_01 import AddressBook, Record, Name, Phone, Birthday
except ImportError:
    print("Помилка: Не знайдено файл task_01.py")
    sys.exit()

def inspect_file():
    file_path = Path("data") / "addressbook.pkl"

    if not file_path.exists():
        print(f"❌ Файл {file_path} не знайдено. Спочатку запустіть бота і додайте контакти.")
        return

    print(f"✅ Файл знайдено: {file_path}")
    print("Спроба прочитати 'сирі' дані...")

    try:
        with open(file_path, "rb") as f:
            book = pickle.load(f)
        
        print("\n--- ВМІСТ ФАЙЛУ (Відновлений об'єкт) ---")
        if not book.data:
            print("Адресна книга порожня.")
        else:
            for name, record in book.data.items():
                print(f"👤 {name}")
                print(f"   📞 Телефони: {'; '.join(p.value for p in record.phones)}")
                if record.birthday:
                    print(f"   🎂 Дн: {record.birthday}")
                print("-" * 20)
                
    except Exception as e:
        print(f"❌ Помилка читання файлу: {e}")

if __name__ == "__main__":
    inspect_file()