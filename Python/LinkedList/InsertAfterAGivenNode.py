# create a node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# function to insert node after a given node
def insert_after(head, key, new_data):
    # traverse the list
    curr = head
    while curr is not None:
        if curr.data == key:
            break
        curr = curr.next

    if curr == None:
        return  head
    
    new_node = Node(new_data)
    new_node.next = curr.next
    curr.next = new_node

    return new_node

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
    head.next.next = Node(4)
    head.next.next.next = Node(5)

    data = 3
    insert_after(head, 2, data)
    print_list(head)
