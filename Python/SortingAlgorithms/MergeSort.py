# python program to implement mergesort algorithm
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    
    