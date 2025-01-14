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
    
# Time Complexity: O(n), as we are traversing the array only twice.
# Auxiliary Space: O(1)

"""

"""
[Expected Approach] One Traversal – O(n) Time and O(1) Space
The idea is similar to the previous approach where we took a pointer, 
say count to track where the next non-zero element should be placed. 
However, on encountering a non-zero element, instead of directly placing 
the non-zero element at arr[count], we will swap the non-zero element 
with arr[count]. This will ensure that if there is any zero present 
at arr[count], it is pushed towards the end of array and is not overwritten.

"""
def moveZerosToEnd(arr):
    n = len(arr)
    
    # Pointer to track the position for next non-zero element
    count = 0
    
    # itterate over the entire array
    for i in range(n):
        # check if a non zero element is encountered
        if arr[i] != 0:
            # swap the current element with the 0 at index count
            arr[i], arr[count] = arr[count], arr[i]
            # increment the count
            count += 1
    
    # return the array 
    return arr
    

# code execution
if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    
    print(moveZerosToEnd(arr))