#!/usr/bin/env python3
""" A basic Flask App """

from auth import Auth
from flask import abort, Flask, jsonify, make_response, request, Response

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> Response:
    """ A simple flask method """
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> tuple[Response, int]:
    """ End point to register a user """
    email = str(request.form.get('email'))
    password = str(request.form.get('password'))

    try:
        user = AUTH.register_user(email=email, password=password)
        if user is not None:
            return jsonify({'email': email, 'message': 'user created'}), 200
    except ValueError:
        return jsonify({'message': 'email already registered'}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> Response:
    """ Creates a new session for the user and stores it in a session ID
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        abort(401)
    if not AUTH.valid_login(email, password):
        abort(401)

    # Create a new session
    session_id = AUTH.create_session(email)
    response = make_response(
        jsonify({'email': email, 'message': 'logged in'}))
    response.set_cookie('session_id', session_id)

    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
