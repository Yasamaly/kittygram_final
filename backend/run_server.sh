#!/bin/sh

python3 manage.py migrate

python manage.py collectstatic

cp -r static_backend /static
rm -rf static_backend


# При старте контейнера запустить сервер разработки.
python3 manage.py runserver "0:8000"
