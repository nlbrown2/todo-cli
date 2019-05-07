from todo import TodoItem, kItemNameKey
from utility import kItemKey, read_word, read_line
from collections import deque


def create(curUser, db, inputs):
    name = read_line(inputs, "What is the name of the item? ")
    item = TodoItem(name, curUser["_id"]) # link the item to the user
    res = db.users.update_one(
            curUser,
            {
                "$addToSet": { kItemKey: vars(item) }
            })
    if(res.acknowledged is not True or res.modified_count is not 1):
        print("error!")
    return deque() #clears out input always

def read(curUser, db, inputs):
    for item in curUser[kItemKey]:
        print(item[kItemNameKey])
    return inputs

def delete_all(curUser, db, inputs):
    confirm = read_word(inputs, "are you sure you want to delete all? ")
    if confirm == 'yes' or confirm == 'y':
        res = db.users.update_one(
                curUser,
                {
                    "$set": { kItemKey: [] }
                })
        if(res.acknowledged is not True or res.modified_count > 1):
            print("error!")
            return deque()
    else:
        print("aborting!")
        return deque()
    return inputs

def delete(curUser, db, inputs):
    item_name = read_line(inputs, "what do you want to delete? ")
    res = db.users.update_one(
            curUser,
            {
                "$pull": { kItemKey: { kItemNameKey: item_name } }
            })
    if(res.acknowledged is not True or res.modified_count is not 1):
        print("error!")
        return deque()
    return inputs

def edit(curUser, db, inputs):
    old_name = read_line(inputs, "what is the old name? ")
    new_name = read_line(inputs, "what is the new name? ") # create a new item object
    res = db.users.update_one(
            curUser,
            { "$set": { kItemKey + ".$[element]." + kItemNameKey: new_name } },
            array_filters= [ { "element." + kItemNameKey: { "$eq": old_name } } ])
    if(res.acknowledged is not True or res.modified_count is not 1):
        print("error!")
    return deque() #clears out input always
