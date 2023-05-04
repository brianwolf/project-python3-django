FROM python:3.10-slim

RUN useradd -ms /bin/bash nonroot
USER nonroot
WORKDIR /home/nonroot/src

ARG ARG_VERSION=local

ENV VERSION=${ARG_VERSION}
ENV TZ=America/Argentina/Buenos_Aires
ENV GUNICORN_HOST=0.0.0.0
ENV GUNICORN_PORT=8000
ENV GUNICORN_THREADS=5

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
COPY .env .
