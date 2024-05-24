#!/usr/bin/env python3
"""this is the test file for the music_downloader function"""
import unittest
from unittest.mock import patch
from external_apis.music_downloader.main import music_downloader

class TestMusicDownloader(unittest.TestCase):
    """class to test the music_downloader function"""

    @patch('external_apis.music_downloader.main.get_music_link')
    @patch('external_apis.music_downloader.main.music_download_link')
    def test_music_downloader_success(self, mock_music_download_link, mock_get_music_link):
        """test the music_downloader function when it is successful"""
        # Configure mock_get_music_link to return a mock music link
        mock_get_music_link.return_value = 'https://www.youtube.com/watch?v=video_id'

        # Configure mock_music_download_link to return a mock download link
        mock_music_download_link.return_value = 'https://www.example.com/download'

        # Call the function under test
        result = music_downloader('song_query')

        # Assertions
        self.assertEqual(result, 'https://www.example.com/download')
        mock_get_music_link.assert_called_once_with('song_query')
        mock_music_download_link.assert_called_once_with('https://www.youtube.com/watch?v=video_id')


    @patch('external_apis.music_downloader.main.get_music_link')
    @patch('external_apis.music_downloader.main.music_download_link')
    def test_music_downloader_no_result(self, mock_music_download_link, mock_get_music_link):
        """test the music_downloader function when no music link is found"""
        # Configure mock_get_music_link to return None (no music link found)
        mock_get_music_link.return_value = None
        mock_music_download_link.return_value = None
        
        # Call the function under test
        result = music_downloader('song_query')

        # Assertions
        self.assertIsNone(result)  # Ensure result is None when no music link is found
        

    @patch('external_apis.music_downloader.main.get_music_link')
    @patch('external_apis.music_downloader.main.music_download_link')
    def test_music_downloader_download_failure(self, mock_music_download_link, mock_get_music_link):
        """test the music_downloader function when music download fails"""
        # Configure mock_get_music_link to return a mock music link
        mock_get_music_link.return_value = 'https://www.youtube.com/watch?v=video_id'

        # Configure mock_music_download_link to return None (download failure)
        mock_music_download_link.return_value = None

        # Call the function under test
        result = music_downloader('song_query')

        # Assertions
        self.assertIsNone(result)
        mock_get_music_link.assert_called_once_with('song_query')
        mock_music_download_link.assert_called_once_with('https://www.youtube.com/watch?v=video_id')

if __name__ == '__main__':
    unittest.main()