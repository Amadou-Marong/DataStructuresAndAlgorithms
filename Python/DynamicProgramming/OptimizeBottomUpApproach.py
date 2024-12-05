# Optimization of the bottom up approach

def nth_fibbonacci(n):
    
    # define the base cases
    prev = 0
    curr = 1
    
    # Using the bottom up approach
    for i in range(2, n + 1):
        next = prev + curr
        prev = curr
        curr = next
    return curr

if __name__ == "__main__":
    n = 7
    result = nth_fibbonacci(n)
    
    print(result)