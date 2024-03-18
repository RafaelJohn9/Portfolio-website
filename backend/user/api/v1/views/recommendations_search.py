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

@app_views.route('/music/search', methods=['POST'])
def search_music():
    """
    Search for music
    """
    try:
        music_name = request.json['music_name']
        response = fetch_tracks(music_name)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app_views.route('/movie/search', methods=['POST'])
def search_movie():
    """
    Search for movies
    """
    try:
        movie_name = request.json['movie_name']
        response = fetch_movies(movie_name)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app_views.route('/book/search', methods=['POST'])
def search_book():
    """
    Search for books
    """
    try:
        book_name = request.json['book_name']
        response = fetch_books(book_name)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400