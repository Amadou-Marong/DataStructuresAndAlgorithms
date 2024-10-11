# python program to insert a node at a specific position in a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# function to insert a node at a specific position in linked list
def insert_at(head, postion, new_data):
    # create a new node
    new_node = Node(new_data)
    # if the position is at 1
    if postion == 1:
        new_node.next = head
        head = new_node
        return head
    
    curr = head
    for _ in range(1, postion-1):
        if curr is None:
            break
        curr = curr.next

    # if current is none
    if curr is None:
        print("Position is out of bounds")
        return head

    new_node.next = curr.next
    curr.next = new_node
    return head 


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

    data, position = 12, 2
    head = insert_at(head, position, data)

    print_list(head)