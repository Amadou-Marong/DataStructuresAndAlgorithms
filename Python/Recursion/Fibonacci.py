# program to print the fibonacci series using recursion

def fibonacci(num):

    if (num == 0):
        return 0
    if (num == 1 or num == 2):
        return 1
    else:
        return (fibonacci(num - 1) + fibonacci(num - 2))
    

num = 5
print(f"fibonacci of {num} number series:")
for i in range(0, num):
    print(fibonacci(i), end=" ")
