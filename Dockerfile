FROM python:3.6

COPY ./requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -U pip && \
    pip install -r requirements.txt
RUN apt-get update && \
    apt-get install git netcat-openbsd -y && \
    git clone https://github.com/vishnubob/wait-for-it.git /wait-for-it