FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN adduser \
        --no-create-home \
        --disabled-password \
        django-user

RUN chmod 777 app
RUN chown django-user:django-user -R app

USER django-user