#!/usr/bin/env python3
"""route for downloading recommendations (movies, music, books)"""
from flask import request, jsonify
from api.v1.views import app_views
from external_apis.music_downloader.main import music_downloader

@app_views.route('/music/download', methods=['GET'])
def download_music():
    """defining route for downloading music"""
    data = request.get_json()
    query = data.get('query', None)
    
    # check if query is empty or is provided
    if not query or query == '':
        return jsonify({'error': 'query not entered'}), 400

    return jsonify(music_downloader(query)), 200


