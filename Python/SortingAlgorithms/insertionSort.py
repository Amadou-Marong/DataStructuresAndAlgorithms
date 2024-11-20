# python program to implement insertionsort algorithm

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


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
