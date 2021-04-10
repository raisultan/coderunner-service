FROM python:3.9.0-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /loadlimiter && apt-get update
WORKDIR /loadlimiter

COPY ./pyproject.toml /loadlimiter/
COPY ./poetry.lock /loadlimiter/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY ./ /loadlimiter
