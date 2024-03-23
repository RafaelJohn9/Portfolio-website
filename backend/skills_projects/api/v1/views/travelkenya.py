"""
This module contains the logic for the travelkenya route
"""
from flask import jsonify
from api.v1.views import app_views
import json

# Define the route
@app_views.route('/projects/travelkenya', methods=['GET'])
def get_travel_kenya():
    """
    This function returns the json data from travel_kenya.json file
    """
    try:
        # Open the json file
        with open('projects/travel_kenya/travel_kenya.json', 'r') as file:
            data = json.load(file)
        return jsonify(data), 200
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500