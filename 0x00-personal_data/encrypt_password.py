#!/usr/bin/env python3
""" Encrypting passwords using bcrypt """

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a string password using bcrypt

    Args:
        password (str): the password argument to be hashed
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that the provided password matches the hashed password

    Args:
        hashed_password (bytes): The hashed version of the password
        password (str): The original password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
