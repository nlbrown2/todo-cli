# each user has a name and an ID
# if id is none, it hasn't been given one yet
kItemKey = "todoItems"
class User:
    def __init__(self, name_):
        self.name = name_
        self.todoItems = []

    def addItem(self, item):
        self.todoItems.append(item)

    def removeItem(self, item):
        self.todoItems.remove(item)


def test():
    u = User("User1")
    u.addItem(1)
    u.removeItem(1)
    print("works")

if __name__ == "__main__":
    test()
