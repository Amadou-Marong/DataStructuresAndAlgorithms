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
            