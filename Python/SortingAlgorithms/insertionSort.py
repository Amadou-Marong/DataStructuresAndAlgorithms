# python program to implement insertionsort algorithm

def insertionSort(arr):
    n = len(arr)
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        
        while i >= 0 and key < arr[i]:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key


# function to print array elements
def printArray(arr):
    n = len(arr)
    for i in range(n):
        print(arr[i], end=" ")
    print()


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    
    insertionSort(arr)
    
    printArray(arr)
