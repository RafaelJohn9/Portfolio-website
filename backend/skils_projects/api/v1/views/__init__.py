"""
__init__.py is the file that initializes the blueprint object and imports the views.
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.skills import *
