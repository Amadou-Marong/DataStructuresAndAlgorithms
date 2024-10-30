# python program for postorder traversal of a binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorderTraversal(node):

    if node == None:
        return
    
    postorderTraversal(node.left)

    postorderTraversal(node.right)

    print(node.data, end=" ")


def main():
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)
    postorderTraversal(node)


if __name__ == "__main__":
    main()