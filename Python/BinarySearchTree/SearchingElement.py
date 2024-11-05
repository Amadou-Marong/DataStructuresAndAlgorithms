class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# fuction to search a key in a BST
def search(root, key):

    if root is None or root.data == key:
        return root

    if root.data > key:
        return search(root, root.right)
    
    if root.data < key:
        return search(root, root.left)

    
    
