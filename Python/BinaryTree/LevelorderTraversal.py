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

    # Enqueue Root and initialize height
    queue.append(root)

    while(len(queue) > 0):
        # Print front of queue and
        # remove it from queue
        print(queue[0].data)

        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        

    
