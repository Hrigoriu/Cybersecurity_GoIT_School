import re
from functools import wraps

# Банер привітання
WELCOME_BANNER = """
 _____                _                 _    ______         _   
/  __ \              | |               | |   | ___ \       | |  
| /  \/  ___   _ __  | |_   __ _   ___ | |_  | |_/ /  ___  | |_ 
| |     / _ \ | '_ \ | __| / _` | / __|| __| | ___ \ / _ \ | __|
| \__/\| (_) || | | || |_ | (_| || (__ | |_  | |_/ /| (_) || |_ 
 \____/ \___/ |_| |_| \__| \__,_| \___| \__| \____/  \___/  \__|
"""

def input_error(func):
    """
    Декоратор для обробки помилок введення.
    """
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return inner

def parse_input(user_input):
    """Розбирає введений рядок на команду та аргументи."""
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args
    except ValueError:
        return "", []

def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує телефонні номери до стандартного формату +380XXXXXXXXX.
    """
    sanitized_number = re.sub(r'\D', '', phone_number)
    
    if sanitized_number.startswith("380"):
        return f"+{sanitized_number}"
    else:
        return f"+38{sanitized_number}"