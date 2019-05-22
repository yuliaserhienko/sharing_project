FROM python:3.7

RUN mkdir /src
WORKDIR /src
COPY ./sharing /src
COPY requirements.txt /src/requirements.txt

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

