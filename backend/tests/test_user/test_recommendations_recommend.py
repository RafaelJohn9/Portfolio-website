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


class RecommendationsRecommendTestCase(unittest.TestCase):
    base_url = "http://0.0.0.0:5000/api/v1/user"
    def setUp(self):
        self.session = requests.Session()
        self.base_url = "http://localhost:5000/api/v1/user"
        # Create a new user
        url = f"{self.base_url}/create"
        data = {
            "email": "testonRecommendations@example.com",
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
            "email": "testonRecommendations@example.com",
            "password": "password123"
        }
        response_login = self.session.post(url, json=data)
        self.assertEqual(response_login.status_code, 200)
        
    def tearDown(self):
        # Delete the user
        url = f"{self.base_url}/delete/{user_data['userId']}"
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        
    def test_recommend_music(self):
        url = f"{self.base_url}/music/recommend"
        data = fetch_tracks("Never Gonna Give You Up")[0]
        response = self.session.post(url, json=data)
        # Add assertions to validate the response
        self.assertTrue(response.status_code, 200)
        
        # Delete the recommended music
        delete_url = f"{self.base_url}/music/recommended/delete"
        delete_response = self.session.delete(delete_url, json=data)
        # Add assertions to validate the delete response
        self.assertEqual(delete_response.status_code, 200)
        
    def test_recommend_movie(self):
        url = f"{self.base_url}/movie/recommend"
        data = fetch_movies("The Matrix")[0]
        response = self.session.post(url, json=data)
        # Add assertions to validate the response
        self.assertTrue(response.status_code, 200)
        self.assertTrue(response.json(), list)
        
        # Delete the recommended movie
        delete_url = f"{self.base_url}/movie/recommended/delete"
        delete_response = self.session.delete(delete_url, json=data)
        # Add assertions to validate the delete response
        self.assertEqual(delete_response.status_code, 200)

    def test_recommend_book(self):
        url = f"{self.base_url}/book/recommend"
        data = fetch_books("The Alchemist")[0]
        response = self.session.post(url, json=data)
        # Add assertions to validate the response
        self.assertTrue(response.status_code, 200)
        
        # Delete the recommended book
        delete_url = f"{self.base_url}/book/recommended/delete"
        delete_response = self.session.delete(delete_url, json=data)
        # Add assertions to validate the delete response
        self.assertEqual(delete_response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
