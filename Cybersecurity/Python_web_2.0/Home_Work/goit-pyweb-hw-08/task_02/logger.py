from datetime import datetime
from colorama import init, Fore, Style

# Ініціалізація colorama для кросплатформної підтримки кольорів
init(autoreset=True)

class RetroLogger:
    """
    Кастомний логер, що імітує естетику Retro-Tech Terminal (зелений/блакитний текст на чорному).
    """
    @staticmethod
    def _print(level: str, color: str, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"{color}[{timestamp}] [{level}] > {message}{Style.RESET_ALL}"
        print(formatted_message)

    @classmethod
    def info(cls, message: str):
        """Інформаційне повідомлення (зелений термінал)."""
        cls._print("INFO", Fore.GREEN, message)

    @classmethod
    def warning(cls, message: str):
        """Попередження (жовтий)."""
        cls._print("WARN", Fore.YELLOW, message)

    @classmethod
    def error(cls, message: str):
        """Помилка (червоний)."""
        cls._print("ERROR", Fore.RED, message)

    @classmethod
    def success(cls, message: str):
        """Успішне виконання (яскраво-зелений)."""
        cls._print("SUCCESS", Fore.LIGHTGREEN_EX + Style.BRIGHT, message)
