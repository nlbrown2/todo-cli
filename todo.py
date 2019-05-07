# each item has a name and a user ID
# TODO: give each item a priority
# TODO: make each item allow for infinite nesting
    # allows for checklists/ordered steps
kItemNameKey = "name"
class TodoItem:
    def __init__(self, name_, userId_):
        self.name = name_
        self.userId = userId_

    def getName(self):
        return self.name

    def getUser(self):
        return self.userId

def test():
    item = TodoItem("first TODO", 1)
    print(item.getName())
    print(item.getUser())
    print(vars(item))

if __name__ == "__main__":
    test()
