# python program to implement mergesort algorithm
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    
    # create temp arrays
    L = [0] * n1
    R = [0] * n2
    
    # copy data to temp arrays
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[right + mid + j]
    
    