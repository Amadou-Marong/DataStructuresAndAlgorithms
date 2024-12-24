# python program to print the distinct elements in an array

def findDistinct(arr):
    
    results = []
    
    arr.sort()
    
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i - 1]:
            results.append(arr[i])
    
    return results

if __name__ == "__main__":
    arr = [12, 10, 9, 45, 2, 10, 10, 45]
    print(findDistinct(arr))
    