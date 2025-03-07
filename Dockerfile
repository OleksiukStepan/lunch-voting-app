FROM python:3.10

WORKDIR /usr/fastapi

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR off

RUN apt-get update && apt-get install -y gcc libpq-dev netcat-openbsd

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

COPY backend/app/scripts/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
