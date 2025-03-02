#  python program to implement quicksort algorithm

# function to partition
def partition(arr, low, high):
    
    # choose a pivot index
    pivot = arr[high]
    
    # pointer for greater element
    i = low - 1
    
    # traverse through all the elements and compare each element with the pivot
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)
    
    # Move pivot after smaller elements and return its value
    swap(arr, i + 1, high)
    return i + 1


# define a swaf function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    
# the quicksort function implementation
def quickSort(arr, low, high):
    if low < high:
        
        # pi for partition index returned of pivot
        pi = partition(arr, low, high)
        
        # recursions calls on smaller elements 
        quickSort(arr, low, pi-1)
        
        # recursion calls on the higher or equal elements
        
        quickSort(arr, pi+1, high)
        

# Driver code
if __name__ == "__main__":
    
    arr = [10, 7, 8, 9, 1, 5]
    
    n = len(arr)
    
    print("Original array")
    print(arr)
    
    quickSort(arr, 0, n-1)
    
    print("Sorted Array")
    
    print(arr)
    