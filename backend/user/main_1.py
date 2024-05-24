#!/usr/bin/python3

from external_apis.music_downloader.main import music_downloader

if __name__=="__main__":
    search_query = input("Enter the name of the song you want to download: ")
    music = music_downloader(search_query)
    print("Download link:", music)