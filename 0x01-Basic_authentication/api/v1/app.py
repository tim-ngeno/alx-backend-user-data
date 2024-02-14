#!/usr/bin/env python3
"""
Route module for the API
"""

from api.v1.views import app_views
from flask import Flask, jsonify, abort, request, Response
from flask_cors import (CORS, cross_origin)
from typing import Union
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = os.getenv('AUTH_TYPE')
if auth_type:
    if auth_type == 'Auth':
        from api.v1.auth.auth import Auth
        auth = Auth()
    else:
        from api.v1.auth.basic_auth import BasicAuth
        auth = BasicAuth()


@app.before_request
def before_request() -> Union[str, None]:
    """
    Handler for before each request
    """
    if auth is None:
        return None

    excluded_paths = [
        '/api/v1/status/', '/api/v1/unauthorized/',
        '/api/v1/forbidden/',
    ]
    if request.path not in excluded_paths:
        return None
    if not auth.require_auth(request.path, excluded_paths):
        return None
    if auth.authorization_header(request) is None:
        return abort(401)
    if auth.current_user(request) is None:
        return abort(403)


@app.errorhandler(401)
def unauthorized_error_handler(error: Exception) -> tuple[Response, int]:
    """
    Unauthorized error handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error_handler(error: Exception) -> tuple[Response, int]:
    """
    Forbidden error handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error: Exception) -> tuple[Response, int]:
    """
    Not found handler
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = os.getenv("API_PORT", 5000)
    app.run(host=host, port=port)
