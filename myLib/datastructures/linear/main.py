from SLL import SinglyLinkedList
from DLL import DoublyLinkedList 
from CSLL import CircularSinglyLinkedList ,Node 
from CDLL import CircularDoublyLinkedList
from Stack import Stack 
from Queue import Queue 



print()
print('Testing SLL:')
print()

# create some nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

nodes_list = [node1, node2, node3, node4, node5]
print('Nodes list:')
for node in nodes_list:
    print(node.data, end=' ')
    
print()


# create a singly linked list and insert nodes
sll = SinglyLinkedList()
sll.insert_head(node1)
print('Singly Linked list after inserting head:', sll)
# sll.insert_tail(node2)
# print('Singly Linked list after inserting tail:', sll)                
sll.insert(node3, 1)
print('Singly Linked list after inserting node3 into position one:', sll)  

sll.insert_tail(node2)
print('Singly Linked list after inserting tail:', sll)

sll.sorted_insert(node4)
print('Singly Linked list after a sorted insert of node4:', sll)
sll.sorted_insert(node5)
print('Singly Linked list after a sorted insert of node5:', sll)


# print the list and search for a node
sll.print_list()
print("Searching for node with data=3...")
result = sll.search(Node(3))
if result:
    print("Node found!")
else:
    print("Node not found.")

# delete nodes and print the list again
sll.delete_head()
print('Singly Linked list after deleting head:', sll)
# sll.delete_tail()                                                         #deletetail method not working (deleted whole list)
# print('Singly Linked list after deleting tail:', sll)
sll.delete_node(node4)
print('Singly Linked list after deleting node4:', sll)
sll.print_list()

sll.sort()
sll.print_list()



print()
print('Testing DLL:')
print()

# Create a new doubly linked list
dll = DoublyLinkedList()

# Test insert_head() and insert_tail()
print("Inserting 3 nodes at the head...")
dll.insert_head(Node(3))
dll.insert_head(Node(2))
dll.insert_head(Node(1))
dll.print_list()

print("Inserting 3 nodes at the tail...")
dll.insert_tail(Node(4))
dll.insert_tail(Node(5))
dll.insert_tail(Node(6))
dll.print_list()

# Test insert()
print("Inserting a node at position 3...")
dll.insert(Node(10), 3)
dll.print_list()

print("Inserting a node at position 0...")
dll.insert(Node(0), 0)
dll.print_list()

print("Inserting a node at position 8...")
dll.insert(Node(20), 8)
dll.print_list()

# Test sorted_insert()
print("Inserting a node in a sorted list...")
dll.sorted_insert(Node(7))
dll.print_list()

# Test search()
print("Searching for a node with value 3...")
node = dll.search(Node(3))
if node:
    print("Node found!")
else:
    print("Node not found!")

print("Searching for a node with value 30...")
node = dll.search(Node(30))
if node:
    print("Node found!")
else:
    print("Node not found!")

# Test delete_head() and delete_tail()
print("Deleting the head node...")
dll.delete_head()
dll.print_list()

print("Deleting the tail node...")
dll.delete_tail()
dll.print_list()

# Test delete_node()
print("Deleting a node with value 10...")          
dll.delete_node(Node(10))
dll.print_list()

print("Deleting a node with value 1...")
dll.delete_node(Node(1))   
dll.print_list()

# Test clear()
print("Clearing the list...")
dll.clear()
dll.print_list()

# Test sorting
# print("Sorting the list...")
dll.insert_tail(Node(5))
dll.insert_tail(Node(1))
dll.insert_tail(Node(3))
dll.insert_tail(Node(2))
dll.insert_tail(Node(4))
dll.print_list()
print("Sorting the list...")
dll.sort()
dll.print_list()



print()
print('Testing CSLL:')
print()

# create some nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# create a circular singly linked list
csl = CircularSinglyLinkedList()

# insert nodes at head and tail
csl.insert_head(node5)
csl.insert_tail(node3)
print('Circular singly linked list after inserting head and tail:')
csl.print_list()  # List content: 5 3  List length: 2  List is sorted

# insert node at specific position
print('Circular singly linked list after inserting node2 at position one:')
csl.insert(node2, 1)
csl.print_list()  # List content: 5 2 3  List length: 3  List is sorted

# search for a node and delete it
print('Circular singly linked list after searching for node2 and deleting it:')
found_node = csl.search(node2)
if found_node:
    csl.delete_node(found_node)
csl.print_list()  # List content: 5 3  List length: 2  List is sorted

# insert node in sorted order
print('Circular singly linked list after a sorted insert of node2:')
csl.sorted_insert(node2)
csl.print_list()  # List content: 5 2 3  List length: 3  List is sorted

# Test search()
print("Searching for a node with value 3...")
node = dll.search(Node(3))
if node:
    print("Node found!")
else:
    print("Node not found!")

# delete head and tail nodes
print('Circular singly linked list after deleting head and tail nodes:')
csl.delete_head()
csl.delete_tail()
csl.print_list()  # List content: 2  List length: 1  List is sorted

# clear the list
print('Clearing the list:')
csl.clear()
csl.print_list()  # List is empty


