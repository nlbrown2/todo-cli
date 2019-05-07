from todo import TodoItem, test as test_item
from user import User, test as test_user
from todo_service import create as create_item, read, delete_all, delete, edit
from user_service import create_user, get_user
from utility import read_word
from pymongo import MongoClient
from collections import deque

# args not needed, but used for the same interface with the rest
def help_fn(curUser, db, inputs):
    print("The following operations are supported: ")
    for op in commands.keys():
        print(op)
        if op in descriptions:
            print('\t' + descriptions[op])
    return inputs

commands = {
        "create": create_item,
        "read": read,
        "delete": delete,
        "clear": delete_all,
        "edit": edit,
        "help": help_fn
        }

descriptions = {
        "create": "Create a new todo item",
        "read": "List all of your todo items",
        "delete": "Delete a todo item",
        "clear": "Delete all todo items",
        "edit": "change the name of an existing todo item",
        "help": "View available commands"
        }

operations = '\n'.join(list(commands.keys()))

def main():
    inputs = deque()
    username = read_word(inputs, "who are you? ")
    user = get_user(username, db)
    while(not user):
        make_new = read_word(inputs, "not a known user, would you like to make a new one? ")
        if make_new == 'yes' or make_new == 'y':
            create_user(username, db, make_new)
            user = get_user(username, db)
    print('For help, just type "help"')
    while(True):
        command = read_word(inputs, "what do you want to do today? ")
        if command == "quit":
            break
        elif command not in commands:
            print("error! " + command + " not recognized")
        else:
            inputs = commands[command](user, db, inputs) #pass along rest of the inputs
            user = get_user(username, db)


if __name__ == "__main__":
    client = MongoClient()
    db = client.database
    users = db.users
    try:
        main()
    except Exception as e:
        print(e)

