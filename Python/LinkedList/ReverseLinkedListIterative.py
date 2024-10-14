# iterative method to reverse a linked list 

# create a node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# function to reverse list
def reverse_list(head):
    prev = None
    curr = head
    
    while curr is not None:
        next_node = curr.next

        curr.next = prev
        prev = curr

    return prev

# function to printList
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
    head.next.next.next = Node(4)

    
    print_list(head)