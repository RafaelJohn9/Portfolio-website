#!/usr/bin/python3
"""
It is used to query gutendex, Project gutenberg's API to get the download link of a book.
after given a title
"""
import requests

def get_download_url(title):
    """
    the function used to get the downlod link of the book from the gutendex API
    """
    # Make a GET request to the Gutendex API
    response = requests.get(f"https://gutendex.com/books/?search={title}", timeout=10)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if any books were found
        if data["count"] > 0:
            # Get the first book from the results
            book = data["results"][0]

            # Get the download link for the book
            download_link = book["formats"]["application/epub+zip"]

            return download_link
        else:
            return None
    else:
        return None


if __name__ == '__main__':
    # Example usage
    BOOK_TITLE = input("Enter the book title: ")
    book_download_link = get_download_url(BOOK_TITLE)
    print(book_download_link)
