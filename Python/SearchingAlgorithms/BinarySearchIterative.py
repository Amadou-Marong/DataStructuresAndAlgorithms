# iterative python program to implement Binary Search

def binarySearch(arr, key):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == key:
            return mid
        
        if arr[mid] < key:
            low = mid + 1
        
        else:
            high = mid - 1
    return -1

arr = [2, 3, 4, 10, 40]
key = 10

result = binarySearch(arr, key)

print(f"the value {key} is found at index {result} of the array" if result != -1 else f"the value {key} is not found in the array")