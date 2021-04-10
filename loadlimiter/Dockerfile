FROM python:3.9.0-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /loadbalancer && apt-get update
WORKDIR /loadbalancer

COPY ./pyproject.toml /loadbalancer/
COPY ./poetry.lock /loadbalancer/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY ./ /loadbalancer
