FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

COPY . .

# Відкриваємо порт 5000 для доступу ззовні
EXPOSE 5000

# Запускаємо app.py замість main.py
CMD ["python", "app.py"]