# a python class that represents an individual node in a binary tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


# create root 
root = Node(1)
root.left = Node(2)
root.right = Node(3)