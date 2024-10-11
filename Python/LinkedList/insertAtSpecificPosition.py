# python program to insert a node at a specific position in a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# function to insert a node at a specific position in linked list
def insert_at(head, postion):
    pass


# function to print linked list
def print_list(head):
    curr = head
    while curr is not None:
        print(f"{curr.data}", end="->")
        curr = curr.next
    print()

# code execution starts here
if __name__ == "__main__":
    head = Node(3)
    head.next = Node(5)
    head.next.next = Node(8)
    head.next.next.next = Node(10)

    print_list(head)