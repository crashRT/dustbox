FROM python:3.10.8-alpine

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
RUN mkdir -p /var/run/gunicorn
VOLUME db.sqlite3

CMD ["gunicorn", "dustbox.wsgi", "--bind=unix:/var/run/gunicorn/gunicorn.sock"]