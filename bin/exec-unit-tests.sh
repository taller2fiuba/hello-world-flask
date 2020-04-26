#!/bin/bash

find . -type f -name "*.py" | xargs pylint --load-plugins pylint_flask --ignore wsgi.py && nose2 -v
