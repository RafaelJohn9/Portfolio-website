#!/usr/bin/python3
"""
Tests module tests the storage module
"""
from models.user import User
from models.recommendation import Recommendation
from models import storage
import unittest
from unittest import TestCase
from sqlalchemy.exc import IntegrityError

class TestStorage(TestCase):
    """
    tests the storage module
    """
    def setUp(self):
        """
        Set up for the test
        """
        self.new_user = User(username="testuser", password="testpassword", email="testuser@example.com")
        storage.new(self.new_user)
        storage.save()

    def tearDown(self):
        """
        Tear down for the test
        """
        storage.delete(self.new_user)
        storage.save()
        
    def test_new(self):
        """
        Test the new method of the DBStorage class
        """
        # Test adding a new user
        new_user = User(username="user", password="password", email="user@example.com")
        storage.new(new_user)
        storage.save()
        self.assertIsNotNone(storage.get("users",userId=new_user.userId))

        # Test adding an existing user
        with self.assertRaises(IntegrityError):
            existing_user = User(username="user", password="password", email="user@example.com")
            storage.new(existing_user)
            storage.save()

        # Test adding a user with the same email
        with self.assertRaises(IntegrityError):
            same_email_user = User(username="differentuser", password="differentpassword", email="user@example.com")
            storage.new(same_email_user)
            storage.save()

        # Test adding a user with the same username
        with self.assertRaises(IntegrityError):
            same_username_user = User(username="user", password="differentpassword", email="differentuser@example.com")
            storage.new(same_username_user)
            storage.save()

        # Test adding a user with the same password
        same_password_user = User(username="differentuser", password="password", email="differentuser@example.com")
        storage.new(same_password_user)
        storage.save()
        self.assertIsNotNone(storage.get("users", userId=same_password_user.userId))

        # Test adding a new movie, music, book
        # Assuming item_type attribute in Recommendation class can take values "movie", "music", "book"
        new_movie = Recommendation(item_type="movie", name="newmovie", item_id=0, user_id=new_user.userId)
        new_music = Recommendation(item_type="music", name="newmusic", item_id=1, user_id=new_user.userId)
        new_book = Recommendation(item_type="book", name="newbook", item_id=2, user_id=new_user.userId)
        storage.new(new_movie)
        storage.new(new_music)
        storage.new(new_book)
        storage.save()
        self.assertIsNotNone(storage.get("recommendations", item_id=new_movie.item_id))
        self.assertIsNotNone(storage.get("recommendations", item_id=new_music.item_id))
        self.assertIsNotNone(storage.get("recommendations", item_id=new_book.item_id))

        # Test adding the same movie, music, book
        with self.assertRaises(IntegrityError):
            same_movie = Recommendation(item_type="movie", name="newmovie", item_id=0, user_id=new_user.userId)
            same_music = Recommendation(item_type="music", name="newmusic", item_id=1, user_id=new_user.userId)
            same_book = Recommendation(item_type="book", name="newbook", item_id=2, user_id=new_user.userId)
            storage.new(same_movie)
            storage.new(same_music)
            storage.new(same_book)
            storage.save()

        # Clean up
        storage.delete(new_movie)
        storage.delete(new_music)
        storage.delete(new_book)
        
        storage.delete(same_password_user)
        storage.delete(new_user)
        
        storage.save()
        
    def test_all(self):
        # Test the all method of the DBStorage class
        table_name_0 = "users"  # Replace with the actual table name
        table_name_1 = "recommendations"  # Replace with the actual table name
        result_0 = storage.all(table_name_0)
        result_1 = storage.all(table_name_1)
        self.assertIsNotNone(result_0)  # Assert that the result is not None
        self.assertIsNotNone(result_1)  # Assert that the result is not None
        
    def test_get(self):
        """
        Test the get method of the DBStorage class
        """
        # Create a user
        user = User(username="Exampleuser", password="password", email="userexample@example.com")
        storage.new(user)
        storage.save()

        # Test retrieving the user by userId
        retrieved_user = storage.get("users", userId=user.userId)
        self.assertEqual(retrieved_user.userId, user.userId)
        
        # Test retrieving the user by username
        retrieved_user = storage.get("users", username=user.username)
        self.assertEqual(retrieved_user.userId, user.userId)
        
        # Test retrieving the user by email
        retrieved_user = storage.get("users", email=user.email)
        self.assertEqual(retrieved_user.userId, user.userId)
        
        storage.delete(user)
    
    def test_all_with(self):
        """
        Test the all_with method of the DBStorage class
        """
        # Create a user
        user = User(username="Exampleuser", password="password", email="userexample@example.com")
        storage.new(user)
        storage.save()

        # Create a book and a movie recommendation for the user
        book = Recommendation(item_type="book", name="newbook", item_id=0, user_id=user.userId)
        movie = Recommendation(item_type="movie", name="newmovie", item_id=1, user_id=user.userId)
        storage.new(book)
        storage.new(movie)
        storage.save()

        # Use all_with to get the items from recommendations table
        recommendations = storage.all_with("recommendations", user_id=user.userId)

        # Check the length and assert that it is two
        self.assertEqual(len(recommendations), 2)

        # Clean up
        storage.delete(book)
        storage.delete(movie)
        storage.delete(user)
        storage.save()
                
    def test_count(self):
        """
        Test the count method of the DBStorage class
        """
        # Create a user
        user = User(username="Exampleuser", password="password", email="userexample@example.com")
        storage.new(user)
        storage.save()
        # Test count method
        count = storage.count("users")
        self.assertIsInstance(count, int)
        # Clean up
        storage.delete(user)
        storage.save()
        
    def test_update(self):
        """
        Test the update method of the DBStorage class
        """
        # Create a user
        user = User(username="Exampleuser", password="password", email="userexample@example.com")
        storage.new(user)
        storage.save()

        # Update the user's username
        new_username = "NewUsername"
        storage.update(user, username=new_username)
        storage.save()

        # Get the updated user from the database
        updated_user = storage.get("users", username=new_username)

        # Check if the username has been updated
        self.assertEqual(updated_user.username, new_username)

        # Clean up
        storage.delete(updated_user)
        storage.save()
