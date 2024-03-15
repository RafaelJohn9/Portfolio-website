"""Create a unique DBStorage instance for your application"""
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from models.engine.storage import DBStorage
storage = DBStorage()