#!/bin/sh
set -e

# sync database migrations
python manage.py migrate

# sync static files to reverse proxy
python manage.py collectstatic --noinput

# sync accounts to celery and it will be send to v2ray via grpc
python manage.py syncv2ray

# run django server
cd /code

python -m gunicorn -b 0.0.0.0:8000 simple_sspanel.asgi:application -k uvicorn.workers.UvicornWorker
