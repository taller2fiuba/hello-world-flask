#!/bin/bash

pip install -r app/requirements.txt
flask run --host=0.0.0.0
# Cleanup __pycache__ directories
#find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
