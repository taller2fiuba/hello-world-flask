FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV STATIC_URL /static
ENV STATIC_PATH /app/static

COPY . /app

