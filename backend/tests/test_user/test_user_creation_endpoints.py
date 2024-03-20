import requests
import unittest
import json

#!/usr/bin/env python3
# Global variable to store user data
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

class TestAPIEndpoints(unittest.TestCase):
    """
    Test API endpoints
    """
    def setUp(self):
        """
        Create a new user and store the user data in the global variable USER
        """
        self.base_url = "http://localhost:5000/api/v1"
        # User data
        self.user_data = {
            "email": "testing3user@example.com",
            "password": "testpassword"
        }
        response = requests.post(f"{self.base_url}/user/create", json=self.user_data)
        self.assertEqual(response.status_code, 201)
        global USER
        USER = response.json()
        global user_data
        user_data = extract_user_data(USER) if USER else {}
        
    def test_user_update(self):
        """
        Test user update endpoint
        """
        # Update user data
        updated_data = {
            "username": "newusername",
            "password": "newpassword"
            }
        response = requests.put(f"{self.base_url}/user/update/{user_data['userId']}", json=updated_data)
        self.assertEqual(response.status_code, 200)
    
    def test_user_fetch(self):
        """
        Test user fetch endpoint
        """
        response = requests.get(f"{self.base_url}/user/fetch/{user_data['userId']}")
        self.assertEqual(response.status_code, 200)
        # Check if the fetched user data is correct
        fetched_user = response.json()['user']
        self.assertEqual(fetched_user['email'], user_data['email'])
        
    def tearDown(self):
        """
        Delete the user created in the setUp method
        """
        # Now you can proceed with the rest of your code
        response = requests.delete(f"{self.base_url}/user/delete/{user_data['userId']}")
        self.assertEqual(response.status_code, 200)
