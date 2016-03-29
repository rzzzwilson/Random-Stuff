class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# define a tree
tree = Node(value=7)
tree.left = Node(value=3)
tree.left.left = Node(value=2)
tree.left.right = Node(value=5)
tree.left.right.left = Node(value=4)
tree.left.right.right = Node(value=6)
tree.right = Node(value=8)
tree.right.right = Node(value=9)

def walk_inorder(node):
    if node is not None:
        walk_inorder(node.left)
        print(node.value)
        walk_inorder(node.right)

def walk_preorder(node):
    if node is not None:
        print(node.value)
        walk_preorder(node.left)
        walk_preorder(node.right)

def walk_postorder(node):
    if node is not None:
        walk_postorder(node.left)
        walk_postorder(node.right)
        print(node.value)

print('Inorder:')
walk_inorder(tree)

print('\nPreorder')
walk_preorder(tree)

print('\nPostorder')
walk_postorder(tree)
