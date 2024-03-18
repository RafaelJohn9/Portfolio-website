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

@app_views.route('/music/recommended', methods=['GET'])
@login_required
def get_recommended_music():
    """
    Get recommended music
    """
    if not current_user.is_authenticated:
        return redirect(url_for('api_views.login'))
    try:
        user_id = request.json['user_id']
        music_recommendations = storage.all_with(Recommendation, {"item_type": "music", "user_id": user_id})
        return jsonify([fetch_tracks(rec.name, release_date=rec.release_date)[0] for rec in music_recommendations]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    
@app_views.route('/movie/recommended', methods=['GET'])
@login_required
def get_recommended_movies():
    """
    Get recommended movies
    """
    if not current_user.is_authenticated:
        return redirect(url_for('api_views.login'))
    try:
        user_id = request.json['user_id']
        movie_recommendations = storage.all_with(Recommendation, {"item_type": "movie", "user_id": user_id})
        return jsonify([fetch_movies(rec.name, release_date=rec.release_date)[0] for rec in movie_recommendations]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app_views.route('/book/recommended', methods=['GET'])
@login_required
def get_recommended_books():
    """
    Get recommended books
    """
    if not current_user.is_authenticated:
        return redirect(url_for('api_views.login'))
    try:
        user_id = request.json['user_id']
        book_recommendations = storage.all_with(Recommendation, {"item_type": "book", "user_id": user_id})
        return jsonify([fetch_books(rec.name, release_date=rec.release_date)[0] for rec in book_recommendations]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app_views.route('/book/all-recommended', methods=['GET'])
@login_required
def get_all_recommended_books():
    """
    Get all recommended books
    """
    if not current_user.is_authenticated:
        return redirect(url_for('api_views.login'))
    try:
        book_recommendations = storage.all_with(Recommendation, {"item_type": "book"})
        return jsonify([fetch_books(book.name, release_date=book.release_date)[0] for book in book_recommendations])
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app_views.route('/music/all-recommended', methods=['GET'])
@login_required
def get_all_recommended_music():
    """
    Get all recommended music
    """
    if not current_user.is_authenticated:
        return redirect(url_for('api_views.login'))
    try:
        music_recommendations = storage.all_with(Recommendation, {"item_type": "music"})
        return jsonify([fetch_tracks(music.name, release_date=music.release_date) for music in music_recommendations])
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app_views.route('/movie/all-recommended', methods=['GET'])
@login_required
def get_all_recommended_movies():
    """
    Get all recommended movies
    """
    if not current_user.is_authenticated:
        return redirect(url_for('api_views.login'))
    try:
        movie_recommendations = storage.all_with(Recommendation, {"item_type": "movie"})
        return jsonify([fetch_movies(movie.name, release_date=movie.release_date) for movie in movie_recommendations])
    except Exception as e:
        return jsonify({"error": str(e)}), 400
