#!/usr/bin/python3
"""Provides a direct link to download the audio of a YouTube video given its URL."""
import logging
import yt_dlp

def get_audio_download_link(url):
    """Gets the direct download link of the audio of a YouTube video given its URL."""
    if not url:
        raise ValueError("Invalid URL")
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'extract_flat': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            audio_url = info_dict['url']
            return audio_url
    except Exception as e:
        # Configure logging
        logging.basicConfig(filename='./music_download_link.log',
                            level=logging.ERROR,
                            format='%(asctime)s - %(levelname)s - %(message)s')

        # Log the error
        logging.error(str(e))
        return None

if __name__ == "__main__":
    download_url = input("Enter the URL of the YouTube video: ")
    audio_link = get_audio_download_link(download_url)
    if audio_link:
        print(f"Direct download link for audio: {audio_link}")
    else:
        print("Failed to get the download link for the audio.")
