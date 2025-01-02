# python program to reverse an array

def reverse_array(arr):
    n = len(arr)
    
    temp = [0] * n
    
    for i in range(n):
        temp[i] = arr[n-i-1]
    
    for i in range(n):
        arr[i] = temp[i]
        
    return arr

arr = [1, 4, 3, 2, 6, 5]    

print(reverse_array(arr))