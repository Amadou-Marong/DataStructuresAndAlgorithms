# implementation of a heap

# importing the heapq to implement the heap queue
import heapq

my_list = [5, 7, 9, 1, 3]

# using the heapify method to convert the list to heap
print(my_list)
heapq.heapify(my_list)

# print the heap queue

print(my_list)

# push elements to the heap
heapq.heappush(my_list, 4)

print("The heap after we pushed 4")
print(my_list)


# using heappop to pop the smallest element from the queue
popped_element = heapq.heappop(my_list)

print(f"The heap after popping the smallest element {popped_element} from the queue")
print(my_list)