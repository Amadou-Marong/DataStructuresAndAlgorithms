# python program to find the sum of all subarrays of a given array

def sum_of_all_subarrays(arr):
    n = len(arr)
    
    # outer loop to pick the starting index of the subarray
    for start in range(n):
        
        # inner loop to pick the ending index of the subarray
        for end in range(start, n):
            
            # slice the array from start to end and print it
            subarray = arr[start:end + 1]
            print(subarray)
            
# Example usage
array = [1, 2, 3]
print("All subarrays:")
sum_of_all_subarrays(array)
        
    