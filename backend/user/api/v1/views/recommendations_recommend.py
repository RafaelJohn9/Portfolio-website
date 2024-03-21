#!/usr/bin/env python3
"""
Module for handling recommendations
"""
from api.v1.views import app_views
from models import storage
from models.recommendation import Recommendation
from external_apis.book import fetch_books
from external_apis.movie import fetch_movies
from external_apis.music import fetch_tracks
from flask import request, jsonify
from flask_login import login_required
from flask_login import current_user
from flask import redirect, url_for

@app_views.route('/music/recommend', methods=['POST'])
@login_required
def recommend_music():
    """
    Recommend music
    """
    if not current_user.is_authenticated:
        return jsonify({"error": "Unauthorized"}), 401
    try:
        data = request.json
        track_name = data['Track Name']
        item_type = data['item_type']
        release_date = data['release_date']
        user_id = current_user.userId
        new_recommendation = Recommendation(name=track_name, item_type=item_type, user_id=user_id, release_date=release_date)
        storage.new(new_recommendation)
        storage.save()
        return jsonify({"success": "Music recommendation saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app_views.route('/movie/recommend', methods=['POST'])
@login_required
def recommend_movie():
    """
    Recommend movie
    """
    if not current_user.is_authenticated:
        return jsonify({"error": "Unauthorized"}), 401
    try:
        data = request.json
        title = data['title']
        item_type = data['item_type']
        user_id = current_user.userId
        release_date = data['release_date']
        new_recommendation = Recommendation(name=title, item_type=item_type, user_id=user_id, release_date=release_date)
        storage.new(new_recommendation)
        storage.save()
        return jsonify({"success": "Movie recommendation saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app_views.route('/book/recommend', methods=['POST'])
@login_required
def recommend_book():
    """
    Recommend book
    """
    if not current_user.is_authenticated:
        return jsonify({"error": "Unauthorized"}), 401
    try:
        data = request.json
        title = data['title']
        item_type = data['item_type']
        release_date = data['release_date']
        user_id = current_user.userId
        new_recommendation = Recommendation(name=title, item_type=item_type, user_id=user_id, release_date=release_date)
        storage.new(new_recommendation)
        storage.save()
        return jsonify({"success": "Book recommendation saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
