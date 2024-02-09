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
