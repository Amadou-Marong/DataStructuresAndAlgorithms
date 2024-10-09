# create a node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create a function to insert a node before a given node

def insert_before(head, key, new_data):
    pass

# create a function to print the nodes

def print_list(head):
    pass


# code execution starts here
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(5)
