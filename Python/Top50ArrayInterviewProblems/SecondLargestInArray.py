# python program to find the second largest distinct element from an array

"""
Given an array of positive integers arr[] of size n, 
the task is to find second largest distinct element in the array.
"""
"""
# [Naive Approach] Using Sorting – O(n*logn) Time and O(1) Space
def getSecondLargest(arr):
    n = len(arr)

    arr.sort()
    
    largest = arr[-1]
    
    # starting from the second last element as the last element is the largest
    for i in range(n-2, -1, -1):
        
        # return the first element which is not equal to the largest element
        if arr[i] != largest:
            secondLargest = arr[i]
            
            return secondLargest
    
    #  return -1 if no second largest element was found
    return -1
        

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))
"""

# [Better Approach] Two Pass Search – O(n) Time and O(1) Space
"""
The approach is to traverse the array twice. In the first traversal, find the maximum element. 
In the second traversal, find the maximum element ignoring the one we found in the first traversal.
"""
"""
def getSecondLargest(arr):
    n = len(arr)
    
    largest = -1
    secondLargest = -1
    
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
            
    for i in range(n):
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
       
            
    return secondLargest


if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))
    
"""

"""
# [Expected Approach] One Pass Search – O(n) Time and O(1) Space

The idea is to keep track of the largest and second largest element while traversing the array. 
Initialize largest and second largest with -1. Now, for any index i,

If arr[i] > largest, update second largest with largest and largest with arr[i].
Else If arr[i] < largest and arr[i] > second largest, update second largest with arr[i]. 
"""

def getSecondLargest(arr):
    n = len(arr)
    
    largest = -1
    secondLargest = -1
    
    for i in range(n):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > secondLargest:
            secondLargest = arr[i]
            
    return secondLargest

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))