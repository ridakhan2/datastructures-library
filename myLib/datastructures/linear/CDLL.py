from DLL import DoublyLinkedList
from myLib.datastructures.nodes.DNode import DNode

class CircularDoublyLinkedList(DoublyLinkedList):
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0
        if head:
            self.head.next = self.head
            self.head.prev = self.head
            self.size = 1

    def insert_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            node.next = self.head
            node.prev = self.tail
            self.head.prev = node
            self.tail.next = node
            self.head = node
        self.size += 1

    def insert_tail(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            node.prev = self.tail
            node.next = self.head
            self.tail.next = node
            self.head.prev = node
            self.tail = node
        self.size += 1

    def insert(self, node, position):
        if position <= 0:
            self.insert_head(node)
        elif position >= self.size:
            self.insert_tail(node)
        else:
            current_node = self.head
            for _ in range(position - 1):
                current_node = current_node.next
            node.next = current_node.next
            node.prev = current_node
            current_node.next.prev = node
            current_node.next = node
            self.size += 1

    def is_sorted(self):
        super().is_sorted()

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
            node.prev = current_node
            if current_node.next != self.head:
                current_node.next.prev = node
            current_node.next = node
            self.size += 1

    def search(self, node):
        current_node = self.head
        while current_node and current_node != self.head.prev:
            if current_node.data == node.data:
                return current_node
            current_node = current_node.next
        return None

    def delete_head(self):
        if not self.head:
            return
        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head
        self.size -= 1

    def delete_tail(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            return
        
        current = self.head
        while current.next != self.head:
            current = current.next
        
        current.prev.next = self.head
        self.head.prev = current.prev
        
    def delete_node(self, node):
        if not self.head:
            return
        
        if self.head == node:
            self.head = self.head.next
        
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def sort(self):
        if not self.head:
            return
        
        current = self.head
        while current.next != self.head:
            inner_current = current.next
            while inner_current != self.head:
                if current.data > inner_current.data:
                    current.data, inner_current.data = inner_current.data, current.data
                inner_current = inner_current.next
            current = current.next
        
    def clear(self):

        super().clear()
        
    def print_list(self):
        if not self.head:
            print("List is empty")
            return
        
        current = self.head
        count = 1
        is_sorted = True
        print("List content: ", end="")
        print(current.data, end=" ")
        current = current.next
        
        while current != self.head:
            print(current.data, end=" ")
            if current.data < current.prev.data:
                is_sorted = False
            current = current.next
            count += 1
        
        print("\nList length:", count)
        if is_sorted:
            print("List is sorted")
        else:
            print("List is not sorted")
        