
def containsDuplicatesWithinK(arr, k):
    n = len(arr)
    
    # loop through every element
    for i in range(n):
        
        # loop through 1 to k
        for j in range(i, k+1):
            
            # check if element occures more than once within the distance
            if arr[i] == arr[j]:
                return False
            
        return False
    
# driver program 
# arr = [10, 5, 3, 4, 3, 5, 6]

# arr = [1, 2, 3, 4, 1, 2, 3, 4]

arr = [1, 2, 3, 1, 4, 5]
k = 3

print("Yes" if containsDuplicatesWithinK(arr, k) else "No")
