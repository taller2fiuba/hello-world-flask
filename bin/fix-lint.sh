#!/bin/bash

find . -type f -name "*.py" | xargs autopep8 --in-place --aggressive --aggressive
