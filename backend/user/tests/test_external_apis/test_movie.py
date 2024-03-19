#!/usr/bin/env python3

from external_apis.movie import fetch_movies
import unittest
from unittest.mock import patch
import json

class TestFetchMovies(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_movies_success(self, mock_get):
        # Mock the response from the TMDB API
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = '{"results": [{"title": "Inception", "release_date": "2010-07-16", "overview": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.", "vote_average": 8.3, "poster_path": "/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg"}]}'

        # Call the fetch_movies function
        movie_name = "Inception"
        movie_details = fetch_movies(movie_name)

        # Assert the expected movie details
        expected_movie_details = [{"results": [{"title": "Inception", "release_date": "2010-07-16", "overview": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.", "vote_average": 8.3, "poster_path": "/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg"}]}]
        self.assertEqual(json.dumps(movie_details), expected_movie_details[0])

    @patch('requests.get')
    def test_fetch_movies_failure(self, mock_get):
        # Mock the response from the TMDB API
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        # Call the fetch_movies function
        movie_name = "Nonexistent Movie"
        movie_details = fetch_movies(movie_name)

        # Assert that no movie details are returned
        self.assertIsNone(movie_details)

if __name__ == '__main__':
    unittest.main()
