# 1. Використовуємо сумісну версію Python
FROM python:3.12-slim

WORKDIR /app

# Встановлюємо Poetry
RUN pip install poetry

# Копіюємо конфіги
COPY pyproject.toml poetry.lock* ./

# Налаштування Poetry (не створювати virtualenv)
RUN poetry config virtualenvs.create false

# 2. Встановлюємо залежності БЕЗ самого проекту (--no-root)
RUN poetry install --no-ansi --no-interaction --no-root

# Копіюємо код
COPY . .

# Запуск
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]