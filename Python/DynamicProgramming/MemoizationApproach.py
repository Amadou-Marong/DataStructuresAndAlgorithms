# function to calculate the nth fibbonacci number using memoization

def nth_fibbonacci_util(n, memo):
    
    if n <= 1:
        return n
    
      
    if memo[n] != -1:
        return memo[n]
    
    memo = nth_fibbonacci_util(n - 1, memo) + nth_fibbonacci_util(n - 2, memo)
    