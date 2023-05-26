FROM python:3.11.3-slim-bullseye

ENV PYTHONUNBUFFERED 1

WORKDIR /drf_src

COPY . .

RUN pip install -r requirements.txt

VOLUME /drf_src

CMD python manage.py makemigrations && python manage.py migrate && python manage.py load_csv  && python manage.py load_trucks && python manage.py runserver 0.0.0.0:8000
