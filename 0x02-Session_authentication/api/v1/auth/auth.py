#!/usr/bin/env python3
"""
API authentication module
"""
import os
from typing import List, TypeVar, Union


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
            if excluded_path.endswith('*'):
                prefix = excluded_path[:-1]
                if path.startswith(prefix):
                    return False
            elif path == excluded_path:
                return False
            # if path.startswith(excluded_path):
            #     return False

        return True

    def authorization_header(self, request: str = None) -> Union[str, None]:
        """ Takes a Flask request object and returns the Authorization
        header value. Returns None if request is None or if
        Authorization header is not present.
        """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        return header if header else None

    def current_user(self, request: str = None) -> TypeVar('User'):
        """
        Returns None, with the request arg as a flask request object
        """
        return None

    def session_cookie(self, request: str = None) -> str:
        """
        Returns a cookie value from a request
        """
        if request is None:
            return None
        cookie_name = os.getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(cookie_name)
