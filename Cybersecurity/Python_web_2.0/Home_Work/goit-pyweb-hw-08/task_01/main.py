from dotenv import load_dotenv
from config.db import init_mongodb
from controllers.terminal_controller import TerminalController
from services.data_loader import DataLoaderService

# Завантажуємо змінні середовища одразу після імпортів
load_dotenv()

def main():
    # 1. Ініціалізація БД
    init_mongodb()

    # 2. Завантаження даних
    DataLoaderService.load_authors("authors.json")
    DataLoaderService.load_quotes("quotes.json")

    # 3. Запуск інтерфейсу
    TerminalController.run()

if __name__ == "__main__":
    main()
