import os
import json
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException


from db import db

app = Flask(__name__, static_folder='../../dist', static_url_path='/')

@app.before_request
def _db_connect():
    db.db.connect()

@app.teardown_request
def _db_close(exc):
    if not db.db.is_closed():
        db.db.close()

@app.route('/read', methods=['POST'])
def read():
    return jsonify(db.get_psychotherapists())

@app.route('/read_single', methods=['POST'])
def read_single():
    return jsonify(
        db.get_psychotherapist(
            json.loads(request.data).get('id')
        )
    )

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.errorhandler(HTTPException)
def fallback(e):
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()
