# pull official base image
FROM python:3.7-alpine

# set work directory
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2
RUN apk update
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache postgresql-dev


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apk del .build-deps

# copy project
COPY . /usr/src/app/

