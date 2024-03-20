#!/usr/bin/python3
"""
    This is a simple route for creating a new user
"""
from api.v1.views import app_views
from flask import Flask, request, jsonify
from werkzeug.exceptions import Conflict
from models.user import User
from models import storage
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import DataError


@app_views.route('/create', methods=['POST'], strict_slashes=False)
def create_user():
    """
    Create a new user and save it in the storage.
    """
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    new_user = User(username=username, email=email, password=password)
    try:
        storage.new(new_user)
    except IntegrityError as e:
        error_message = str(e)
        if 'email' in error_message:
            return jsonify({'error': 'User with email already exists'}), 409
        elif 'username' in error_message:
            return jsonify({'error': 'User with username already exists'}), 409
        else:
            return jsonify({'error': error_message}), 409
    except DataError as e:
        return jsonify({'error': 'Invalid data provided'}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
    return jsonify({
                    'message': 'New user created',
                    'user': str(new_user.to_dict())
                    }), 201


@app_views.route('/update/<string:userId>',
                 methods=['PUT'],
                 strict_slashes=False)
def update_user(userId):
    """
    Update a user and save the changes in the storage.
    """
    try:
        data = request.get_json()
        user = storage.get(User, userId=userId)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        for key, value in data.items():
            if key in ['username', 'email', 'password']:
                if key == 'username' and storage.get(User, username=value):
                    return jsonify({'error': 'Username already exists'}), 409
                elif key == 'email' and storage.get(User, email=value):
                    return jsonify({'error': 'Email already exists'}), 409
                else:
                    kwargs = {key: value}
                    storage.update(user, **kwargs)
        storage.save()
        return jsonify({'message': 'User updated', 'user': user.to_dict()}), 200
    except DataError as e:
        return jsonify({'error': 'Invalid data provided'}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500


@app_views.route('/delete/<string:userId>',
                 methods=['DELETE'],
                 strict_slashes=False)
def delete_user(userId):
    """
    Delete a user from the storage.
    """
    user = storage.get(User, userId=userId)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    storage.delete_items_with(User, userId=userId)
    storage.save()
    return jsonify({'message': 'User deleted'}), 200


@app_views.route('/fetch/<string:userId>',
                 methods=['GET'],
                 strict_slashes=False)
def fetch_user(userId):
    """
    Fetch a user from the storage.
    """
    user = storage.get(User, userId=userId)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'user': user.to_dict()}), 200
