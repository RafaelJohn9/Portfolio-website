#!/usr/bin/env python3
"""This is the main file that will contain the main function used to run the program"""
import logging
from external_apis.music_downloader.music_link_getter import get_music_link
from external_apis.music_downloader.music_download_link import music_download_link

def music_downloader(query):
    """ uses the get_music_link and download_music 
    functions to get the download link for a given query."""
    if query == "" or query is None:
        raise ValueError("Invalid query")
    try:
        music_link = get_music_link(query)
        download = music_download_link(music_link)
        return download
    # pylint: disable=broad-except
    except Exception as e:
        logging.basicConfig(filename='main.log', level=logging.ERROR)
        logging.error(str(e))

if __name__=="__main__":
    search_query = input("Enter the name of the song you want to download: ")
    music = music_downloader(search_query)
    print("Download link:", music)
