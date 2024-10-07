# python program to insert a node at the front of the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_front(head, new_data):
    # create a new node with the given data
    new_node = Node(new_data)

    # make the next of the new node point to the current head
    new_node.next = head

    # return the new node as the new head of the list
    return new_node