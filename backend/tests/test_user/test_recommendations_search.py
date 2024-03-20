import unittest
import requests

class TestRecommendationsSearch(unittest.TestCase):
    base_url = "http://0.0.0.0:5000/api/v1/user"

    def test_search_music(self):
        response = requests.post(f"{self.base_url}/music/search", json={"music_name": "test"})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_search_movie(self):
        response = requests.post(f"{self.base_url}/movie/search", json={"movie_name": "test"})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_search_book(self):
        response = requests.post(f"{self.base_url}/book/search", json={"book_name": "test"})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

if __name__ == "__main__":
    unittest.main()