# python program to insert a node at the front of the linked list

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


def insert_at_front(head, new_data):
    # create a new node with the given data
    new_node = Node(new_data)

    # make the next of the new node point to the current head
    new_node.next = head

    # return the new node as the new head of the list
    return new_node


def print_list(head):
    curr = head
    while curr is not None:
        print(f"{curr.data}", end="->")
        curr = curr.next
    print()

# code execution starts here
if __name__ == "__main__":

    # create a linked list 2->3->4->5
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)

    data = 1

    head = insert_at_front(head, data)
    print_list(head)