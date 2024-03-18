#!/usr/bin/python3
"""
This module is responsible for creating the UserORM class, which represents a User object in the database.
"""
from models import Base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import os
import uuid
from werkzeug.security import generate_password_hash
from . import recommendation

class User(Base):
    """
    Represents a User object in the database.
    """

    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(String(150), index=True, unique=True)
    username = Column(String(50), unique=True, nullable=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=True)
    
    recommendations = relationship("Recommendation", back_populates="user")
    def __init__(self, email, username="", password="", is_active=True):
        """
        Initializes a User object with the provided user model.
        """
        self.userId = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.is_active = is_active
                    
        database_url = URL.create(
            drivername="mysql+pymysql",
            username=os.getenv('DB_USER', 'user'),
            password=os.getenv('DB_PASSWORD', 'password'),
            host=os.getenv('DB_HOST', 'localhost'),
            database=os.getenv('DB_NAME', 'PortfolioDB')
        )
        self.__engine = create_engine(database_url)
        Base.metadata.create_all(self.__engine)
    
    def get_id(self):
        """
        Returns the user's id.
        """
        return self.userId
    
    def is_authenticated(self):
        """
        Returns True if the user is authenticated, False otherwise.
        """
        return True
    
    def is_active(self):
        """
        Returns True if the user is active, False otherwise.
        """
        return self.is_active
    
    def is_anonymous(self):
        """
        Returns True if the user is anonymous, False otherwise.
        """
        return False
    
    def to_dict(self):
        """
        Converts the User object to a dictionary.
        """
        return {
            'userId': self.userId,
            'userId': self.userId,
            'username': self.username,
            'email': self.email,
        }

    def __repr__(self):
        return f"<UserORM(username={self.username}, email={self.email})>"
    
    def __str__(self):
        return f"User: {self.username}"
    