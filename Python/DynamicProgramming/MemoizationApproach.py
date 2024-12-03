# function to calculate the nth fibbonacci number using memoization

def nth_fibbonacci_util(n, memo):
    
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    
    # Check if the result is already in the memo table 
    if memo[n] != -1:
        return memo[n]
    
    # Recursive case: calculate Fibonacci number
    # and store it in memo
    memo[n] = nth_fibbonacci_util(n - 1, memo) + nth_fibbonacci_util(n - 2, memo)
    
    return memo[n]


# Wrapper function that handles both initialization
# and Fibonacci calculation
def nth_fibbonacci(n):
    
    # Create a memoization table and initialize with -1
    memo = [-1] * (n + 1)
    
    # Call the utility function
    return nth_fibbonacci_util(n, memo)


if __name__ == "__main__":
    n = 7
    result = nth_fibbonacci(n)
    
    print(result)