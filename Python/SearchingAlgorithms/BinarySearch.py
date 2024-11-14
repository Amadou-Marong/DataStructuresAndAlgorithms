# program to implement binary search in python

def binarySearch(arr, key):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
    
        if arr[mid] == key:
            return mid
        
        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
        
    return - 1
         

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
key = 11

result = binarySearch(arr, key)

# if result != -1:
#     print(f"The value {key} is found at index {result} of the array")
# else:
#     print(f"The value {key} is not found in the array")


print(f"The value {key} is found at index {result} of the array" if result!= -1 else f"The value {key} is not found in the array")