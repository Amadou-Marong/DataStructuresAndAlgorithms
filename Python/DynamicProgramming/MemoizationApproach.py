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
    memo = nth_fibbonacci_util(n - 1, memo) + nth_fibbonacci_util(n - 2, memo)
    
    return memo[n]


def nth_fibbonacci(n):
    
    memo = 