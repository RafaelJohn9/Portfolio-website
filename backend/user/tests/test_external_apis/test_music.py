#!/usr/bin/env python3
import requests
import unittest
from unittest.mock import patch
from external_apis.music import fetch_tracks

class TestMusicAPI(unittest.TestCase):
    @patch('external_apis.music.requests.get')
    def test_fetch_tracks_success(self, mock_get):
        # Mock the response from the API
        mock_response = {
            'tracks': {
                'items': [
                    {
                        'name': 'Track 1',
                        'artists': [{'name': 'Artist 1'}],
                        'preview_url': 'https://example.com/track1',
                        'album': {'images': [{'url': 'https://example.com/artwork1'}],
                                  'release_date': '2020/11/12'},
                        'external_urls': {'spotify': 'https://example.com/direct1'},
                        'uri': 'spotify:track:123456',
                        'id': '123456'
                    },
                    {
                        'name': 'Track 2',
                        'artists': [{'name': 'Artist 2'}],
                        'preview_url': 'https://example.com/track2',
                        'album': {'images': [{'url': 'https://example.com/artwork2'}],
                                  'release_date': '2020/11/12'},
                        'external_urls': {'spotify': 'https://example.com/direct2'},
                        'uri': 'spotify:track:789012',
                        'id': '789012'
                    }
                ]
            }
        }
        mock_get.return_value.json.return_value = mock_response
        # Call the fetch_tracks function
        tracks = fetch_tracks('rise till we fall')
        # Assert the expected results
        self.assertEqual(len(tracks), 2)
        self.assertEqual(tracks[0]['Track Name'], 'Track 1')
        self.assertEqual(tracks[0]['Artist(s) Name'], 'Artist 1')
        self.assertEqual(tracks[0]['Preview URL or Track URI'], 'https://example.com/track1')
        self.assertEqual(tracks[0]['Album Artwork'], 'https://example.com/artwork1')
        self.assertEqual(tracks[0]['Direct Link'], 'https://open.spotify.com/track/' + mock_response['tracks']['items'][0]['id'])
        self.assertEqual(tracks[0]['Track URI'], 'spotify:track:123456')
        self.assertEqual(tracks[1]['Track Name'], 'Track 2')
        self.assertEqual(tracks[1]['Artist(s) Name'], 'Artist 2')
        self.assertEqual(tracks[1]['Preview URL or Track URI'], 'https://example.com/track2')
        self.assertEqual(tracks[1]['Album Artwork'], 'https://example.com/artwork2')
        self.assertEqual(tracks[1]['Direct Link'], 'https://open.spotify.com/track/' + mock_response['tracks']['items'][1]['id'])
        self.assertEqual(tracks[1]['Track URI'], 'spotify:track:789012')
        mock_get.return_value.json.return_value = mock_response

if __name__ == '__main__':
    unittest.main()
    
