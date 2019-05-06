from todo import TodoItem, kItemNameKey
from user import kItemKey


def create(curUser, db):
    name = input("what is the name of the item? ")
    item = TodoItem(name, curUser["_id"]) # link the item to the user
    res = db.users.update_one(
            curUser,
            {
                "$addToSet": { kItemKey: vars(item) }
            })
    if(res.acknowledged is not True or res.modified_count is not 1):
        print("error!")

def read(curUser, db):
    for item in curUser[kItemKey]:
        print(item[kItemNameKey])

def delete_all(curUser, db):
    confirm = input("are you sure you want to delete all? ")
    if confirm == 'yes' or confirm == 'y':
        res = db.users.update_one(
                curUser,
                {
                    "$set": { kItemKey: [] }
                })
        if(res.acknowledged is not True or res.modified_count is not 1):
            print("error!")
    else:
        print("aborting!")

def delete(curUser, db):
    item_name = input("what do you want to delete? ")
    res = db.users.update_one(
            curUser,
            {
                "$pull": { kItemKey: { kItemNameKey: item_name } }
            })
    if(res.acknowledged is not True or res.modified_count is not 1):
        print("error!")
