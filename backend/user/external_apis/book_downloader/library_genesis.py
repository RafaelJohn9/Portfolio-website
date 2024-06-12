#!/usr/bin/env python3
"""
this component scraps libgen.rs for the download link of the book
"""
import requests
from bs4 import BeautifulSoup


def get_download_url(query):
    """
    function scrapper to search for the book on libgen.rs
    """
    # Construct the search URL
    search_url = (
        f"https://libgen.is/search.php?req={query}&lg_topic=libgen&open=0"
        f"&view=simple&res=25&phrase=1&column=def"
    )

    # Send a GET request to the search URL
    response = requests.get(search_url, timeout=10)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, 'html.parser')


    # Find the link with the title "Libgen & IPFS & Tor"
    link = soup.find('a', title='Libgen & IPFS & Tor')

    if link:
        # Extract the download link
        download_link = link['href']
        # Request the page using the download link
        response = requests.get(download_link, timeout=10)
        # Parse the HTML content of the response
        soup = BeautifulSoup(response.content, 'html.parser')
        # Continue with the rest of the code
        # Find the link with the value "GET"
        get_link = soup.find('a', string='GET')

        if get_link:
            # Extract the href link
            get_link_href = get_link['href']
            return get_link_href
        else:
            return
    else:
        return


if __name__ == '__main__':
    book_query = input("Enter the book title: ")
    book_download_link = get_download_url(book_query)
    if book_download_link:
        print(f"Download link: {book_download_link}")
    else:
        print("Book not found")
