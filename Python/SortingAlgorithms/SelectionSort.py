# python program to implement selection sort
def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        
        for j in range(i + 1, n):
            if (arr[j] < arr[min_index]):
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
        

def printArray(arr):
    for val in arr:
        print(val, end=" ")
    print()

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array")
    printArray(arr)
    
    print("Sorted array")
    selectionSort(arr)
    printArray(arr)