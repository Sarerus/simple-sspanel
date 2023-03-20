FROM python:3.10-buster

COPY ./requirements.txt /requirements.txt

COPY /entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt

WORKDIR /code

EXPOSE 8000

ENTRYPOINT [ "/entrypoint.sh" ]