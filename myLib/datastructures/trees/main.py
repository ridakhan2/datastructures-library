

from BST import BST

print()
print('Testing BST')
print()

# create a BST object
bst = BST()

# insert some nodes
bst.insert(5)
bst.insert(2)
bst.insert(8)
bst.insert(1)
bst.insert(3)
bst.insert(6)
bst.insert(9)

# print the tree in order
print("In order traversal:")
bst.print_in_order()

# print the tree breadth-first
print("Breadth-first traversal:")
bst.print_bf()

# search for a node
node = bst.search(6)
print(f"Node found: {node.data}" if node else "Node not found")

# delete some nodes
bst.delete(2)
bst.delete(8)

# print the tree in order again
print("In order traversal after deleting 2 and 8:")
bst.print_in_order()

# print the tree breadth-first again
print("Breadth-first traversal after deleting 2 and 8:")
bst.print_bf()

# search for a deleted node
node = bst.search(8)
print('Searching for node 8:')
print(f"Node found: {node.data}" if node else "Node not found")


from AVL import AVL

print()
print('Testing AVL')
print()

# create an empty AVL tree
avl = AVL()

# insert values into the AVL tree
avl.insert(10)
avl.insert(5)
avl.insert(20)
avl.insert(3)
avl.insert(8)
avl.insert(15)
avl.insert(25)
avl.insert(1)
avl.insert(4)
avl.insert(6)
avl.insert(9)
avl.insert(13)
avl.insert(17)
avl.insert(22)
avl.insert(27)

# print the AVL tree in-order and breadth-first
print("In-order traversal:")
avl.print_in_order()
print("Breadth-first traversal:")
avl.print_bf()

# search for values in the AVL tree
print("Searching for values:")
print('Searching for node 10')
print(avl.search(10))
print('Searching for node 5')
print(avl.search(5))
print('Searching for node 20')
print(avl.search(20))
print('Searching for node 30')
print(avl.search(30))

# delete values from the AVL tree
avl.delete(8)
avl.delete(13)
avl.delete(22)

# print the AVL tree in-order and breadth-first
print("In-order traversal:")
avl.print_in_order()
print("Breadth-first traversal:")
avl.print_bf()