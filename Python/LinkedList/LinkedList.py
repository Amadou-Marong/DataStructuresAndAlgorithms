# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None



if __name__ == "__main__":

    llist = LinkedList()

    llist.head = Node(1)

    second = Node(2)

    third = Node(3)

    # link the nodes 

    llist.head.next = second
    llist.second.next = third

    
    