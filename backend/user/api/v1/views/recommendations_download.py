#!/usr/bin/env python3
"""Route for downloading recommendations (movies, music, books)"""
import io
from flask import request, jsonify, send_file, make_response
from pytube import YouTube
from api.v1.views import app_views
from external_apis.music_downloader.music_link_getter import get_music_link
from external_apis.book_downloader.book_downloader import get_book_download_link


@app_views.route('/music/download', methods=['POST'])
def download_music():
    """Defining route for downloading music"""
    data = request.get_json()
    query = data.get('query', None)

    # Check if query is empty or is provided
    if not query or query == '':
        return jsonify({'error': 'query not entered'}), 400

    # Use the get_music_link function to get the YouTube URL or process the query
    youtube_url = get_music_link(query)  # This should return the YouTube URL based on the query

    if not youtube_url:
        return jsonify({'error': 'No video found for the given query'}), 404

    # Create a YouTube object
    yt = YouTube(youtube_url)

    # Get the audio-only stream
    audio_stream = yt.streams.filter(only_audio=True).first()

    audio_file = io.BytesIO()

    audio_stream.stream_to_buffer(audio_file)
    audio_file.seek(0)

    # Send the audio file as a response
    response = make_response(send_file(audio_file, mimetype='audio/mpeg'))
    response.headers['Content-Disposition'] = f'attachment; filename={audio_stream.default_filename}'

    return response

@app_views.route('/book/download', methods=['POST'])
def download_book():
    """Defining route for downloading books"""
    data = request.get_json()
    title = data.get('title', None)

    # Check if title is empty or is provided
    if not title or title == '':
        return jsonify({'error': 'title not entered'}), 400

    # Use the get_book_download_link function to get the download link based on the title
    download_link = get_book_download_link(title)

    if not download_link:
        return jsonify({'error': 'No download link found for the given title'}), 404

    # Send the download link as a response
    return jsonify({'download_link': download_link})