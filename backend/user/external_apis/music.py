#!/usr/bin/env python3

import os
import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session


def fetch_tracks(track_name, **kwargs):
    client_id = os.environ['SPOTIFY_CLIENT_ID']
    client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
    auth = HTTPBasicAuth(
                         client_id,
                         client_secret
                         )
    response = requests.post(
                              'https://accounts.spotify.com/api/token',
                              auth=auth,
                              data={'grant_type': 'client_credentials'}
                              )
    response.raise_for_status()
    access_token = response.json()['access_token']

    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'q': track_name, 'type': 'track'}
    response = requests.get(
                            'https://api.spotify.com/v1/search',
                            headers=headers,
                            params=params)
    response.raise_for_status()

    tracks = []
    for item in response.json()['tracks']['items']:
        track = {
            'item_type': 'music',
            'Track Name': item['name'],
            'Artist(s) Name': ', '.join(artist['name'] for artist in item['artists']),
            'Preview URL or Track URI': item['preview_url'] or item['uri'],
            'Track URI': item['uri'],
            'Album Artwork': item['album']['images'][0]['url'] if item['album']['images'] else None,
            'Direct Link': f"https://open.spotify.com/track/{item['id']}",
            'release_date': item['album']['release_date']
        }
        tracks.append(track)
    if not kwargs:
        return tracks
    precise_tracks = []
    for track in tracks:
        if all(track.get(key) == value for key, value in kwargs.items()):
            precise_tracks.append(track)
    return precise_tracks


if __name__ == "__main__":
    track_name = "Never gonna give up"
    tracks = fetch_tracks(track_name, release_date="2020-07-03")
    for track in tracks:
        print(f"Track Name: {track['Track Name']}")
        print(f"Artist(s) Name: {track['Artist(s) Name']}")
        print(f"Preview URL or Track URI: {track['Preview URL or Track URI']}")
        print(f"Album Artwork: {track['Album Artwork']}")
        print(f"Direct Link: {track['Direct Link']}")
        print(f"Track URI: {track['Track URI']}")
        print(f"release_date: {track['release_date']}")
        print("\n")
