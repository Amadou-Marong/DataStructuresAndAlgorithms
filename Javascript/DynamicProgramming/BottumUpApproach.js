// Bottom up or Tabulation approach to finding the nth fibbonacci number

function nth_fibbonacci(n) {
    let dp = new Array().fill(n + 1)

    // initialize the base cases
    dp[0] = 0
    dp[1] = 1

    for(let i=2; i<n+1; i++) {
        dp[i] = dp[i - 1] + dp[i - 2]
    }
    return dp[n]
}

let n = 5
let result = nth_fibbonacci(n)

console.log(result);
