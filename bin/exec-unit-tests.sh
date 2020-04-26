#!/bin/bash

find . -type f -name "*.py" | xargs pylint --load-plugins pylint_flask --ignore wsgi.py && coverage run -m nose2 -v && coverage report -m
