import pickle
from pathlib import Path
from collections import UserDict
from datetime import datetime, timedelta

class AddressBook(UserDict):
    """
    Клас для зберігання та управління записами.
    """
    
    def add_record(self, record):
        """Додає запис до книги."""
        self.data[record.name.value] = record
        self.log(f"Contact {record.name.value} has been added.")

    def find(self, name):
        """Знаходить запис за ім'ям."""
        return self.data.get(name)

    def delete(self, name):
        """Видаляє запис за ім'ям."""
        if name in self.data:
            del self.data[name]
            self.log(f"Contact {name} has been removed!")

    def log(self, action):
        """
        Записує повідомлення про дії у файл logs.txt.
        Файл зберігається у папці 'data' поруч зі скриптом.
        """
        current_time = datetime.now().strftime('%H:%M:%S')
        message = f'[{current_time}] {action}'
        
        # Використовуємо _get_storage_path для правильного шляху
        log_path = self._get_storage_path("logs.txt")
        
        with open(log_path, 'a', encoding='utf-8') as file:
            file.write(f'{message}\n')

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = datetime.today().date()

        for record in self.data.values():
            if record.birthday is None:
                continue
            
            birthday_date = record.birthday.date
            birthday_this_year = birthday_date.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days

            if 0 <= delta_days <= days:
                congratulation_date = birthday_this_year
                if congratulation_date.weekday() == 5: 
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6: 
                    congratulation_date += timedelta(days=1)

                upcoming_birthdays.append({
                    "name": record.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                })

        return upcoming_birthdays

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

    # --- Persistence Logic ---

    @staticmethod
    def _get_storage_path(filename):
        """Отримує абсолютний шлях до файлу в папці data."""
        base_dir = Path(__file__).resolve().parent
        data_dir = base_dir / "data"
        data_dir.mkdir(exist_ok=True)
        return data_dir / filename

    def save_data(self, filename="addressbook.pkl"):
        """Зберігає книгу у файл."""
        file_path = self._get_storage_path(filename)
        with open(file_path, "wb") as f:
            pickle.dump(self, f)
        self.log("Addressbook has been saved!")

    @classmethod
    def load_data(cls, filename="addressbook.pkl"):
        """Завантажує книгу з файлу."""
        file_path = cls._get_storage_path(filename)
        
        # Створюємо порожню книгу, якщо файлу немає
        if not file_path.exists():
            book = cls()
            book.log("Addressbook has been created!")
            return book
            
        try:
            with open(file_path, "rb") as f:
                book = pickle.load(f)
                book.log("Addressbook has been loaded!")
                return book
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            book = cls()
            book.log("Addressbook has been created (error loading)!")
            return book