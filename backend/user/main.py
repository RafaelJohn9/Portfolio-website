#!/usr/bin/python3

from models.user import User
from models import storage

# Create an instance of User
name = "Joe Doe"
email = "mail@example.com"
password = "password"


user = User(name, email, password)
print(user)
userORM = user.toORM()
storage.new(userORM)
storage.close()
