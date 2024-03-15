"""_summary_
    it is a class that is used to store data in a database
    and perform other basic operations
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
import os
from models.engine.user_orm import UserORM

class DBStorage:
    """
    A class that is used to store user data in a database
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
        
    def new(self, user):
        """
        a method that adds a new user to the database
        """
        self.__session.add(user)
        self.__session.commit()

    def delete(self, user):
        """
        a method that deletes a user from the database
        """
        self.__session.delete(user)

    def update(self, user, **kwargs):
        """
        a method that updates a user in the database
        """
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        self.__session.commit()

    def save(self):
        """
        a method that saves changes made to the database
        """
        self.__session.commit()

    def get(self, **kwargs):
        """
        a method that returns a user from the database
        """
        return self.__session.query(UserORM).filter_by(**kwargs).first()
    
    def all(self, **kwargs):
        """
        a method that returns all users with a specific attr from the database
        """
        return self.__session.query(UserORM).filter_by(**kwargs).all()

    def count(self):
        """
        returns count of all the users in the database
        """
        return self.__session.query(UserORM).count()

    def close(self):
        self.__session.close()