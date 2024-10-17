# Базовый образ с Python
FROM python:3.11-slim

# Установка необходимых системных зависимостей
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && apt-get clean

# Установка Poetry
ENV POETRY_VERSION=1.7.0
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Установка рабочего каталога
WORKDIR /app

# Копирование файлов Poetry
COPY pyproject.toml poetry.lock /app/

# Установка зависимостей через Poetry
RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi

# Копирование проекта
COPY ./src /app/src

# Установка Alembic и копирование alembic.ini
COPY ./src/alembic.ini /app/

# Открытие порта для сервера
EXPOSE 8000

# Команда по умолчанию, если не указана в docker-compose
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
