# python program to reverse an array

def reverse_array(arr):
    n = len(arr)
    
    # create a temporary array of length n and initial value 0
    temp = [0] * n
    
    # store the values of the original array in reverse order in temp array
    for i in range(n):
        temp[i] = arr[-i]


arr = [1, 4, 3, 2, 6, 5]    

print(reverse_array(arr))