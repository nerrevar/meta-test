#!/usr/bin/sh
export FLASK_APP=$(dirname $(realpath $0))/api/flaskr/index.py
export FLASK_ENV=development
cd $(dirname $(realpath $0))/api
python -m flask run
