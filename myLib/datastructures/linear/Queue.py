
from SLL import SinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode

class Queue(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def insert_head(self, node):
        pass  # Override method from SinglyLinkedList with an empty body

    def dequeue(self):
        if self.head:
            node = self.head
            self.head = self.head.next
            self.size -= 1
            if not self.head:
                self.tail = None
            return node
        else:
            return None

    def enqueue(self, node):
        self.insert_tail(node)  # Call SinglyLinkedList's insert_tail method

    def print_queue(self):
        self.print_list()  # Call SinglyLinkedList's print_list method

    def peek(self):
        if self.head:
            return self.head
        else:
            return None

    def search(self, data):
        pos = 0
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                return pos
            curr_node = curr_node.next
            pos += 1
        return "Not found"

    def clear(self):
        super().clear()

    def full(self):
        return False  # LLQueue is not a bounded queue, hence it is never full

    def empty(self):
        return self.size == 0