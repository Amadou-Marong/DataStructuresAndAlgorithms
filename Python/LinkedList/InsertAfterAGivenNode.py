# create a node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create a function to print the nodes
def print_list(head):
    curr = head
    while curr is not None:
        print(f"{curr.data}", end="->")
        curr = curr.next

