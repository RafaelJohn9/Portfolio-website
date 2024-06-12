#!/usr/bin/env python3
"""
Tests for the get_book_download_link function.
"""
import unittest
from unittest.mock import patch
from external_apis.book_downloader.book_downloader import get_book_download_link

class TestGetBookDownloadLink(unittest.TestCase):
    """
    Test class for the get_book_download_link function.
    """

    def setUp(self):
        """Set up common test variables."""
        self.title = "Book Title"
        self.library_genesis_link = "https://example.com/library_genesis/book_title"
        self.pdfdrive_link = "https://example.com/pdfdrive/book_title"
        self.gutendex_link = "https://example.com/gutendex/book_title"

    @patch('external_apis.book_downloader.library_genesis.get_download_url')
    @patch('external_apis.book_downloader.pdfdrive.get_download_url')
    @patch('external_apis.book_downloader.gutendex.get_download_url')
    def test_get_book_download_link(self, mock_gutendex, mock_pdfdrive, mock_library_genesis):
        """
        Test the get_book_download_link function with mocked API responses.
        """
        # Test when library_genesis returns a link
        mock_library_genesis.return_value = self.library_genesis_link
        mock_pdfdrive.return_value = None
        mock_gutendex.return_value = None
        self.assertEqual(get_book_download_link(self.title), self.library_genesis_link)

        # Test when pdfdrive returns a link and library_genesis does not
        mock_library_genesis.return_value = None
        mock_pdfdrive.return_value = self.pdfdrive_link
        mock_gutendex.return_value = None
        self.assertEqual(get_book_download_link(self.title), self.pdfdrive_link)

        # Test when gutendex returns a link and neither library_genesis nor pdfdrive do
        mock_library_genesis.return_value = None
        mock_pdfdrive.return_value = None
        mock_gutendex.return_value = self.gutendex_link
        self.assertEqual(get_book_download_link(self.title), self.gutendex_link)

        # Test when none of the sources return a link
        mock_library_genesis.return_value = None
        mock_pdfdrive.return_value = None
        mock_gutendex.return_value = None
        self.assertIsNone(get_book_download_link(self.title))

if __name__ == '__main__':
    unittest.main()
