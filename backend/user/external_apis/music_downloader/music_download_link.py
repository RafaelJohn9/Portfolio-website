#!/usr/bin/python3
"""Downloads the audio of a YouTube video given its URL."""
import logging
from pytube import YouTube

def music_download_link(url):
    """downloads the audio of a YouTube video given its URL."""
    if url == "" or url is None:
        raise ValueError("Invalid URL")
    try:
        # Create a YouTube object with the given URL
        video = YouTube(url)

        # Get the audio stream with the highest bitrate
        audio_stream = video.streams.get_audio_only()

        # Download the audio stream
        audio_stream.download()
        # Return the path of the downloaded audio file
        return audio_stream.default_filename
    # pylint: disable=broad-except
    except Exception as e:
        # Configure logging
        logging.basicConfig(filename='./music_download_link.log',
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

        # Log the error
        logging.error(str(e))

if __name__=="__main__":
    download_url = input("Enter the URL of the YouTube video: ")
    music_download_link(download_url)
