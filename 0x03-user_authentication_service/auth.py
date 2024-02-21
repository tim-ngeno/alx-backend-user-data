#!/usr/bin/env python3
""" Auth class module """

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Takes in a string password and returns a byte-hashed salt

    Args:
        password (str): input password to be hashed
    """
    salt = bcrypt.gensalt()
    hash_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hash_pwd


def _generate_uuid() -> str:
    """Returns a string representation of a new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database
    """

    def __init__(self) -> None:
        """Initializes the Auth module
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user into the database
        """
        try:
            if self._db.find_user_by(email=email) is not None:
                raise ValueError(f'User {email} already exists')
        except NoResultFound:
            pass
        hashed_pwd = _hash_password(password).decode('utf-8')
        return self._db.add_user(email=email, hashed_password=hashed_pwd)

    def valid_login(self, email: str, password: str) -> bool:
        """Validates a registered user
        """
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                return bcrypt.checkpw(
                    password.encode('utf-8'),
                    user.hashed_password.encode('utf-8'))
            else:
                return False
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """Finds a user with `email` and generates a session ID
        """
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                session_id = _generate_uuid()
                user.session_id = session_id
                return session_id
            return None
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """Returns the corresponding user from session_id or None
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Updates the corresponding user's ID to None
        """
        user = self._db.find_user_by(id=user_id)
        if user is not None:
            user_id = None
            self._db.update_user(user_id, {'session_id': None})
        else:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Generates a password reset token for the user
        """
        user = self._db.find_user_by(email=email)
        if not user:
            raise ValueError(f'No user found with email: {email}')

        # Generate a UUID for the reset token
        reset_token = _generate_uuid()

        # Update user reset token
        self._db.update_user(user.id, reset_token=reset_token)

        return reset_token
