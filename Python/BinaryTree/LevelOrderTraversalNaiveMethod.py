# Recursive program for level order ttraversal of Binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# function to print level order traversal of a tree




# compute the height of a tree
def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
    
    
