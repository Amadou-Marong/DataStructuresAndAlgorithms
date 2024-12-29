# python program to find the sum of all subarrays of a given array

def sum_of_all_subarrays(arr):
    n = len(arr)
    result = 0
    
    # outer loop to pick the starting index of the subarray
    for start in range(n):
        
        # inner loop to pick the ending index of the subarray
        for end in range(start, n):
            
            # slice the array from start to end and print it
            subarray = arr[start:end + 1]
           
            for item in subarray:
                result += item
            
    return result
        

            
# Example usage
array = [1, 2, 3]

print("Result of the sum of subarrays")
print(sum_of_all_subarrays(array))
        
    