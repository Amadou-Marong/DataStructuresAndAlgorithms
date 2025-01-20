def rotateArray(arr, d):
    n = len(arr)
    
    for i in range(d):
        
        first = arr[0]
    
        for j in range(n-1):
            arr[j] = arr[j+1]
        arr[n-1] = first      
        
    return arr

arr = [1, 2, 3, 4, 5, 6]
d = 2
print(rotateArray(arr, d))