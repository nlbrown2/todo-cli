"""
model for todo item, revisions to come
"""
# TODO: give each item a priority
# TODO: make each item allow for infinite nesting
    # allows for checklists/ordered steps
ITEM_NAME_KEY = "name"
class TodoItem:
    """ model for a single todo item. contains a name and a user id even tho it
    is embedded in the user document"""
    def __init__(self, name_, userId_):
        self.name = name_
        self.user_id = userId_

    def get_name(self):
        """ returns name of item """
        return self.name

    def get_user(self):
        """ returns id of user """
        return self.user_id

def test():
    """ smol test for todo item model """
    item = TodoItem("first TODO", 1)
    print(item.get_name())
    print(item.get_user())
    print(vars(item))

if __name__ == "__main__":
    test()
