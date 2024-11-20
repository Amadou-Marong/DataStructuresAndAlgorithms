# python program to implement insertionsort algorithm

def insertionSort(arr):
    n = len(arr) - 1
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        
        while key >= 0 and key < arr[i]:
            key = arr[i]
            i -= 1
        
            