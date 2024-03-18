#!/usr/bin/env python3
# Define a function to set up Flask-Login within the application context
"""
Login and logout routes
"""
from api.v1.views import app_views
from flask import jsonify, redirect, request, url_for
from flask_login import login_user, logout_user
from models import storage
from models.user import User
from werkzeug.security import check_password_hash
from flask_login import LoginManager
from flask import current_app


@app_views.route('/login', methods=['POST'])
def login():
    """
    Logs in a user
    """
    data = request.get_json()
    if 'email' not in data:
        return jsonify({"message": "Missing email"}), 400

    if 'password' not in data:
        return jsonify({"message": "Missing password"}), 400

    try:
        user = storage.get(User, email=data.get('email'))
    except Exception as e:
        return jsonify(
                {"message": "Internal server error",
                 "error": str(e)
                 }), 500

    if not user:
        return jsonify({"message": "User does not exist"}), 404

    if user and check_password_hash(user.password, data.get('password')):
        login_user(user)
        return redirect(url_for('app_views.dashboard', user_id=user.userId))

    return jsonify({"message": "Invalid email or password"}), 401


@app_views.route('/logout', methods=['POST'])
def logout():
    """
    Logs out a user
    """
    logout_user()
    return redirect(
            url_for('app_views.homepage',
                    message="Logged out successfully")
            )
