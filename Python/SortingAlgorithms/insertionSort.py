# python program to implement insertionsort algorithm

def insertionSort(arr):
    n = len(arr) - 1
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        
        while key >= 0 and key < arr[i]:
            key = arr[i]
            i -= 1
        arr[i + 1] = key


# function to print array elements
def printArray(arr):
    for val in arr:
        print(val, end=" ")
    print()


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
            
