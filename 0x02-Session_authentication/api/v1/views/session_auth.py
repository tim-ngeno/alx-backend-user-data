#!/usr/bin/env python3
""" Session authentication views """
from flask import Blueprint, jsonify, request, make_response
from models.user import User
from api.v1.app import auth

session_auth_bp = Blueprint(
    'session_auth', __name__, url_prefix='/auth_session')


@session_auth_bp.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """
    Handle user login using Session authentication
    """
    # Retrieve email and password parameters from request form
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if email is missing or empty
    if not email:
        return jsonify({"error": "email missing"}), 400

    # Check if password is missing or empty
    if not password:
        return jsonify({"error": "password missing"}), 400

    # Retrieve User instance based on email
    user = User.search({"email": email})

    # If no User found, return 404 error
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    # Check if password matches the User's password
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create a session ID for the User
    session_id = auth.create_session(user.id)

    # Return User dictionary representation and set cookie to the response
    response_data = user.to_json()
    response = make_response(jsonify(response_data))
    session_cookie_name = os.getenv('SESSION_NAME', '_my_session_id')
    response.set_cookie(session_cookie_name, session_id)

    return response
