#!/usr/bin/env python3
""" Hashing password module """

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Takes in a string password and returns a byte-hashed salt
    """
    salt = bcrypt.gensalt()
    hash_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hash_pwd
