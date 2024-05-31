#!/usr/bin/env python3
"""
contains the homepage route
"""
from api.v1.views import app_views
from flask import render_template


@app_views.route('/homepage')
def homepage():
    """
    homepage endpoint
    """
    return {"message": "welcome"}, 200
