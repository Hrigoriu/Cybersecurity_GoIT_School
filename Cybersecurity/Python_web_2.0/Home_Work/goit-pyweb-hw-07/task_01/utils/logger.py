import datetime


class RetroLogger:
    """
    Утиліта для стилізованого консольного виводу (Retro-Tech Terminal Aesthetic).
    Використовує ANSI-коди для створення ефекту старих терміналів.
    """

    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

    @staticmethod
    def _get_timestamp() -> str:
        """Повертає поточний час у форматі системного логу."""
        return datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]

    @classmethod
    def info(cls, msg: str):
        """Вивід стандартної системної інформації (Зелений)."""
        print(f"{cls.GREEN}[SYS_INFO] {cls._get_timestamp()} >> {msg}{cls.RESET}")

    @classmethod
    def warn(cls, msg: str):
        """Вивід попереджень (Жовтий)."""
        print(f"{cls.YELLOW}[SYS_WARN] {cls._get_timestamp()} >> {msg}{cls.RESET}")

    @classmethod
    def error(cls, msg: str):
        """Вивід критичних помилок (Червоний)."""
        print(f"{cls.RED}[SYS_ERR ] {cls._get_timestamp()} >> {msg}{cls.RESET}")

    @classmethod
    def data(cls, msg: str):
        """Вивід даних або результатів запитів (Блакитний)."""
        print(f"{cls.CYAN}[SYS_DATA] {cls._get_timestamp()} >> {msg}{cls.RESET}")
