from myLib.datastructures.nodes.SNode import SNode

class SinglyLinkedList:
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
            self.head = node
        self.size += 1

    def insert_tail(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
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
            current_node.next = node
            self.size += 1

    def search(self, node):
        current_node = self.head
        while current_node is not None:
            if current_node.data is node.data:
                return current_node
            current_node = current_node.next
        return None

    def delete_head(self):
        if not self.head:
            return
        self.head = self.head.next
        self.size -= 1
        if not self.head:
            self.tail = None

    def delete_tail(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next
        current_node.next = None
        self.tail = current_node
        self.size -= 1

    def delete_node(self, node):
        if not self.head:
            return
        if self.head == node:
            self.head = self.head.next
            self.size -= 1
            if not self.head:
                self.tail = None
            return
        current_node = self.head
        while current_node.next != node:
            current_node = current_node.next
        current_node.next = node.next
        self.size -= 1
        if not node.next:
            self.tail = current_node

    def sort(self):
        if not self.head:
            return
        new_head = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            if not new_head or current_node.data < new_head.data:
                current_node.next = new_head
                new_head = current_node
            else:
                search_node = new_head
                while search_node.next and current_node.data > search_node.next.data:
                    search_node = search_node.next
                current_node.next = search_node.next
                search_node.next = current_node
            current_node = next_node
        self.head = new_head

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print_list(self):
        if not self.head:
            print("List is empty")
            return
        current_node = self.head
        print(f"List length: {self.size}")
        print(f"Sorted status: {'Yes' if self.is_sorted() else 'No'}")
        print("List content: ", end="")
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    def __str__(self):
        current = self.head
        node_list = []
        while current:
            node_list.append(str(current.data))
            current = current.next
        return " -> ".join(node_list)