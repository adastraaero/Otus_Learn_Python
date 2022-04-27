FROM python:3.9-buster

#вывод из консоли не буфферизируется в Docker
ENV PYTHONBUFFERED=1

RUN pip install poetry

#указываем рабочую директорию по умолчанию
WORKDIR /app/

COPY poetry.lock pyproject.toml /app/

#отключаем VirtualEnv т.к. не нужно в Docker
RUN poetry config virtualenvs.create false

RUN poetry install

COPY main.py /app/

EXPOSE 8000

#Автоматический маппинг 8000 порта контейнера на рандомный порт хоста
CMD ["uvicorn", "--host=0.0.0.0", "main:app", "--port=8000"]






