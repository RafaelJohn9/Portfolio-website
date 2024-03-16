#!/usr/bin/env python3
"""
a module used for movie fetching information
"""
import requests
import json
from typing import List, Dict
import os


def fetch_movies(movie_name: str) -> List[Dict]:
    """
    Fetches movie details from TMDB API.

    Parameters:
    movie_name (str): The name of the movie

    Returns:
    dict: A dictionary containing movie details
    """
    # TMDB API URL
    api_key = os.getenv('MOVIE_API')
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}"

    # Send GET request to TMDB API
    response = requests.get(url)

    # If the request is successful, status code will be 200
    if response.status_code == 200:
        # Get the JSON data from the response
        data = json.loads(response.text)
        
        movies = []
        for movie in data['results']:
            # Create a dictionary to store movie details
            movie_details = {
                             'title': movie['title'],
                             'release_date': movie['release_date'],
                             'overview': movie['overview'],
                             'rating': movie['vote_average'],
                             'poster': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
                             }
            movies.append(movie_details)

        return movies

    else:
        return None
    
if __name__ == "__main__":
    movie_name = "Inception"
    movie_details = fetch_movies(movie_name)
    if movie_details:
        for movie in movie_details:
            print(f"Title: {movie['title']}")
            print(f"Release Date: {movie['release_date']}")
            print(f"Overview: {movie['overview']}")
            print(f"Rating: {movie['rating']}")
            print(f"Poster URL: {movie['poster']}")
            print("\n")
    else:
        print("No movie details found.")
