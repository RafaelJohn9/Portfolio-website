#!/usr/bin/python3

from models.user import User
from models.recommendation import Recommendation
from models import storage

# Create an instance of User
name = "Holna D"
email = "somethin@example.com"
password = "password"


user = User(username=name, email=email, password=password)
recommendation = Recommendation(user_id=user.userId, item_type="music", name="The Matrix")
print(user)
print(recommendation)
storage.new(user)
storage.new(recommendation)
storage.close()
