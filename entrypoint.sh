#!/bin/sh

while ! nc -z db 5432; do
  echo "Waiting for database...."
  sleep 0.1
done

echo "Database started"

python manage.py migrate --no-input
# python manage.py seed_db --no-input

exec "$@"
