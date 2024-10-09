# create a node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create a function to insert a node before a given node

def insert_before(head, key, new_data):
    prev = None
    curr = head

    # if node is not found 
    if head is None:
        return None

    # if the key is found at the head
    if head.data == key:
        new_node = Node(new_data)
        new_node.next = head
        return new_node
    
    while curr is not None and curr.data != key:
        prev = curr
        curr = curr.next

    if curr is not None:
        new_node = Node(new_data)
        prev.next = new_node
        new_node.next = curr
    
    return head
    

# create a function to print the nodes

def print_list(head):
    curr = head
    while curr is not None:
        print(f"{curr.data}", end="->")
        curr = curr.next
    print()


# code execution starts here
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(5)

    data = 4
    head = insert_before(head, 5, data)
    print_list(head)