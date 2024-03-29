#!/usr/bin/env python3
""" A basic Flask App """

from flask import (
    abort, Flask, jsonify, make_response, request, Response, redirect)
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> tuple[Response, int]:
    """ A simple flask method """
    return jsonify({'message': 'Bienvenue'}), 200


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
def login() -> str:
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
        jsonify({'email': email, 'message': 'logged in'}), 200)
    response.set_cookie('session_id', session_id)

    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> Response:
    """Log out a user from a session"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        return jsonify({'error': 'Forbidden'}), 403


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> Response:
    """ Returns the user profile if the user exists
    """
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            return jsonify({'email': user.email}), 200
    return abort(403)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
