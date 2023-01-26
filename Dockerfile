FROM python:3.9.4-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000
ENV SECRET_KEY=${SECRET_KEY}
ENV SENTRY_DSN=${SENTRY_DSN}

WORKDIR /app

COPY requirements.txt /app/

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

EXPOSE $PORT

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD python manage.py runserver 0.0.0.0:$PORT