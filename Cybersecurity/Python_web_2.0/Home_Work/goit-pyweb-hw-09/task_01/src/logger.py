from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

class RetroLogger:
    """Логер у стилі Retro-Tech Terminal для консольного виводу."""

    @staticmethod
    def _print(level: str, color: str, message: str):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"{color}[{timestamp}] [SYS.{level}] > {message}{Style.RESET_ALL}")

    @classmethod
    def info(cls, message: str):
        cls._print("INFO", Fore.GREEN, message)

    @classmethod
    def process(cls, message: str):
        cls._print("EXEC", Fore.CYAN, message)

    @classmethod
    def warning(cls, message: str):
        cls._print("WARN", Fore.YELLOW, message)

    @classmethod
    def error(cls, message: str):
        cls._print("FAIL", Fore.RED, message)

    @classmethod
    def success(cls, message: str):
        cls._print("DONE", Fore.LIGHTGREEN_EX + Style.BRIGHT, message)
