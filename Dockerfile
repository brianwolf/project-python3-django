FROM python:3.10-slim

WORKDIR /home/src

ARG ARG_VERSION=local

ENV VERSION=${ARG_VERSION}
ENV TZ=America/Argentina/Buenos_Aires
ENV DEBUG=True
ENV ALLOWED_HOSTS=0.0.0.0
ENV SQLITE_PATH=db.sqlite3

CMD python manage.py migrate && gunicorn \
    -b 0.0.0.0:8000 \
    --workers=1 \
    --threads=5 \
    core.wsgi

COPY requirements.txt ./
RUN pip install -r requirements.txt --upgrade pip
RUN rm -fr requirements.txt

COPY . .
