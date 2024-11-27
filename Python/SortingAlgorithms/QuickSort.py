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
    

# define a swaf function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    
    