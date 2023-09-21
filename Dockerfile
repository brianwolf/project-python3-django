FROM python:3.10-slim

USER root

ARG ARG_VERSION=local

ENV VERSION=${ARG_VERSION}
ENV TZ=America/Argentina/Buenos_Aires
ENV GUNICORN_HOST=0.0.0.0
ENV GUNICORN_PORT=8000
ENV GUNICORN_THREADS=20
ENV DEBUG=False
ENV ALLOWED_HOSTS=127.0.0.1,localhost,0.0.0.0
ENV SQLITE_PATH=db.sqlite3
ENV LOG_LEVEL=INFO
ENV LOG_PATH=django.log
ENV LOG_BACKUP_COUNT=3

CMD python manage.py migrate && gunicorn \
    -b ${GUNICORN_HOST}:${GUNICORN_PORT} \
    --workers=1 \
    --threads=${GUNICORN_THREADS} \
    core.wsgi

COPY requirements.txt ./
RUN pip install -r requirements.txt --upgrade pip
RUN rm -fr requirements.txt

COPY manage.py .
COPY core/ core/
COPY apps/ apps/
COPY .env ./
