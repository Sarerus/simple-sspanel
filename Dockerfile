FROM python:3.10-buster

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt

WORKDIR /code

EXPOSE 8000