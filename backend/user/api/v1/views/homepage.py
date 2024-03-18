from api.v1.views import app_views
from flask import render_template

@app_views.route('/homepage')
def homepage():
    return {"message": "welcome"}, 200