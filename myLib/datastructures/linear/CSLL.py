from SLL import SinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList(SinglyLinkedList):
    def __init__(self, head=None):
        if head:
            head.next = head
        self.head = head
        self.tail = head
        self.size = 1 if head else 0

    def insert_head(self, node):
        if not self.head:
            self.head = node
            node.next = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            self.tail.next = self.head
        self.size += 1
        

    def insert_tail(self, node):
        if not self.head:
            self.head = node
            node.next = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
        self.size += 1

    def insert(self, node, position): 
        super().insert(node, position)
        
  
    def is_sorted(self):
        if not self.head:
            return True

        current_node = self.head
        while current_node.next != self.head:
            if current_node.data > current_node.next.data:
                return False
            current_node = current_node.next

        if self.head.data > current_node.data:
            return False

        return True
    
    
    def sorted_insert(self, node):
        if not self.is_sorted():
            self.sort()
        current_node = self.head
        if not current_node or node.data < current_node.data:
            self.insert_head(node)
        else:
            while current_node.next != self.head and node.data > current_node.next.data:
                current_node = current_node.next
            node.next = current_node.next
            current_node.next = node
            self.size += 1

    def search(self, node):
        current_node = self.head
        while current_node:
            if current_node.data == node.data:
                return current_node
            current_node = current_node.next
            if current_node == self.head:
                break


    def delete_head(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size -= 1

    def delete_tail(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            current_node.next = self.head
            self.tail = current_node
        self.size -= 1

    def delete_node(self, node):
        if not self.head:
            return
        if self.head == node:
            self.head = self.head.next
            self.tail.next = self.head
        else:
            current_node = self.head
            while current_node.next != node:
                current_node = current_node.next
            current_node.next = node.next
        self.size -= 1


    def sort(self):
        if self.head is None:
            return
        current = self.head
        while current.next != self.head:
            next_node = current.next
            while next_node != self.head:
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                next_node = next_node.next
            current = current.next
   
    def clear(self): 
        super().clear()

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        length = 0
        is_sorted = True
        while current.next != self.head:
            length += 1
            if current.data > current.next.data:
                is_sorted = False
            current = current.next
        length += 1
        if current.data > self.head.data:
            is_sorted = False
       
        
        print("List content:", end=" ")
        current = self.head
        while current.next != self.head:
            print(current.data, end=" ")
            current = current.next
        print(current.data)
        
        print("List length:", length)
        
        if self.is_sorted():
            print("List is sorted")
        else:
            print("List is not sorted")
    