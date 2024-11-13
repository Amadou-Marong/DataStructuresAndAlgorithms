def fact(num):
    if num == 0 or num == 1:
        return 1
    return num * fact(num-1)

mynum = 10
print(f"factorial of {mynum} is {fact(mynum)}")