

class TNode:
    def init(self):
        self.data = 0
        self.left = None
        self.right = None
        self.parent = None
        self.balance = 0

    def __init__(self, data, left=None, right=None, parent=None, balance=0):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.balance = balance

    # Getters and Setters
    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    # methods
    def print_node(self):
        print("Data: ", self.data)
        print("Balance: ", self.balance)
        print("Left: ", "null" if self.left is None else str(self.left.data))
        print("Right: ", "null" if self.right is None else str(self.right.data))
        print("Parent: ", "null" if self.parent is None else str(self.parent.data))

    # returns the data member as a string (will be used for the tree prints)
    def __str__(self):
        return str(self.data)
            