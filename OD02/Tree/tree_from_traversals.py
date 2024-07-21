#Построение из предобхода и симметричного обхода

from OD02.Tree.print_tree import Node, display_tree

class BinaryTreeFromTraversal:
    def build_tree(self, inorder, preorder):
        if not inorder or not preorder:
            return None

        root_value = preorder.pop(0)
        root = Node(root_value)
        inorder_index = inorder.index(root_value)

        root.left = self.build_tree(inorder[:inorder_index], preorder)
        root.right = self.build_tree(inorder[inorder_index+1:], preorder)

        return root

# Пример использования построения из обхода
inorder = [9, 3, 15, 20, 7]
preorder = [3, 9, 20, 15, 7]
tree = BinaryTreeFromTraversal()
root = tree.build_tree(inorder, preorder)

# Печать дерева
display_tree(root)
