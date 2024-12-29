# naive approach to find the sum of all subarrays of a given array

def sub_array_sum(arr):
    n = len(arr)
    result = 0
    
    # pick the starting point
    for i in range(n):
        
        # pick the ending point
        for j in range(i, n):
            
            # sum the starting and ending points


# optimal approach to find the sum of all subarrays of a given array
