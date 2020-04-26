FROM python:3.8

ADD ./requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -q -r /tmp/requirements.txt

# Add our code
ADD ./src /var/www/app
WORKDIR /var/www/app

# Expose is NOT supported by Heroku

# Run the image as a non-root user
RUN useradd -ms /bin/bash chotuve
USER chotuve

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
CMD gunicorn --bind 0.0.0.0:$PORT wsgi
