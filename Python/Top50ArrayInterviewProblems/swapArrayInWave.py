# python program to swap array in wave form

def swapArray(arr):
    n = len(arr)
    
    arr.sort()
    
    for i in range(0, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    
    return arr


arr = [20, 10, 8, 6, 4, 2]        
print(swapArray(arr))