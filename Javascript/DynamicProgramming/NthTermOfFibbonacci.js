function fib(n) {
    if (n <= 1) {
        return n
    }
    
    let x = fib(n - 1)
    let y = fib(n - 2)

    return x+y
}

console.log(fib(7));
