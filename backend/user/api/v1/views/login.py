#!/usr/bin/env python3
from flask import jsonify, request
from flask_login import login_user, logout_user, LoginManager, UserMixin
from werkzeug.security import check_password_hash
from models import storage
from models.user import User
from api.v1.views import app_views

login_manager = LoginManager()
login_manager.init_app(app_views)

@login_manager.user_loader
def load_user(user_id):
    return storage.get(User, user_id)

@app_views.route('/login', methods=['POST'])
def login():
    """
    Logs in a user
    """
    data = request.get_json()
    if 'email' not in data or 'password' not in data:
        return jsonify({"message": "Missing email or password"}), 400

    user = storage.get(User, email=data.get('email'))

    if not user or not check_password_hash(user.password, data.get('password')):
        return jsonify({"message": "Invalid email or password"}), 401

    login_user(user)
    return jsonify({"message": "Logged in successfully", "user_id": user.userId}), 200

@app_views.route('/logout', methods=['POST'])
def logout():
    """
    Logs out a user
    """
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200
