#!/usr/bin/env python3
"""
Main module for the API.
"""
from flask import Flask, jsonify
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*", "supports_credentials": True}})

@app.after_request
def add_cors_headers(response):
    """
    Add CORS headers to the response.
    
    Args:
        response (flask.Response): The response object.
    
    Returns:
        flask.Response: The response object with added CORS headers.
    """
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route('/')
def home():
    """
    Home route handler.
    
    Returns:
        dict: A dictionary with a welcome message.
    """
    return {"message": "Welcome"}

app.register_blueprint(app_views)
@app.errorhandler(404)
def page_not_found(e):
    """
    Error handler for 404 Not Found.
    
    Args:
        e (Exception): The exception object.
    
    Returns:
        tuple: A tuple containing the error message and status code.
    """
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(host='localhost', port=5001)