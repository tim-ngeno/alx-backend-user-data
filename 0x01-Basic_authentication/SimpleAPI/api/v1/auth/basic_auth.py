#!/usr/bin/env python3
""" Basic Authentication module """
from api.v1.auth.auth import Auth
import base64
from typing import Union


class BasicAuth(Auth):
    """
    Basic authentication
    """

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
        except Exception as e:
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
        return tuple(decoded_base64_authorization_header.split(':'))
