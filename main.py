from todo import TodoItem, test as test_item
from user import User, test as test_user
from todo_service import create as create_item, read, delete_all, delete
from user_service import create_user
from pymongo import MongoClient

def help_fn(curUser):
    print("The following operations are supported: ")
    for op in commands.keys():
        print(op)
        if op in descriptions:
            print('\t' + descriptions[op])

commands = {
        "create": create_item,
        "read": read,
        "delete": delete,
        "clear": delete_all,
        "help": help_fn
        }

descriptions = {
        "create": "Create a new todo item",
        "read": "List all of your todo items",
        "delete": "Delete a todo item",
        "clear": "Delete all todo items",
        "help": "View available commands"
        }

operations = '\n'.join(list(commands.keys()))

def main():
    username = input("who are you? ")
    user = users.find_one({"name": username})
    if not user:
        make_new = input("not a known user, would you like to make a new one? ")
        if make_new == 'yes' or make_new == 'y':
            create_user(username)
    print('For help, just type "help"')
    while(True):
        command = input("what do you want to do today? ")
        if command == "quit":
            break
        elif command not in commands:
            print("error! " + command + " not recognized")
        else:
            commands[command](user, db)
            user = users.find_one({"name": username})


if __name__ == "__main__":
    client = MongoClient()
    db = client.database
    users = db.users
    main()
