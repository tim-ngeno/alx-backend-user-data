#!/usr/bin/env python3
""" SQLAlchemy User model """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """
    User module for a database `users`

    Attributes:
        id (int): The primary key column for user ID
        email (str): The column for user email (required)
        hashed_password (str): The column for an encrypted password
        session_id (str): The unique id for a user session
        reset_token (str): A reset token column
    """
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: str = Column(String(250))
    reset_token: str = Column(String(250))
