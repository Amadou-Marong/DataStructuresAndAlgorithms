def printFun(test):
    if (test < 1):
        return 
    else:
        print(test)
        printFun(test - 1)
        print(test, end=" ")
        return
    

printFun(8)