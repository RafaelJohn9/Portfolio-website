#!/usr/bin/env python3
"""This module creates a Flask app"""
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from
from models import storage
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
app.secret_key = getenv('SECRET_KEY', 'default-secret-key')

app.config['SESSION_TYPE'] = 'filesystem'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

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
    host = getenv('USER_API_HOST', '0.0.0.0')
    port = getenv('USER_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
