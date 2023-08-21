FROM python:3.8-alpine

ENV PYTHONBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

RUN mkdir /django-blog
WORKDIR /django-blog/
COPY ./requirements.txt .
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps
COPY . .

#db username
RUN adduser -D aliona
USER aliona

RUN python manage.py collectstatic