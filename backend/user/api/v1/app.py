#!/usr/bin/env python3
"""This module creates a Flask app"""
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger
from models import storage
from os import getenv
from flask_login import LoginManager
from flask import current_app
from models.user import User


def setup_login_manager():
    """ a function to set up Flask-Login
    within the application context
    """
    with current_app.app_context():
        current_app.login_manager = login_manager

        @login_manager.user_loader
        def load_user(user_id):
            """
            load_user function that is used to load the current user
            """
            return storage.get(User, userId=user_id)


app = Flask(__name__)
app.register_blueprint(app_views)
app.secret_key = getenv('SECRET_KEY', 'default-secret-key')

app.config['SESSION_TYPE'] = 'filesystem'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'app_views.login'


@login_manager.user_loader
def load_user(user_id):
    """ Load and return the user object based on the user_id """
    return storage.get(User, userId=user_id)


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.route('/')
def home():
    """ Home route
    ---
    responses:
    200:
    description: Welcome message
    """
    # Call the setup function after the application is created
    setup_login_manager()
    return jsonify({"message": "Welcome"}), 200


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return jsonify({"error": "Not found"}), 404


app.config['SWAGGER'] = {
    'title': 'Portfolio Website Restful API',
    'uiversion': 3
}

Swagger(app)


if __name__ == "__main__":
    """ Main Function """
    host = getenv('USER_API_HOST', 'localhost')
    port = getenv('USER_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
