"""
Code demonstrating recursion used on a binary tree.
"""

class Node:
    """A binary tree "node".

    Each node contains a "value" and has references to left and right
    sub-nodes in "left" and "right".
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def in_order(node):
    """Walk a binary tree "in-order"."""

    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)

# define a tree
tree = Node(7)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.left.right.left = Node(4)
tree.left.right.right = Node(6)
tree.right = Node(8)
tree.right.right = Node(9)

# walk the tree
in_order(tree)
