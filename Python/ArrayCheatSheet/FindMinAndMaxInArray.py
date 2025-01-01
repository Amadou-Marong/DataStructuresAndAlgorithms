# python program to find the minimum and maximum element in an array

def set_min(arr):
    
    mini = float('inf')
    
    for num in arr:
        if num < mini:
            mini = num
    return mini

def set_max(arr):
    maxi = float('-inf')
    
    for num in arr:
        if num > maxi:
            maxi = num
    return maxi


if __name__ == "__main__":

    arr = [4, 9, 6, 5, 2, 3]
    
    print(set_min(arr))
    print(set_max(arr))
    