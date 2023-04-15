

from myLib.datastructures.nodes.TNode import TNode

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = TNode(val)
        self._insert(new_node)

    def _insert(self, new_node):
        temp = self.root
        parent = None
        while temp is not None:
            parent = temp
            if new_node.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

    def delete(self, val):
        self.root = self._delete_helper(self.root, val)

    def _delete_helper(self, node, val):
        if node is None:
            print("Value not found in the tree.")
            return None
        if val < node.data:
            node.left = self._delete_helper(node.left, val)
        elif val > node.data:
            node.right = self._delete_helper(node.right, val)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_min(node.right)
                node.data = successor.data
                node.right = self._delete_helper(node.right, successor.data)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def search(self, val):
        temp = self.root
        while temp is not None:
            if val == temp.data:
                return temp
            elif val < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return None

    def print_in_order(self):
        self._print_in_order_helper(self.root)
        print()

    def _print_in_order_helper(self, node):
        if node is not None:
            self._print_in_order_helper(node.left)
            print(node.data, end=" ")
            self._print_in_order_helper(node.right)

    def print_bf(self):
        queue = []
        queue.append(self.root)

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                current = queue.pop(0)
                assert current is not None
                print(current.data, end=" ")

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            print()  # print a new line after each level