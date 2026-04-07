from services.search_service import SearchService
from utils.logger import RetroTerminal


class TerminalController:
    @staticmethod
    def run():
        RetroTerminal.print_sys("Ініціалізація Retro-Tech Терміналу...")
        RetroTerminal.print_sys(
            "Доступні команди: name:<ім'я>, tag:<тег>, tags:<тег1,тег2>, exit"
        )

        while True:
            try:
                user_input = input("\nuser@retro-os:~$ ").strip()
                if not user_input:
                    continue

                if user_input.lower() == "exit":
                    RetroTerminal.print_sys("Завершення роботи. До побачення.")
                    break

                if ":" not in user_input:
                    RetroTerminal.print_error(
                        "Невідомий формат. Використовуйте команду у форматі name:value"
                    )
                    continue

                command, value = user_input.split(":", 1)
                command = command.strip().lower()
                value = value.strip()

                results = []
                if command == "name":
                    results = SearchService.search_by_name(value)
                elif command == "tag":
                    results = SearchService.search_by_tag(value)
                elif command == "tags":
                    results = SearchService.search_by_tags(value)
                else:
                    RetroTerminal.print_error(f"Невідома команда: {command}")
                    continue

                # 🛑 БРОНЕЖИЛЕТ ВІД ДУБЛІКАТІВ НА ЕКРАНІ
                if results:
                    # Цей рядок примусово видаляє будь-які дублікати перед друком, зберігаючи порядок
                    unique_results = list(dict.fromkeys(results))

                    for quote in unique_results:
                        print(f'> "{quote}"')
                else:
                    print("Нічого не знайдено.")

            except KeyboardInterrupt:
                RetroTerminal.print_sys("\nЗавершення роботи. До побачення.")
                break
            except Exception as e:
                RetroTerminal.print_error(f"Помилка: {e}")
                RetroTerminal.print_error(f"Помилка: {e}")
