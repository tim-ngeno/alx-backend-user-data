#!/usr/bin/env python3
""" A basic Flask App """
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ A simple flask method """
    return jsonify({'message': 'Bienvenue'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
