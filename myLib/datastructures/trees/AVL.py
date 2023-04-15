

from BST import BST 
from myLib.datastructures.nodes.TNode import TNode

class AVL(BST):
    def __init__(self, obj=None):
        super().__init__()
        self.root = self._copy_tree(obj) if obj and (obj.left or obj.right) else None

    def _copy_tree(self, node):
        if not node:
            return None
        new_node = TNode(node.data, None, None, None, 0)
        new_node.left = self._copy_tree(node.left)
        new_node.right = self._copy_tree(node.right)
        return new_node

    def _balance_tree(self, node):
        if not node:
            return
        balance = self._get_balance(node)
        if balance > 1:
            if self._get_balance(node.left) >= 0:
                node = self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                node = self._rotate_right(node)
        elif balance < -1:
            if self._get_balance(node.right) <= 0:
                node = self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                node = self._rotate_left(node)
        self._balance_tree(node.left)
        self._balance_tree(node.right)

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_height(self, node):
        if not node:
            return -1
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _update_height(self, node):
        node.balance = self._get_height(node.left) - self._get_height(node.right)

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node):
        self._root = node
        if node and (node.left or node.right):
            self._balance_tree(self._root)

    def insert(self, val):
        if not self.root:
            self.root = TNode(val, None, None, None, 0)
            return
        super().insert(val)
        self._balance_tree(self.root)

    def insert_node(self, new_node):
        if not self.root:
            self.root = new_node
            return
        super().insert_node(new_node)
        self._balance_tree(self.root)

    def delete(self, val):
        super().delete(val)
        self._balance_tree(self.root)

    def search(self, val):
        return super().search(val)

    def print_in_order(self):
        super().print_in_order()

    def print_bf(self):
        super().print_bf()