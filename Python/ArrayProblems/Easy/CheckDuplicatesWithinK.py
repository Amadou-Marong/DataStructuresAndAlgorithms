
def containsDuplicatesWithinK(arr, k):
    n = len(arr)
    
    # loop through every element
    for i in range(n):
        
        # loop through 1 to k
        for c in range(1, k + 1):
            
            j = i + c
            
            # check if element occures more than once within the distance
            if j < n and arr[i] == arr[j]:
                return True
            
    return False
    
# driver program 
# arr = [10, 5, 3, 4, 3, 5, 6]

arr = [1, 2, 3, 4, 1, 2, 3, 4]

# arr = [1, 2, 3, 1, 4, 5]
k = 3

print("True" if containsDuplicatesWithinK(arr, k) else "False")
