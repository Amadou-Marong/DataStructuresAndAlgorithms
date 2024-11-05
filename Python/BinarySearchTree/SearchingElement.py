class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# fuction to search a key in a BST
def search(root, key):

    # Base case if key is none or found at the root
    if root is None or root.data == key:
        return root

    # if the key is greater than the roots key
    if root.data < key:
        return search(root.right, key)
    
    # if the key is less than the roots key
    
    return search(root.left, key)


root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)


# Searching for keys in BST

print("Found" if search(root, 19) else "Not Found")
print("Found" if search(root, 80) else "Not Found")

    
