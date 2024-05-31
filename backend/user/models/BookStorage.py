#!/usr/bin/python3
"""
creates a storage table for books in the db
"""
import uuid
from sqlalchemy import Column, String, Date, Integer
from sqlalchemy.ext.declarative import declarative_base
from models import Base

class Book(Base):
    """
    Book class to represent a book in the database
    """
    __tablename__ = 'books'

    id = Column(String(75), primary_key=True, default=str(uuid.uuid4()))
    title = Column(String(200), nullable=False)
    author = Column(String(50))
    date = Column(Date)
    pages = Column(Integer)
    publisher = Column(String(50))
    DownloadLink = Column(String(100))
    size_mb = Column(Integer)