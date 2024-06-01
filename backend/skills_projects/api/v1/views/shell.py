"""
This module contains the API endpoint for the simple_shell
"""
from flask import request, jsonify
from projects.simple_shell.pass_commands_to_shell import pass_cmd_to_shell
from api.v1.views import app_views  # Import the Blueprint object

@app_views.route('/projects/shell', methods=['POST'])
def shell():
    """
    Handle POST requests to '/shell' endpoint.

    This function receives a command from the request's JSON payload,
    passes the command to the shell, and returns the result as a JSON response.

    Returns:
        A JSON response containing the result of the shell command.
    """
    try:
        command = request.json.get('command')
        result = pass_cmd_to_shell(command)
        return jsonify({'$': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500