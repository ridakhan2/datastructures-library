
from myLib.datastructures.nodes.DNode import DNode

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0
        if head:
            self.size = 1

    def insert_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insert_tail(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
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
        if not self.head:
            return True
        current_node = self.head
        while current_node.next:
            if current_node.data > current_node.next.data:
                return False
            current_node = current_node.next
        return True
    # def is_sorted(self): 
    #     super().is_sorted()
 

    def sorted_insert(self, node):
        if not self.is_sorted():
            self.sort()
        current_node = self.head
        if not current_node or node.data < current_node.data:
            self.insert_head(node)
        else:
            while current_node.next and node.data > current_node.next.data:
                current_node = current_node.next
            node.next = current_node.next
            node.prev = current_node
            if current_node.next:
                current_node.next.prev = node
            current_node.next = node
            self.size += 1


    def search(self, node):
        current_node = self.head
        while current_node:
            if current_node.data == node.data:
                return current_node
            current_node = current_node.next
        return None

    def delete_head(self):
        if not self.head:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1

    def delete_tail(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        current_node = self.tail.prev
        current_node.next = None
        self.tail = current_node
        self.size -= 1

    def delete_node(self, node):
        current_node = self.head
        if node is None:
            return
        if current_node == node:
            self.head = current_node.next
            current_node.prev = None
            return
        while current_node is not None and current_node.next != node:
            current_node = current_node.next
        if current_node is None:
            return
        current_node.next = current_node.next.next
        if current_node.next is not None:
            current_node.next.prev = current_node

    def sort(self):
        
        if self.head is None:
            return
        
        # Convert the linked list into a Python list, sort it, and then rebuild the linked list
        node_values = []
        current_node = self.head
        while current_node is not None:
            node_values.append(current_node.data) #changed to data
            current_node = current_node.next
            
        node_values.sort()
        
        current_node = self.head
        for i in range(len(node_values)):
            current_node.data = node_values[i] 
            current_node = current_node.next

    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print_list(self):
        if self.head is None:
            print("Empty list")
            return
            
        # Determine the length of the list
        length = 0
        current_node = self.head
        while current_node is not None:
            length += 1
            current_node = current_node.next
            
        # Determine the sorted status of the list
        sorted_status = True
        current_node = self.head
        while current_node.next is not None:
            if current_node.data > current_node.next.data:
                sorted_status = False
                break
            current_node = current_node.next
            
        # Print the list information
        print("List content:", end=" ")
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            if current_node.next is not None:
                print("<->", end=" ")
            current_node = current_node.next
        print() # print a newline at the end

        print("List length:", length)
        if sorted_status:
            print("List is sorted")
        else:
            print("List is not sorted")