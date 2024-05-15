#!/usr/bin/python3
"""
An example of an existing user
"""

from models.user import User
from models.recommendation import Recommendation
from models.BookStorage import Book
from models import storage

# Create an instance of User
name = "Holna D"
email = "somethin@example.com"
password = "password"


user = User(username=name, email=email, password=password)
recommendation = Recommendation(user_id=user.userId, item_type="music", name="The Matrix")
book = Book(title="The Matrix", author="The Wachowskis", date="1999-03-31", pages=100, publisher="Warner Bros", size_mb=100, DownloadLink="https://www.google.com")
print(user)
print(recommendation)
print(book)
storage.new(user)
storage.new(recommendation)
storage.new(book)
storage.close()
