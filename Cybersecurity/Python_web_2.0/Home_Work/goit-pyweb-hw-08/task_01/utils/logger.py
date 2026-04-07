import sys


class RetroTerminal:
    """
    Створимо клас для забезпечення естетики Retro-Tech Terminal (зелений текст на чорному фоні).
    Реалізує базові принципи DRY для форматування виводу консолі.
    """

    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

    @staticmethod
    def print_sys(message: str) -> None:
        """Вивід системних повідомлень."""
        print(f"{RetroTerminal.GREEN}[SYS] {message}{RetroTerminal.RESET}")

    @staticmethod
    def print_db(message: str) -> None:
        """Вивід повідомлень бази даних."""
        print(f"{RetroTerminal.CYAN}[DB] {message}{RetroTerminal.RESET}")

    @staticmethod
    def print_error(message: str) -> None:
        """Вивід помилок."""
        print(f"{RetroTerminal.RED}[ERROR] {message}{RetroTerminal.RESET}")

    @staticmethod
    def print_data(message: str) -> None:
        """Вивід знайдених даних (гарантує utf-8)."""
        sys.stdout.buffer.write(
            f"{RetroTerminal.YELLOW}{message}{RetroTerminal.RESET}\n".encode("utf-8")
        )
        sys.stdout.buffer.write(
            f"{RetroTerminal.YELLOW}{message}{RetroTerminal.RESET}\n".encode("utf-8")
        )
