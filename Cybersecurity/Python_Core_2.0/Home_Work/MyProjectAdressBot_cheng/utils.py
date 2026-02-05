import re
from functools import wraps


WELCOME_BANNER = """
===== ADDRESS BOOK BOT =====
"""


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command format."
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
