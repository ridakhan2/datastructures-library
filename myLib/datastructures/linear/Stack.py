
from SLL import SinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode


class Stack(SinglyLinkedList):
    def __init__(self, head=None):
        super().__init__(head)

    def push(self, node):
        super().insert_head(node)

    def pop(self):
        node = self.head
        self.delete_head()
        return node


    def peek(self):
        return self.head

    def is_empty(self):
        return self.size == 0

    def insert_head(self, node):
        super().insert_head(node)

    def insert_tail(self, node):
        pass

    def insert(self, node, position):
        super().insert(node,position)

    def sorted_insert(self, node):
        super().sorted_insert(node)

    def delete_tail(self):
        super().delete_tail()

    def delete_node(self, node):
        super().delete_node(node)

    def sort(self): 
        super().sort()

    def print_list(self):
        super().print_list()