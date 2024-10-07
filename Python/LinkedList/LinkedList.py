# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # linked list traversal

    def printlist(self):
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next



if __name__ == "__main__":

    llist = LinkedList()

    llist.head = Node(1)

    second = Node(2)

    third = Node(3)

    # link the nodes 
    llist.head.next = second
    second.next = third

    llist.printlist()


    