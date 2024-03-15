"""
This module is responsible for creating the UserORM class, which represents a User object in the database.
"""

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

class UserORM(Base):
    """
    Represents a User object in the database.
    """

    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(120))

    def __init__(self, user_model):
        """
        Initializes a User object with the provided user model.
        """
        self.username = user_model.username
        self.email = user_model.email
        self.password = user_model.password
                    
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
        return f"UserORM: {self.username}"
    