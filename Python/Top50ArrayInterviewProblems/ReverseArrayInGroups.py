# python program to reverse an Array in groups of given size

def reverseArray(arr, k):
    n = len(arr)
    
    if k == 1:
        return arr
    
    left = 0
    right = n - 1
    
    while right > left:
        arr[left], arr[right] = arr[right], arr[left]
        
        left += 1
        right -= 1
    
    return arr

# Driver code
arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3

print(reverseArray(arr, k)) 

        