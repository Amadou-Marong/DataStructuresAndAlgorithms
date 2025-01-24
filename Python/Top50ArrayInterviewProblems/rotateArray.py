# [Naive Approach] Rotate one by one – O(n * d) Time and O(1) Space

"""
In each iteration, shift the elements by one position to the left in a circular 
fashion (the first element becomes the last). Perform this operation d times to 
rotate the elements to the left by d positions.
"""
"""
def rotateArray(arr, d):
    n = len(arr)
    
    for i in range(d):
        
        first = arr[0]
    
        for j in range(n-1):
            arr[j] = arr[j+1]
        arr[n-1] = first      
        
    return arr

arr = [1, 2, 3, 4, 5, 6]
d = 2
print(rotateArray(arr, d))

"""

"""
[Better Approach] Using Temporary Array – O(n) Time and O(n) Space
This problem can be solved using the below idea:

The idea is to use a temporary array of size n, where n is the length of the 
original array. If we left rotate the array by d positions, the last n – d elements will 
be at the front and the first d elements will be at the end.
"""

def rotateArray(arr, d):
    n = len(arr)
    temp = [0] * n
    
    # for i in range(n-d):
    #     print(arr[i])
        
    for i in range(n-d):
        temp[i] = (arr[d+i])

    print(temp)

arr = [1, 2, 3, 4, 5, 6]
d = 2

rotateArray(arr, 2)
