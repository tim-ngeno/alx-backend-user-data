#!/usr/bin/env python3
""" Basic Authentication module """
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar, Union
from models.user import User


class BasicAuth(Auth):
    """
    Basic authentication
    """

    def __init__(self):
        """Initializes BasicAuth class"""
        super().__init__()

    def extract_base64_authorization_header(
            self, authorization_header:  str) -> Union[str, None]:
        """ Returns the Base64 part of the Authorization header for
        Basic Authentication. Returns None if authorization_header is
        None, not a string, or doesn't start with 'Basic '. Otherwise,
        returns the value after 'Basic '.

        Args:
            authorization_header (str): The Authorization header string.

        Returns:
            str: The Base64 part of the Authorization header, or None if
        not found.
        """
        if (authorization_header is None or
                not isinstance(authorization_header, str)):
            return None
        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(' ', 1)[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> Union[str, None]:
        """
        Returns the decoded value of a Base64 string
        """
        if (base64_authorization_header is None or
                not isinstance(base64_authorization_header, str)):
            return None
        try:
            # Decode the base64 string
            decoded_bytes = base64.b64decode(
                base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts user credentials from the base64 decoded value
        """
        if (decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str)):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        # Split only at the first occurrence of the colon
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the user instance based on the email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})

        if not users:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves a User instance for a request
        """
        if request is None:
            return None
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        credentials = self.extract_base64_authorization_header(
            auth_header)
        if credentials is None:
            return None

        decoded_credentials = self.decode_base64_authorization_header(
            credentials)
        if decoded_credentials is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(
            decoded_credentials)
        if user_email is None or user_pwd is None:
            return None

        return self.user_object_from_credentials(user_email, user_pwd)
