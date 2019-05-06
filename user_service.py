from user import User
from collections import deque

def create_user(username, db, inputs):
    u = User(username)
    res = db.users.insert_one(vars(u))
    if(res.acknowledged is not True):
        return deque()
    u.id = res.inserted_id
    return inputs

def get_user(username, db):
    return db.users.find_one({"name": username})
