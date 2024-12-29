# naive approach to find the sum of all subarrays of a given array
# O(n^2) time and O(1) space

"""
def sub_array_sum(arr):
    n = len(arr)
    result = 0
    
    # pick the starting point
    for i in range(n):
        temp = 0
        # pick the ending point
        for j in range(i, n):
            
            # sum the starting and ending points
            temp  += arr[j]
            result += temp
    return result


arr = [1, 2, 3]

print(sub_array_sum(arr))
"""

# optimal approach to find the sum of all subarrays of a given array
# O(n) time and O(1) space

def sub_array_sum(arr):
    n = len(arr)
    
    result = 0
    
    # computing the sum of subarrays using the formula Total Contribution=arr[i]×(n−i)×(i+1)
    
    for i in range(n):
        
        result += arr[i] * (n - i) * (i + 1)
    
    # return the sum all subarrays 
    return result


arr = [1, 2, 3]
print(sub_array_sum(arr))

 