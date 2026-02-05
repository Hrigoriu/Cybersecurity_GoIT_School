import pickle
from pathlib import Path
from collections import UserDict
from datetime import datetime, timedelta


class AddressBook(UserDict):
    """
    Адресна книга.
    Відповідає за:
    - зберігання контактів
    - бізнес-логіку
    - збереження / завантаження
    - логування
    """

    # ---------- CRUD ----------

    def add_record(self, record):
        self.data[record.name.value] = record
        self.log(f"Contact '{record.name.value}' saved")

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            self.log(f"Contact '{name}' deleted")

    def clear(self):
        self.data.clear()
        self.log("AddressBook cleared")

    # ---------- Business logic ----------

    def get_upcoming_birthdays(self, days: int = 7):
        today = datetime.today().date()
        result = []

        for record in self.data.values():
            if not record.birthday:
                continue

            birthday = record.birthday.date.replace(year=today.year)
            if birthday < today:
                birthday = birthday.replace(year=today.year + 1)

            delta = (birthday - today).days
            if 0 <= delta <= days:
                if birthday.weekday() == 5:
                    birthday += timedelta(days=2)
                elif birthday.weekday() == 6:
                    birthday += timedelta(days=1)

                result.append({
                    "name": record.name.value,
                    "congratulation_date": birthday.strftime("%d.%m.%Y")
                })

        return result

    # ---------- Persistence ----------

    @staticmethod
    def _storage_path(filename: str) -> Path:
        base = Path(__file__).resolve().parent
        data = base / "data"
        data.mkdir(exist_ok=True)
        return data / filename

    def save(self, filename="addressbook.pkl"):
        with open(self._storage_path(filename), "wb") as f:
            pickle.dump(self, f)
        self.log("AddressBook saved")

    @classmethod
    def load(cls, filename="addressbook.pkl"):
        path = cls._storage_path(filename)
        if not path.exists():
            return cls()

        try:
            with open(path, "rb") as f:
                return pickle.load(f)
        except Exception:
            return cls()

    # ---------- Utils ----------

    def log(self, message: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_file = self._storage_path("logs.txt")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
