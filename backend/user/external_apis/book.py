#!/usr/bin/env python3
import os
import requests


def fetch_books(bookname, **kwargs):
    api_key = os.getenv('BOOK_API')
    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": bookname,
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    books = []
    for item in data['items']:
        book = {
            "item_type": "book",
            "title": item['volumeInfo'].get('title'),
            "authors": item['volumeInfo'].get('authors'),
            "pages": item['volumeInfo'].get('pageCount'),
            "release_date": item['volumeInfo'].get('publishedDate'),
            "rating": item['volumeInfo'].get('averageRating'),
            "genre": item['volumeInfo'].get('categories'),
            "publisher": item['volumeInfo'].get('publisher'),
            "cover_images": item['volumeInfo'].get('imageLinks')
        }
        books.append(book)

    if not kwargs:
        return books

    precise_books = []
    for book in books:
        match = all(book.get(key) == value for key, value in kwargs.items())
        if match:
            precise_books.append(book)
    return precise_books


if __name__ == "__main__":
    bookname = "harry potter"
    books = fetch_books(bookname, release_date="2006-01")
    for book in books:
        print(book)
