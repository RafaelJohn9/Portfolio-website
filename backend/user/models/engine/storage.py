#!/usr/bin/python3
"""
    it is a class that is used to store data in a database
    and perform other basic operations
"""
from sqlalchemy import Table  # Import the Table class
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy.exc import IntegrityError
import os
from models import Base
from models.user import User
from models.recommendation import Recommendation

class DBStorage:
    """
    A class that is used to store items data in a database
    """
    def __init__(self):
        """
        a constructor that initializes the database connection
        """
        database_url = URL.create(
            drivername="mysql+pymysql",
            username=os.getenv('DB_USER', 'user'),
            password=os.getenv('DB_PASSWORD', 'password'),
            host=os.getenv('DB_HOST', 'localhost'),
            database=os.getenv('DB_NAME', 'PortfolioDB')
        )
        self.__engine = create_engine(database_url)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
    
    def all(self, table_name):
        """
        a method that returns all items from the database
        """
        table = Table(table_name, Base.metadata, autoload_with=self.__session.bind)
        return self.__session.query(table).all()
    
    def new(self, item):
        """
        a method that adds a new item to the database
        """
        if isinstance(item, User):
            existing_user = self.__session.query(User).filter(
                (User.email == item.email) | (User.username == item.username)
            ).first()

            if existing_user:
                if existing_user.email == item.email:
                    raise IntegrityError("User with this email already exists", None, None)
                elif existing_user.username == item.username:
                    raise IntegrityError("User with this username already exists", None, None)
        elif isinstance(item, Recommendation):
            existing_user = self.__session.query(User).filter(User.userId == item.user_id).first()
            if not existing_user:
                raise IntegrityError("User with this userId does not exist", None, None)
            existing_recommendation = self.__session.query(Recommendation).filter(
                (Recommendation.name == item.name) & (Recommendation.item_type == item.item_type)
            ).first()

            if existing_recommendation:
                raise IntegrityError("Recommendation with this name and type already exists", None, None)

        self.__session.add(item)
        try:
            self.__session.commit()
        except IntegrityError as e:
            self.__session.rollback()
            raise e
        
    def delete(self, item):
        """
        a method that deletes a item from the database
        """
        self.__session.delete(item)

    def update(self, item, **kwargs):
        """
        a method that updates a item in the database
        """
        for key, value in kwargs.items():
            if hasattr(item, key):
                setattr(item, key, value)
        self.__session.commit()

    def save(self):
        """
        a method that saves changes made to the database
        """
        self.__session.commit()

    def get(self, table_name, **kwargs):
        """
        a method that returns a item from the database
        """
        table = Table(table_name, Base.metadata, autoload_with=self.__session.bind)
        return self.__session.query(table).filter_by(**kwargs).first()
    
    def all_with(self, table_name, **kwargs):
        """
        a method that returns all items with a specific attr from the database
        """
        table = Table(table_name, Base.metadata, autoload_with=self.__session.bind)
        return self.__session.query(table).filter_by(**kwargs).all()


    def count(self, table_name):
        """
        returns count of all the items in the database
        """
        table = Table(table_name, Base.metadata, autoload_with=self.__session.bind)
        return self.__session.query(table).count()

    def close(self):
        """Closes the session
        """
        self.__session.close()