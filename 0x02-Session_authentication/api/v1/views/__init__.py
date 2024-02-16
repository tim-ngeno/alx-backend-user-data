#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *
from .session_auth import session_auth_bp


User.load_from_file()

app_views.register_blueprint(session_auth_bp)
