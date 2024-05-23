import unittest
from unittest.mock import patch
from external_apis.music_downloader.main import music_downloader

class TestMusicDownloader(unittest.TestCase):
    """test class for music_downloader function"""
    
    @patch('music_downloader.get_music_link')
    @patch('music_downloader.music_download_link')
    def test_music_downloader_success(self, mock_music_download_link, mock_get_music_link):
        """test music downloader during success"""
        mock_get_music_link.return_value = 'https://example.com/music'
        mock_music_download_link.return_value = 'https://example.com/download'
        
        query = 'song'
        result = music_downloader(query)
        
        self.assertEqual(result, 'https://example.com/download')
        mock_get_music_link.assert_called_once_with(query)
        mock_music_download_link.assert_called_once_with('https://example.com/music')
    
    @patch('music_downloader.get_music_link')
    @patch('music_downloader.music_download_link')
    def test_music_downloader_exception(self, mock_music_download_link, mock_get_music_link):
        """test music downloader during exception"""
        mock_get_music_link.side_effect = Exception('An error occurred')
        
        query = 'song'
        result = music_downloader(query)
        
        self.assertIsNone(result)
        mock_get_music_link.assert_called_once_with(query)
        mock_music_download_link.assert_not_called()

if __name__ == '__main__':
    unittest.main()