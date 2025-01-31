# python program to swap array in wave form

def swapArray(arr):
    n = len(arr)
    
    for i in range(0, n-1, 2):
        print(arr[i])


arr = [1, 2, 3, 4, 5, 6]        
swapArray(arr)