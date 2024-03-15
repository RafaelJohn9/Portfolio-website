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
    username = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(120))
    
    recommendations = relationship("Recommendation", back_populates="user")
    def __init__(self, username, password, email):
        """
        Initializes a User object with the provided user model.
        """
        self.userId = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
                    
        database_url = URL.create(
            drivername="mysql+pymysql",
            username=os.getenv('DB_USER', 'user'),
            password=os.getenv('DB_PASSWORD', 'password'),
            host=os.getenv('DB_HOST', 'localhost'),
            database=os.getenv('DB_NAME', 'PortfolioDB')
        )
        self.__engine = create_engine(database_url)
        Base.metadata.create_all(self.__engine)
        
        
    def __repr__(self):
        return f"<UserORM(username={self.username}, email={self.email})>"
    
    def __str__(self):
        return f"User: {self.username}"
    