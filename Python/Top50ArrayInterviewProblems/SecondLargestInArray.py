# python program to find the second largest distinct element from an array

"""
Given an array of positive integers arr[] of size n, 
the task is to find second largest distinct element in the array.
"""

# [Naive Approach] Using Sorting – O(n*logn) Time and O(1) Space
def getSecondLargest(arr):
    n = len(arr)

    arr.sort()
    
    largest = arr[-1]
    
    # starting from the second largest element
    for i in range(n-2, -1, -1):
        
        # return the first element which is not equal to the largest element
        if arr[i] != largest:
            secondLargest = arr[i]
            
            return secondLargest
    
    return -1
        

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))