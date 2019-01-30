FROM python:3.6

COPY ./requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -U pip && \
    pip install -r requirements.txt
RUN apt-get update && \
    apt-get install netcat-openbsd -y