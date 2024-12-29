def generate_all_subarrays(arr):
    n = len(arr)
    
    # outer loop to pick the starting index
    for i in range(0, n):
        
        # pick ending point
        for j in range(i, n):
            
            # print subarrays between starting and ending points
            for k in range(i, j+1):
                print(arr[k], end=" ")
             
            print('\n', end="")

# Driver program
arr = [1, 2, 3, 4]

generate_all_subarrays(arr)