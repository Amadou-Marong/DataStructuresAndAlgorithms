# function to calculate the nth fibbonacci number

def nth_fibbonacci(n):
    
    # initialize the list 
    dp = [0] * (n + 1)
    
    # define the base cases
    
    dp[0] = 0
    dp[1] = 1
    
    # use the bottom up approach
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]