# python program to implement mergesort algorithm

def mergeSort(arr):
    if len(arr) > 1:
        
        # finding the middle of the array
        mid = (arr)//2
        
        # devide the array into two halves
        
        L = arr[:mid]
        
        R = arr[mid:]
        
        