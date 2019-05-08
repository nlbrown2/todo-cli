"""
service for interacting with users
"""
from collections import deque
from user import User

def create_user(username, database, inputs):
    """ creates a user with username and inserts into DB """
    user = User(username)
    res = database.users.insert_one(vars(user))
    if res.acknowledged is not True:
        return deque()
    user.id = res.inserted_id
    return inputs

def get_user(username, database):
    """ gets a user with name username from DB """
    return database.users.find_one({"name": username})
