FROM --platform=$BUILDPLATFORM python:3.12-bullseye

WORKDIR .

COPY . .

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]