#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', strict_slashes=False)
def unauthorized_handler() -> str:
    """ Raises a 401 error using abort
    """
    return abort(401)


@app_views.route('/forbidden', strict_slashes=False)
def forbidden_handler() -> str:
    """ Raises a 403 error using abort
    """
    return abort(403)


class Response:
    """ Class Response module """

    def __init__(self, status_code, data):
        """ Initializes the class Response """
        self.status_code = status_code
        self.data = data

    def _get_data_for_json(self):
        """ Get suitable data for JSON serialization """
        return {
            "status_code": self.status_code,
            "data": self.data
        }
