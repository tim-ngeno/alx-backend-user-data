#!/usr/bin/env python3
"""
API authentication module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Manages the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns a boolean
        """
        if path is None or not excluded_paths:
            return True

        path = path.rstrip('/') + '/'

        # Check if path is in excluded_paths
        for excluded_path in excluded_paths:
            if path.startswith(excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Takes a Flask request object and returns the Authorization
        header value. Returns None if request is None or if
        Authorization header is not present.
        """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        return header if header else None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None, with the request arg as a flask request object
        """
        return None
