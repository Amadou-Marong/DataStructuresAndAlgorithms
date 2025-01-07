# python program to find the third largest element in an array of distinct elements

"""
Naive Approach: The task is to first find the largest element, 
followed by the second-largest element and then excluding them both 
find the third-largest element. The basic idea is to iterate the array 
twice and mark the maximum and second maximum element and then excluding 
them both find the third maximum element, 
i.e the maximum element excluding the maximum and second maximum.

Time O(n) space O(1)
"""
"""
def getThirdLargest(arr):
    
    n = len(arr)
    
    largest = -1
    secondLargest = -1
    thirdLargest = -1
    
    # first iterate over the array to find the maximum. store the value alongside its index
    
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
        
    # Now traverse the whole array finding the second max, excluding the maximum element.
    for i in range(n):
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    
    # Finally traverse the array the third time and find the third largest element 
    # i.e., excluding the maximum and second maximum.

    for i in range(n):
        if arr[i] > thirdLargest and arr[i] != secondLargest and arr[i] != largest:
            thirdLargest = arr[i]
    
    return thirdLargest

if __name__ == "__main__":
    
    arr = [12, 13, 1, 10, 34, 16]
    
    print(getThirdLagest(arr))
"""

"""
Efficient Approach: The problem deals with finding the third largest element in the array in 
a single traversal. The problem can be cracked by taking help of a similar problem- finding the 
second maximum element. So the idea is to traverse the array from start to end and to keep track 
of the three largest elements up to that index (stored in variables). So after traversing the whole 
array, the variables would have stored the indices (or value) of the three largest elements of the array.

Time O(n) Space 0(1)
"""
def getThirdLargest(arr):
    
    n = len(arr)
    
    firstLargest = -1
    secondLargest = -1
    thirdLargest = -1
    
    for i in range(n):
        if arr[i] > firstLargest:
            firstLargest = arr[i]
        
        if arr[i] > firstLargest and arr[i] > secondLargest:
            secondLargest = firstLargest
            firstLargest = arr[i]
        
        if arr[i] > secondLargest and arr[i] > thirdLargest:
            thirdLargest = secondLargest
            secondLargest = arr[i]
    
    return thirdLargest

if __name__ == '__main__':
    arr = [12, 13, 1, 10, 34, 16] 

    print(getThirdLargest(arr))



