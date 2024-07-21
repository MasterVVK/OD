#Построение из отсортированного массива

from OD02.Tree.print_tree import Node, display_tree


class BinaryTree:
    def __init__(self):
        self.root = None

    def sorted_array_to_bst(self, arr):
        if not arr:
            return None

        mid = len(arr) // 2
        root = Node(arr[mid])

        root.left = self.sorted_array_to_bst(arr[:mid])
        root.right = self.sorted_array_to_bst(arr[mid + 1:])

        return root


# Пример использования построения из отсортированного массива
arr = [10, 20, 30, 40, 50, 60, 70]
tree = BinaryTree()
root = tree.sorted_array_to_bst(arr)

# Печать дерева
display_tree(root)
