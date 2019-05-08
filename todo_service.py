"""
services for interacting with todo items
"""
from collections import deque
from todo import TodoItem, ITEM_NAME_KEY
from utility import ITEM_KEY, read_word, read_line


def create(cur_user, database, inputs):
    """ creates a new todo item for the current user """
    name = read_line(inputs, "What is the name of the item? ")
    print("inserting with name: " + name)
    item = TodoItem(name, cur_user["_id"]) # link the item to the user
    res = database.users.update_one(
        cur_user,
        {
            "$addToSet": {ITEM_KEY: vars(item)}
        })
    if(res.acknowledged is not True or res.modified_count != 1):
        print("error!")
    return deque() #clears out input always

def read(cur_user, _, inputs):
    """ prints all todo items in alphabetical order """
    for item in sorted(cur_user[ITEM_KEY], key=lambda i: i[ITEM_NAME_KEY]):
        print(item[ITEM_NAME_KEY])
    return inputs

def delete_all(cur_user, database, inputs):
    """ removes all todo items from current user """
    confirm = read_word(inputs, "are you sure you want to delete all? ")
    if confirm in ('yes', 'y'):
        res = database.users.update_one(
            cur_user,
            {
                "$set": {ITEM_KEY: []}
            })
        if(res.acknowledged is not True or res.modified_count > 1):
            print("error!")
            return deque()
    else:
        print("aborting!")
        return deque()
    return inputs

def delete(cur_user, database, inputs):
    """ deletes one item from the current user """
    item_name = read_line(inputs, "what do you want to delete? ")
    res = database.users.update_one(
        cur_user,
        {
            "$pull": {ITEM_KEY: {ITEM_NAME_KEY: item_name}}
        })
    if(res.acknowledged is not True or res.modified_count != 1):
        print("error!")
        return deque()
    return inputs

def edit(cur_user, database, inputs):
    """ changes the name of one users input """
    old_name = read_line(inputs, "what is the old name? ")
    new_name = read_line(inputs, "what is the new name? ") # create a new item object
    res = database.users.update_one(
        cur_user,
        {"$set": {ITEM_KEY + ".$[element]." + ITEM_NAME_KEY: new_name}},
        array_filters=[{"element." + ITEM_NAME_KEY: {"$eq": old_name}}])
    if(res.acknowledged is not True or res.modified_count != 1):
        print("error!")
    return deque() #clears out input always

def all_items(cur_user, database, inputs):
    """ if current user is admin, will print out all todo items """
    if cur_user["admin"] is not True:
        print("User is not admin! this cannot be done")
        return deque()
    for doc in database.users.find({}, {ITEM_KEY + "." + ITEM_NAME_KEY : 1, "_id": 0}):
        for dic in doc[ITEM_KEY]:
            name = dic[ITEM_NAME_KEY]
            if name.strip():
                print(name)
    return inputs
