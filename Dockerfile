FROM python:3.8-alpine

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /django-blog
WORKDIR /django-blog
COPY . /django-blog

#db username
RUN adduser -D aliona
USER aliona

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
