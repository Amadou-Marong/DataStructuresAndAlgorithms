# python program to swap array in wave form
"""
Naive Approach – Sorting – O(n Log n) time and O(1) Space
A idea is to use sorting. First sort the input array, then swap all adjacent elements.

Follow the steps mentioned below to implement the idea:

Sort the array.
Traverse the array from index 0 to n-1, and increase the value of the index by 2.
While traversing the array swap arr[i] with arr[i+1].
"""
# def swapArray(arr):
#     n = len(arr)
    
#     arr.sort()
    
#     for i in range(0, n-1, 2):
#         arr[i], arr[i+1] = arr[i+1], arr[i]
    
#     return arr


# arr = [20, 10, 8, 6, 4, 2]        
# print(swapArray(arr))

"""
Expected Approach – O(n) Time and O(1) Space
The idea is based on the fact that if we make sure that all even 
positioned (at index 0, 2, 4, ..) elements are greater than their adjacent 
odd elements, we don’t need to worry about oddly positioned elements. 


Follow the steps mentioned below to implement the idea:

Traverse all even positioned elements of the input array, and do the following. 
If the current element is smaller than the previous odd element, swap the previous and current. 
If the current element is smaller than the next odd element, swap next and current.
"""
def swapArray(arr):
    n = len(arr)
    
    #  traverse all even index of the array
    for i in range(0, n-1, 2):
        
        # if array at current even index is less than the previous
        if(i > 0 and arr[i] < arr[i-1]):
            
            # then we swap them
            arr[i], arr[i-1] = arr[i-1], arr[i]
        
        # if the next index element of the array is greater than the current even index 
        if(i < n and arr[i+1] > arr[i]):
            
            # then swap them
            arr[i+1], arr[i] = arr[i], arr[i+1]
    
    return arr

 
arr = [20, 10, 8, 6, 4, 2]   
 
print(swapArray(arr))