FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV STATIC_URL /static
ENV STATIC_PATH /app/static

COPY . /app
COPY ./preentry.sh /preentry.sh

ENTRYPOINT /preentry.sh /entrypoint.sh /start.sh
