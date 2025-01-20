# [Naive Approach] Rotate one by one – O(n * d) Time and O(1) Space

"""
In each iteration, shift the elements by one position to the left in a circular 
fashion (the first element becomes the last). Perform this operation d times to 
rotate the elements to the left by d positions.
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