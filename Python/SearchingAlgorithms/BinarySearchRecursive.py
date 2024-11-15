# Implementation of binary search using recursion

def binarySearch(arr, low, high, key):
    
    if low <= high:
        
        mid = low + (high - low) // 2
        
        # if the key is found in the middle itself
        if arr[mid] == key:
            return mid
        
        # if element is less than the middle then it can only be found in the left subarray
        elif arr[mid] > key:
            # high = mid - 1
            return binarySearch(arr, low, mid - 1, key)
        
        # else the element can be found in the right subarray
        else:
            # low = mid + 1
            return binarySearch(arr, mid + 1, high, key)
    
    # else the key is not found in the array so we return -1
    return -1


arr = [2, 3, 4, 10, 40]
key = 10

low = 0
high = len(arr) - 1

result = binarySearch(arr, low, high, key)

print(f"the value {key} is found at index {result} of the array" if result != -1 else f"the value {key} is not found in the array")