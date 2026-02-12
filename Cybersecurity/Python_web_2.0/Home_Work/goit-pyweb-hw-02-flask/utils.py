import re
from functools import wraps


welcom_big_baner = r"""
 
 _____                _                 _    ______         _   
/  __ \              | |               | |   | ___ \       | |  
| /  \/  ___   _ __  | |_   __ _   ___ | |_  | |_/ /  ___  | |_ 
| |     / _ \ | '_ \ | __| / _` | / __|| __| | ___ \ / _ \ | __|
| \__/\| (_) || | | || |_ | (_| || (__ | |_  | |_/ /| (_) || |_ 
 \____/ \___/ |_| |_| \__| \__,_| \___| \__| \____/  \___/  \__|
                                                                
                                                                
"""

WELCOME_BANNER = """
========================================
    🤖 ADDRESS BOOK ASSISTANT 🤖
========================================
"""


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError:
            return "Контакт не знайдено."
        except IndexError:
            return "Невірний формат команди."
    return inner


def parse_input(user_input: str):
    parts = user_input.split()
    if not parts:
        return "", []
    return parts[0].lower(), parts[1:]


def normalize_phone(phone: str) -> str:
    digits = re.sub(r"\D", "", phone)
    if digits.startswith("380"):
        return f"+{digits}"
    return f"+38{digits}"