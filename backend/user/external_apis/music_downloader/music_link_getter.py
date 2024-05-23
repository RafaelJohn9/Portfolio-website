#!/usr/bin/env python3
"""Module to get the first music video link for a given query."""
import logging
import os
from googleapiclient.discovery import build

# Set up the YouTube API credentials
api_key = os.getenv("YOUTUBE_API_KEY")
youtube = build('youtube', 'v3', developerKey=api_key)

def get_music_link(query):
    """uses the YouTube API to get the first music video link for a given query."""
    # Call the YouTube API to search for videos matching the query
    # pylint: disable=no-member
    search_response = youtube.search().list(
        q=query,
        part='id',
        maxResults=1,
        type='video'
    ).execute()

    # Extract the first video ID from the search results
    video_id = search_response['items'][0]['id']['videoId']

    # Construct the YouTube video link using the video ID
    music_link = f'https://www.youtube.com/watch?v={video_id}'

    # Log any errors to music_link_getter.log
    logging.basicConfig(filename='./music_link_getter.log', level=logging.ERROR)
    try:
        logging.info("Music link for query '%s': %s", query, music_link)
    # pylint: disable=broad-except
    except Exception as e:
        logging.error("Error logging music link: %s", e)

    return music_link

if __name__=="__main__":
    search_query = input("Enter the name of the song you want to download: ")
    music = get_music_link(search_query)
    print("Music link:", music)
