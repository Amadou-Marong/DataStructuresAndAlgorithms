def generate_all_subarrays(arr):
    n = len(arr)
    
    # outer loop to pick the starting index
    for i in range(0, n):
        
        # pick ending point
        for j in range(i, n):
            