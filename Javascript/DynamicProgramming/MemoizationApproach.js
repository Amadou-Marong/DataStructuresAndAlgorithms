// Javascript program to get the nth fibbonacci number using memoization approach
// Utility function
function nth_fibbnacci_util(n, memo) {

    // Base case if n < = -1 
    if (n <= 1) {
        return n
    }

    // Iterative case if n != -1
    if (memo[n] != -1) {
        return memo[n]
    }

    // create a memo table
    memo[n] = nth_fibbnacci_util(n-1, memo) + nth_fibbnacci_util(n-2, memo)

    return memo[n]
}

