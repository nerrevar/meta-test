#!/usr/bin/sh
cd $(dirname $(realpath $0))/api
python update_data.py
