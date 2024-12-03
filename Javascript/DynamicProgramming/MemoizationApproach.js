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

// the main function

function nth_fibbnacci(n) {
    let memo = new Array(1 + n).fill(-1)

    return nth_fibbnacci_util(n, memo)
}

let n = 7

let result = nth_fibbnacci(n)

console.log(result);
