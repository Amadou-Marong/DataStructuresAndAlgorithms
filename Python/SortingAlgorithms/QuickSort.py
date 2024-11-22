#  python program to implement quicksort algorithm

# function to partition
def partition(arr, low, high):
    
    # choose a pivot index
    pivot = arr[high]
    