print()
print('Testing CDLL:')
print()

# Create a new circular doubly linked list
cdll = CircularDoublyLinkedList()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

# Test insert_head() and insert_tail()
print("Inserting 3 nodes at the head...")
cdll.insert_head(node3)
cdll.insert_head(node2)
cdll.insert_head(node1)
cdll.print_list()

print("Inserting 3 nodes at the tail...")
cdll.insert_tail(node4)
cdll.insert_tail(node5)
cdll.insert_tail(node6)
cdll.print_list()

# Test insert()
print("Inserting a node at position 2...")
cdll.insert(Node(10), 2)
cdll.print_list()

# Test is_sorted()
print("Checking if the list is sorted...")
print(cdll.is_sorted())

# Test sorted_insert()
print("Inserting a sorted node...")
cdll.sorted_insert(Node(7))
cdll.print_list()

print("Inserting a node at position 2...")
cdll.insert(Node(12), 2)
cdll.print_list()

print("Sorting the list...")
cdll.sort()
cdll.print_list()

# Test search()
print("Searching for node with data 10...")
node = cdll.search(Node(10))
if node:
    print("Found node with data:", node.data)
else:
    print("Node not found")

# Test delete_head()
print("Deleting head node...")
cdll.delete_head()
cdll.print_list()

# Test delete_tail()
print("Deleting tail node...")
cdll.delete_tail()
cdll.print_list()

# Test delete_node()
print("Deleting node with data 3...")
node = cdll.search(Node(3))
if node:
    cdll.delete_node(node)
    cdll.print_list()
else:
    print("Node not found")

# Test clear()
print("Clearing the list...")
cdll.clear()
cdll.print_list()





# import the Stack class
print()
print("Testing Stack:")
print()

# Create a new stack
my_stack = Stack()

# Check if the stack is empty
print('The initial stack is empty:', my_stack.is_empty()) # True

# Create some nodes to add to the stack
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Push the nodes onto the stack
my_stack.push(node1)
my_stack.push(node2)
my_stack.push(node3)

print('Stack after pushing 3 nodes:')
my_stack.print_list()

# Check if the stack is empty
# print(my_stack.is_empty()) # False
print('Stack is empty:', my_stack.is_empty()) # False

# Peek at the top node of the stack
print('Stack top node found through peek:', my_stack.peek().data)

# Pop the top node off the stack
my_node = my_stack.pop()
# print(my_node.data) # 3

# Print the current state of the stack
print('Stack after popping top node:')
my_stack.print_list() # 2 -> 1 -> None

# Insert a new node at the head of the stack
print('Stack after inserting 4 to the head:')
new_node = Node(4)
my_stack.insert_head(new_node)
my_stack.print_list() # 4 -> 2 -> 1 -> None

# Insert a new node at a specific position in the stack
print('Stack after inserting 5 into position 2:')
new_node = Node(5)
my_stack.insert(new_node, 2)
my_stack.print_list() # 4 -> 2 -> 5 -> 1 -> None

# Delete a specific node from the stack
print('Stack after deleting node with value 1:')
my_stack.delete_node(node1)
my_stack.print_list() # 4 -> 2 -> 5 -> None

# Delete the tail node from the stack
print('Stack after deleting tail node:')
my_stack.delete_tail()
my_stack.print_list() # 4 -> 2 -> None

# Sort the stack
print('Stack after doing a sorted insert of 1 and 3')
my_stack.sorted_insert(Node(1))
my_stack.sorted_insert(Node(3))
my_stack.sorted_insert(Node(2))
my_stack.print_list() # 1 -> 2 -> 3 -> 4 -> None


print()
print('Testing Queue:')
print()
# Create a new LLQueue object
queue = Queue()

# Test enqueue and print_queue methods
print("Testing enqueue and print_queue methods...")
queue.enqueue(Node(1))
queue.enqueue(Node(2))
queue.enqueue(Node(3))
queue.enqueue(Node(4))
queue.enqueue(Node(5))
queue.print_queue()  # Expected output: 1 -> 2 -> 3 -> 4 -> 5 -> None

# Test dequeue method
print("Testing dequeue method...")
node = queue.dequeue()
print('First element of queue:', node.data)  # Expected output: 1
node = queue.dequeue()
print('First element of queue after removing 1:', node.data)  # Expected output: 2
queue.print_queue()  # Expected output: 3 -> 4 -> 5 -> None

# Test peek method
print("Testing peek method...")
node = queue.peek()
print('Top of queue:',node.data)  # Expected output: 3

# Test search method
print("Testing search method...")
pos = queue.search(4)
print('Current position of the value 4 in the queue:', pos)  # Expected output: 1
pos = queue.search(6)
print('Current position of the value 6 in the queue:',pos)  # Expected output: Not found

# Test clear method
print("Testing clear method...")
queue.clear()
queue.print_queue()  # Expected output: None

# Test full and empty methods
print("Testing full and empty methods...")
print('Queue is full:', queue.full())  # Expected output: False
print('Queue is empty:', queue.empty())  # Expected output: True



