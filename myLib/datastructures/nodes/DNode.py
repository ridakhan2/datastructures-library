class DNode:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

    def __eq__(self, other):
        if isinstance(other, DNode):
            return self.data == other.data
        return False
    
