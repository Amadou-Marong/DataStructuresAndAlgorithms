def fib(n):
    if n <= 1:
        return n
    
    x = fib(n - 1)
    y = fib(n - 2)
    
    return x + y

if __name__ == "__main__":
    print(fib(7))