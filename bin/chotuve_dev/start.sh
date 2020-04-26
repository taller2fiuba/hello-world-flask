#!/bin/bash

pip install -r requirements.txt
cd src
flask run --host=0.0.0.0
