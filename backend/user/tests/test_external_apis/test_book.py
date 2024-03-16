#!/usr/bin/env python3
 
import os
import unittest
from unittest.mock import patch
from external_apis.book import fetch_books

class TestFetchBooks(unittest.TestCase):
    @patch('external_apis.book.requests.get')
    def test_fetch_books_success(self, mock_get):
        # Mock the response from the API
        mock_response = {
            "items": [
                {
                    "volumeInfo": {
                        "title": "Book 1",
                        "authors": ["Author 1"],
                        "pageCount": 100,
                        "publishedDate": "2022-01-01",
                        "averageRating": 4.5,
                        "categories": ["Fiction"],
                        "publisher": "Publisher 1",
                        "imageLinks": {
                            "thumbnail": "https://example.com/book1.jpg"
                        }
                    }
                },
                {
                    "volumeInfo": {
                        "title": "Book 2",
                        "authors": ["Author 2"],
                        "pageCount": 200,
                        "publishedDate": "2022-02-01",
                        "averageRating": 3.8,
                        "categories": ["Non-fiction"],
                        "publisher": "Publisher 2",
                        "imageLinks": {
                            "thumbnail": "https://example.com/book2.jpg"
                        }
                    }
                }
            ]
        }
        mock_get.return_value.json.return_value = mock_response

        # Set the environment variable
        os.environ['BOOK_API'] = 'your_api_key'

        # Call the function
        books = fetch_books("harry potter")

        # Assert the expected results
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0]["title"], "Book 1")
        self.assertEqual(books[0]["authors"], ["Author 1"])
        self.assertEqual(books[0]["pages"], 100)
        self.assertEqual(books[0]["release_date"], "2022-01-01")
        self.assertEqual(books[0]["rating"], 4.5)
        self.assertEqual(books[0]["genre"], ["Fiction"])
        self.assertEqual(books[0]["publisher"], "Publisher 1")
        self.assertEqual(books[0]["cover_images"], {"thumbnail": "https://example.com/book1.jpg"})
        self.assertEqual(books[1]["title"], "Book 2")
        self.assertEqual(books[1]["authors"], ["Author 2"])
        self.assertEqual(books[1]["pages"], 200)
        self.assertEqual(books[1]["release_date"], "2022-02-01")
        self.assertEqual(books[1]["rating"], 3.8)
        self.assertEqual(books[1]["genre"], ["Non-fiction"])
        self.assertEqual(books[1]["publisher"], "Publisher 2")
        self.assertEqual(books[1]["cover_images"], {"thumbnail": "https://example.com/book2.jpg"})

    @patch('external_apis.book.requests.get')
    def test_fetch_books_no_results(self, mock_get):
        # Mock the response from the API with no items
        mock_response = {
            "items": []
        }
        mock_get.return_value.json.return_value = mock_response

        # Set the environment variable
        os.environ['BOOK_API'] = 'your_api_key'

        # Call the function
        books = fetch_books("nonexistent book")

        # Assert the expected results
        self.assertEqual(len(books), 0)

if __name__ == '__main__':
    unittest.main()

