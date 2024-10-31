# python program for levelorder traversal of a binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Iterative Method to print the
# height of a binary tree
def printLevelOrder(root):

    # Base case
    if root is None:
        return

    # create an empty queue for level order traversal
    queue = []

