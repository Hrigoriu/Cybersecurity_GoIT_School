#app/core/logger.py
import logging
import sys

class RetroTerminalFormatter(logging.Formatter):
    """
    Спеціальний форматер логів у стилі Retro-Tech Terminal.
    Використовує ANSI escape codes для зеленого тексту на чорному фоні
    та додає ASCII-рамки.
    """
    GREEN = "\033[32m"
    RESET = "\033[0m"
    BG_BLACK = "\033[40m"

    def format(self, record: logging.LogRecord) -> str:
        # Формування базового повідомлення
        log_msg = super().format(record)

        # Створення ASCII інтерфейсу
        border = f"{self.GREEN}{self.BG_BLACK}+=============================================================================+{self.RESET}"
        content = f"{self.GREEN}{self.BG_BLACK}| [SYS_LOG] {record.levelname:<8} | {log_msg}{self.RESET}"

        return f"\n{border}\n{content}\n{border}"

def setup_retro_logger() -> logging.Logger:
    """Ініціалізація та налаштування логера."""
    logger = logging.getLogger("retro_logger")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        console_handler = logging.StreamHandler(sys.stdout)
        formatter = RetroTerminalFormatter(
            fmt="%(asctime)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

log = setup_retro_logger()
