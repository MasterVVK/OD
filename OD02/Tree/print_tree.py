class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def display_tree(node, prefix="", is_left=True):
    if node.right is not None:
        display_tree(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
    if node.left is not None:
        display_tree(node.left, prefix + ("    " if is_left else "│   "), True)
