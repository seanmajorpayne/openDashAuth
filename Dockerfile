# syntax=docker/dockerfile:1
FROM python:3.8.5-slim

RUN apt-get update

WORKDIR /app

ENV FLASK_APP=digitalDash.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .

CMD ["flask", "run"]
