from user import User

def create_user(username, db):
    u = User(username)
    res = db.users.insert_one(vars(u))
    u.id = res.inserted_id

