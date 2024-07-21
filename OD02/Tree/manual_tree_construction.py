#Ручное построение узлов и их связей

from OD02.Tree.print_tree import Node, display_tree

# Создаем узлы вручную
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

# Печать дерева
display_tree(root)
