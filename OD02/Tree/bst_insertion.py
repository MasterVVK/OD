#Вставка элементов в бинарное дерево поиска (BST)

from print_tree import Node, display_tree

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.value:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)

# Пример использования BST
bst = BinarySearchTree()
values = [35, 40, 20, 60, 10, 30, 50, 70, 15]
for value in values:
    bst.insert(value)

# Печать дерева
display_tree(bst.root)
