#!/bin/sh

echo "Waiting for PostgreSQL..."
until nc -z "$POSTGRES_HOST" "$POSTGRES_DB_PORT"; do
    echo "PostgreSQL is unavailable - sleeping"
    sleep 2
done
echo "PostgreSQL is up - running migrations..."

alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

echo "Migrations applied. Starting server..."

# Run web server
uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload --reload-dir /usr/fastapi/
