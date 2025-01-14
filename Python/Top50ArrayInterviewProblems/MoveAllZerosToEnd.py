# python program move all the zeros to the end of the array 
# while maintaining the relative order of all non-zero elements.
"""
[Naive Approach] Using Temporary Array – O(n) Time and O(n) Space

The idea is to create a temporary array of same size as the input array arr[]. 


First, copy all non-zero elements from arr[] to the temporary array. 
Then, fill all the remaining positions in temporary array with 0.
Finally, copy all the elements from temporary array to arr[].

"""
"""
def moveZerosToEnd(arr):
    n = len(arr)
    
    # create a temporary array to store the non zero numbers
    temp = [0] * n
    j = 0
    for i in range(n):
        # copy all the non zero numbers from array in consecutive order to temp 
        if arr[i] != 0:
            temp[j] = arr[i] 
            j+=1
    
    # copy the values of temp to the array 
    for i in range(n):
        arr[i] = temp[i]
        
    return arr
    
    
# code execution
if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    
    print(moveZerosToEnd(arr))


Time complexity: O(n), as we are traversing the array three times.
Auxiliary Space : O(n), as we are using a temp[] array to move all the zeros.
"""

"""
[Better Approach] Two Traversals – O(n) Time and O(1) Space
The idea is to move all the zeros by traversing the array twice.
"""
def moveZerosToEnd(arr):
    
    n = len(arr)
    
    count = 0
    
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    
    while count < n:
        arr[count] = 0
        count += 1
    
    
    return arr
                

# code execution
if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    
    print(moveZerosToEnd(arr))