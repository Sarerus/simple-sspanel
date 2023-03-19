FROM python:buster

COPY ./requirements.txt /requirements.txt

RUN pip install -U pip \
    && pip install -r requirements.txt \
    && rm requirements.txt

WORKDIR /code

EXPOSE 8000