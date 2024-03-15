#!/usr/bin/env python3
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from models.engine.user_orm import UserORM

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self._id = uuid.uuid4()
        self._password = generate_password_hash(password)

    @property
    def id(self):
        return self._id

    @property
    def password(self):
        return self._password
    
    def toORM(self):
        return UserORM(self)
    
    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}', id='{self._id}')"

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}, ID: {self._id}"
    