FROM python:3.9-alpine
WORKDIR .
ENV DJANGO_SETTINGS_MODULE=hw2_4sem2.settings
ENV PYTHONUNBUFFERED=1

RUN apk update\
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY . .


