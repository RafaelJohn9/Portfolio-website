import unittest
import requests
import json
"""
Test user login endpoint
"""
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
        self.base_url = "http://localhost:5000/api/v1/user"
        # Create a new user
        url = f"{self.base_url}/create"
        data = {
            "email": "testonUser@example.com",
            "password": "password123",
            "username": "testuser"
        }
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 201)
        self.user_id = extract_user_data(response.json())["userId"]
    
    def test_user_login(self):
        # Test user login
        url = f"{self.base_url}/login"
        data = {
            "email": "testonUser@example.com",
            "password": "password123"
        } 
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        user_data = response.json()

    
    def test_user_login_missing_data(self):
        # Test user login with missing data
        url = f"{self.base_url}/login"
        data = {}
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 400)
        user_data = response.json()
        self.assertEqual(user_data["message"], "Missing email or password")
    
    def test_user_login_wrong_password(self):
        # Test user login failure
        url = f"{self.base_url}/login"
        data = {
            "email": "testonUser@example.com",
            "password": "password"
        }
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 401)
        user_data = response.json()
        self.assertEqual(user_data["message"], "Invalid email or password")
    
    def test_user_login_wrong_email(self):
        # Test user login failure
        url = f"{self.base_url}/login"
        data = {
            "email": "hello@example.com",
            "password": "password123"
        }
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 401)
        user_data = response.json()
        self.assertEqual(user_data["message"], "Invalid email or password")
    
    def test_user_login_missing_email(self):
        # Test user login failure
        url = f"{self.base_url}/login"
        data = {
            "password": "password123"
        }
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 400)
        user_data = response.json()
        self.assertEqual(user_data["message"], "Missing email or password")
    
    def test_user_login_missing_password(self):
        # Test user login failure
        url = f"{self.base_url}/login"
        data = {
            "email": "hello@example.com"
        }
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 400)
        user_data = response.json()
        self.assertEqual(user_data["message"], "Missing email or password")
    
    def test_user_logout(self):
        # Test user logout
        url = f"{self.base_url}/logout"
        response = requests.post(url)
        self.assertEqual(response.status_code, 200)
        user_data = response.json()
        # redirected to homepage so response changes to welcome
        self.assertEqual(user_data["message"], "Logged out successfully")

    def tearDown(self):
        # Delete the user
        url = f"{self.base_url}/delete/{self.user_id}"
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        
if __name__ == "__main__":
    unittest.main()