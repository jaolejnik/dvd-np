#!/bin/sh

# We make the script wait until the db container is up 
# to be sure that Django container will start properly
echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
    sleep 0.1
done
echo "PostgeSQL started!"

pipenv run python manage.py migrate
pipenv run gunicorn backend.wsgi --bind 0.0.0.0:8000
