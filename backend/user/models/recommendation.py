#!/usr/bin/python3
"""
The Recommendation model represents a recommendation object in the database,
storing recommendations for books, music, and movies with
references to the user who made the recommendation.
"""
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from  models import Base
import os
from . import user

class Recommendation(Base):
    """
    Represents a recommendation object in the database.
    """
    __tablename__ = 'recommendations'
    __table_args__ = (UniqueConstraint('item_type', 'name', name='unique_item_per_type'),)

    recommendation_id = Column(Integer, primary_key=True, autoincrement=True)
    item_id = Column(Integer)
    item_type = Column(Enum('book', 'music', 'movie', name='item_types'))
    name = Column(String(120))
    user_id = Column(String(120), ForeignKey('users.userId'))

    user = relationship("User", back_populates="recommendations")
    def __init__(self, user_id, item_id, item_type, name):
        """
        Initializes a Recommendation object with the provided user model.
        """
        self.user_id = user_id
        self.item_id = item_id
        self.item_type = item_type
        self.name = name
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
        """
        Returns a string representation of the Recommendation object.
        """
        return (f"<Recommendation(recommendation_id={self.recommendation_id}, "
            f"user_id={self.user_id}, item_id={self.item_id}, "
            f"item_type={self.item_type}, name={self.name})>")

    def __str__(self):
        """
        Returns a human-readable string representation of the Recommendation object.
        """
        return (f"Recommendation: {self.name} of type {self.item_type} "
            f"recommended by user {self.user_id}")