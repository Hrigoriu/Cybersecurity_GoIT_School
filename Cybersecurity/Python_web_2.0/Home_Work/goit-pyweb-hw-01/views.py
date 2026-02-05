from abc import ABC, abstractmethod

class UserView(ABC):
    """
    Абстрактний базовий клас для відображення інформації користувачеві.
    Визначає методи, які повинні бути реалізовані у будь-якому інтерфейсі (консоль, веб, GUI).
    """

    @abstractmethod
    def display_message(self, message: str):
        """Відображення простого повідомлення."""
        pass

    @abstractmethod
    def display_contacts(self, contacts: list):
        """Відображення списку контактів."""
        pass

    @abstractmethod
    def display_birthdays(self, birthdays: list):
        """Відображення списку днів народжень."""
        pass

    @abstractmethod
    def display_help(self, commands: dict):
        """Відображення доступних команд."""
        pass


class ConsoleView(UserView):
    """
    Реалізація інтерфейсу користувача для командного рядка.
    """

    def display_message(self, message: str):
        print(f"\n>>> {message}")

    def display_contacts(self, contacts: list):
        if not contacts:
            print("\n>>> Книга контактів порожня.")
            return

        print("\n" + "=" * 40)
        print(f"{'ІМ\'Я':<20} | {'ТЕЛЕФОН':<20}")
        print("-" * 40)
        for contact in contacts:
            phones = "; ".join(p.value for p in contact.phones)
            print(f"{contact.name.value:<20} | {phones:<20}")
        print("=" * 40 + "\n")

    def display_birthdays(self, birthdays: list):
        if not birthdays:
            print("\n>>> Немає найближчих днів народжень.")
            return

        print("\n" + "*" * 40)
        print("🎉 Найближчі іменинники:")
        for item in birthdays:
            print(f"🎂 {item['name']:<15} - {item['congratulation_date']}")
        print("*" * 40 + "\n")

    def display_help(self, commands: dict):
        print("\n" + "#" * 40)
        print("📘 ДОСТУПНІ КОМАНДИ:")
        print("-" * 40)
        for cmd, desc in commands.items():
            print(f"{cmd:<15} : {desc}")
        print("#" * 40 + "\n")