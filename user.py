"""
User model to be stored in DB
"""
ADMIN_KEY = "admin"
class User:
    """
    each user has a name, admin bool and a DB provided ID
    if id is none, then it hasn't been inserted/read from the DB yet
    """
    def __init__(self, name_):
        self.name = name_
        self.admin = False
        self.todo_items = []

    def add_item(self, item):
        """ adds item to todo_items """
        self.todo_items.append(item)

    def remove_item(self, item):
        """ removes item from todo_items """
        self.todo_items.remove(item)


def test():
    """ a small test helper for the User class """
    user = User("User1")
    user.add_item(1)
    user.remove_item(1)
    print("works")

if __name__ == "__main__":
    test()
