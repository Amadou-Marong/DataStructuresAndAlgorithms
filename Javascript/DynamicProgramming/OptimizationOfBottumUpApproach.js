// Optimization of the bottum up approach to find the nth fibbonacci number

function nth_fibbonacci(n){
    let prev = 0
    let curr = 1

    // using tabulation
    for(let i=2; i<n+1; i++) {
        let next = prev + curr
        prev = curr
        curr = next
    }
    return curr
}

