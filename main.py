"""
driver for the whole deal
"""

from collections import deque
from pymongo import MongoClient
from user import User
from todo_service import create as create_item, read, delete_all, delete, edit, all_items
from user_service import create_user, get_user
from utility import read_word

# args not needed, but used for the same interface with the rest
def help_fn(cur_user, _, inputs):
    """
    prints all available functions for the current user
    """
    print("The following operations are supported: ")
    for operation in COMMANDS:
        print(operation)
        if operation in DESCRIPTIONS:
            print('\t' + DESCRIPTIONS[operation])
    if cur_user["admin"] is not True:
        return inputs
    for operation in ADMINCOMMANDS:
        print(operation)
        if operation in DESCRIPTIONS:
            print('\t' + DESCRIPTIONS[operation])
    return inputs

COMMANDS = {
        "create": create_item,
        "read": read,
        "delete": delete,
        "clear": delete_all,
        "edit": edit,
        "help": help_fn
        }

ADMINCOMMANDS = {
        "all": all_items
        }

DESCRIPTIONS = {
        "create": "Create a new todo item",
        "read": "List all of your todo items",
        "delete": "Delete a todo item",
        "clear": "Delete all todo items",
        "edit": "change the name of an existing todo item",
        "help": "View available commands"
        }

def main():
    """ main fn """
    inputs = deque()
    while True:
        username = read_word(inputs, "who are you? ")
        user = get_user(username, DB)
        if user:
            break
        make_new = read_word(inputs, "not a known user, would you like to make a new one? ")
        if make_new in ('yes', 'y'):
            create_user(username, DB, make_new)
            user = get_user(username, DB)
    print('For help, just type "help"')
    while True:
        command = read_word(inputs, "what do you want to do today? ")
        if command == "quit":
            break
        elif command in COMMANDS:
            inputs = COMMANDS[command](user, DB, inputs) #pass along rest of the inputs
        elif command in ADMINCOMMANDS and user["admin"] is True:
            inputs = ADMINCOMMANDS[command](user, DB, inputs) #pass along rest of the inputs
        else:
            print("error! command " + command + " not recognized!")
        user = get_user(username, DB)


def seed_db(database):
    """ seeds the database """
    user = User("Admin")
    user.admin = True
    database.users.insert_one(vars(user))

if __name__ == "__main__":
    CLIENT = MongoClient(host="localhost", port=27017)
    DB = CLIENT.database
    # try:
    seed_db(DB)
    main()
    # except Exception as exception:
    #     print(exception)
