# для билда докер контейнера перейти в директорию homework_03: cd homework_03
# выполнить команду: docker build -t web .
# затем выполнить команду docker run -it -p 8000:8000 web
FROM python:3.10-bookworm
WORKDIR /app
RUN pip install "poetry==1.8.2"
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root
COPY app.py ./
CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]