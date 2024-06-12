#!/usr/bin/env python3
"""
uses multiple sites to fetch  the books needed to be downloaded
"""
from external_apis.book_downloader import library_genesis
from external_apis.book_downloader import pdfdrive
from external_apis.book_downloader import gutendex

def get_book_download_link(title: str) -> str:
    """
    The function used to get the download link 
    of the book from the library genesis, pdfdrive and gutendex
    """
    # Get the download link from library genesis
    download_link = library_genesis.get_download_url(title)
    if download_link is not None:
        return download_link

    # Get the download link from pdfdrive
    download_link = pdfdrive.get_download_url(title)
    if download_link is not None:
        return download_link

    # Get the download link from gutendex
    download_link = gutendex.get_download_url(title)
    if download_link is not None:
        return download_link

    return None


if __name__ == '__main__':
    # Example usage
    BOOK_TITLE = input("Enter the book title: ")
    book_download_link = get_book_download_link(BOOK_TITLE)
    print(book_download_link)
