#!/usr/bin/env python3
""" A basic Flask App """

from auth import Auth
from flask import Flask, jsonify, request, Response

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> Response:
    """ A simple flask method """
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> Response:
    """ End point to register a user """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email=email, password=password)
        if user is not None:
            return jsonify({'email': email, 'message': 'user created'}), 200
    except ValueError:
        return jsonify({'message': 'email already registered'}), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
