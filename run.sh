#!/bin/bash

python3 -m venv todo-venv
source todo-venv/bin/activate
pip3 install -r requirements.txt
python3 main.py