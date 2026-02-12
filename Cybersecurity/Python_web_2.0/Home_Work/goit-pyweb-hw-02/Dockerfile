# Використаємо офіційний легкий образ Python 3.10
FROM python:3.12

# Встановимо змінні оточення
# PYTHONDONTWRITEBYTECODE - не створювати .pyc файли
# PYTHONUNBUFFERED - виводити логи одразу в консоль (важливо для Docker)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Встановимо робочу директорію всередині контейнера
WORKDIR /app

# Встановимо Poetry
RUN pip install poetry

# Копіюємо тільки файли конфігурації Poetry (щоб закешувати цей шар)
COPY pyproject.toml poetry.lock* ./

# Налаштуємо Poetry:
# virtualenvs.create false - не створювати віртуальне середовище всередині Docker, 
# бо сам контейнер - це вже ізоляція. Ставимо пакети глобально в контейнері.
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

# Копіюємо весь інший код проекту в контейнер
COPY . .

# Команда, яка виконається при запуску контейнера
CMD ["python", "main.py"]