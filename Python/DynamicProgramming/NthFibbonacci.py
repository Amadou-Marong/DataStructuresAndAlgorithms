def nth_fibonacci(n):
    # Base case if n = 0 or n = 1
    if n <= 1:
        return n
    
    # Recursive case if the number is greater than 1
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


if __name__ =="__main__":
    n = 10
    print(nth_fibonacci(n))