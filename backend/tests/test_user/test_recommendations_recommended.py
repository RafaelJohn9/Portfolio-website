import unittest
import requests
import json
from user.external_apis.book import fetch_books
from user.external_apis.movie import fetch_movies
from user.external_apis.music import fetch_tracks

USER = {}
user_data = {}


def extract_user_data(user):
    """
    Extract user data from the user dictionary
    """
    # Assuming USER is a dictionary containing JSON data
    user_json = user["user"].replace("'", '"').replace("None", "null")
    # Parse the JSON string
    user_data = json.loads(user_json)
    return user_data


class UserLoginTestCase(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.base_url = "http://localhost:5000/api/v1/user"
        # Create a new user
        url = f"{self.base_url}/create"
        data = {
            "email": "testonRecommended@example.com",
            "password": "password123",
            "username": "testuser"
        }
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 201)
        global USER
        USER = response.json()
        global user_data
        user_data = extract_user_data(USER) if USER else {}
        
        # User login
        url = f"{self.base_url}/login"
        data = {
            "email": "testonRecommended@example.com",
            "password": "password123"
        }
        response_login = self.session.post(url, json=data)
        self.assertEqual(response_login.status_code, 200)
        
        # Create recommendations to be fetched
        # for movie
        url_movie = f"{self.base_url}/movie/recommend"
        self.data_movie = fetch_movies("Inception")[0]
        response = self.session.post(url_movie, json=self.data_movie)
        self.assertEqual(response.status_code, 200)
        
        # for music
        url_music = f"{self.base_url}/music/recommend"
        self.data_music = fetch_tracks("Never Gonna Give You Up")[0]
        response = self.session.post(url_music, json=self.data_music)
        self.assertEqual(response.status_code, 200)
        
        # for book
        url_book = f"{self.base_url}/book/recommend"
        self.data_book = fetch_books("The Great Gatsby")[0]
        response = self.session.post(url_book, json=self.data_book)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        # Delete the user's recommendations
        url_music = f"{self.base_url}/music/recommended/delete"
        url_movie = f"{self.base_url}/movie/recommended/delete"
        url_book = f"{self.base_url}/book/recommended/delete"
        response = self.session.delete(url_music, json=self.data_music)
        self.assertEqual(response.status_code, 200)
        response = self.session.delete(url_movie, json=self.data_movie)
        self.assertEqual(response.status_code, 200)
        response = self.session.delete(url_book, json=self.data_book)
        self.assertEqual(response.status_code, 200)
        

        # Delete the user
        url = f"{self.base_url}/delete/{user_data['userId']}"
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)

    def test_get_recommended_music(self):
        url = f"{self.base_url}/music/recommended"
        json_data = {
            "user_id": user_data["userId"]
        }
        response = self.session.get(url, json=json_data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_recommended_movies(self):
        url = f"{self.base_url}/movie/recommended"
        response = self.session.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_recommended_books(self):
        url = f"{self.base_url}/book/recommended"
        response = self.session.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        
    def test_get_all_recommended_books(self):
        url = f"{self.base_url}/book/all-recommended"
        response = self.session.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_all_recommended_music(self):
        url = f"{self.base_url}/music/all-recommended"
        response = self.session.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_all_recommended_movies(self):
        url = f"{self.base_url}/movie/all-recommended"
        response = self.session.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
