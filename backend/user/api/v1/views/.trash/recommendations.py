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
        return redirect(url_for('api_views.login'))
    try:
        data = request.json
        track_name = data['track_name']
        item_type = data['item_type']
        release_date = data['Release date']
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
        return redirect(url_for('api_views.login'))
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
        return redirect(url_for('api_views.login'))
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
        return jsonify([book.to_dict() for book in book_recommendations])
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
        return jsonify([music.to_dict() for music in music_recommendations])
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
        return jsonify([movie.to_dict() for movie in movie_recommendations])
    except Exception as e:
        return jsonify({"error": str(e)}), 400
