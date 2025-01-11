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
    
    