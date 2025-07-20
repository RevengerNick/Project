FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем наш файл Excel в рабочую директорию контейнера
COPY financial_data.xlsx .

# Копируем остальной код приложения (main.py)
COPY main.py .

# Указываем команду для запуска приложения через Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]