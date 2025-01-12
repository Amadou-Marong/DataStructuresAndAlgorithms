# python program move all the zeros to the end of the array 
# while maintaining the relative order of all non-zero elements.
"""
[Naive Approach] Using Temporary Array – O(n) Time and O(n) Space

The idea is to create a temporary array of same size as the input array arr[]. 


First, copy all non-zero elements from arr[] to the temporary array. 
Then, fill all the remaining positions in temporary array with 0.
Finally, copy all the elements from temporary array to arr[].

"""

def moveZerosToEnd(arr):
    n = len(arr)
    
    # create a temporary array to store the non zero numbers
    temp = [0] * n
    j = 0
    for i in range(n):
        if arr[i] != 0:
            temp[j] = arr[i]
            j+=1
        
    return temp
    
    
# code execution
if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    
    print(moveZerosToEnd(arr))