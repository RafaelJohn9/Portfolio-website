"""
This module contains the API endpoint for retrieving skills.

It defines a Blueprint named `app_views` and a route `/skills` that handles GET requests.
The route retrieves the skills available from a JSON file located at `FILE_PATH`.

Functions:
- get_skills: Retrieves the skills available from the JSON file and returns them as a JSON response.

Exceptions:
- FileNotFoundError: Raised when the JSON file is not found.
- json.JSONDecodeError: Raised when there is an error decoding the JSON file.
- Exception: Raised for any other unexpected error.

"""
from flask import Blueprint, jsonify
import os
import json
from api.v1.views import app_views

FILE_PATH = "./skills/skills.json"

@app_views.route('/skills', methods=['GET'])
def get_skills():
    """
    Retrieves the skills available from the JSON file and returns them as a JSON response.

    Returns:
    - If the JSON file is found and successfully loaded, returns a JSON response with the skills and status code 200.
    - If the JSON file is not found, returns a JSON response with an error message and status code 404.
    - If there is an error decoding the JSON file, returns a JSON response with an error message and status code 400.
    - If there is any other unexpected error, returns a JSON response with the error message and status code 500.
    """
    try:
        with open(FILE_PATH, 'r') as f:
            skills = json.load(f)
        return jsonify(skills), 200
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500