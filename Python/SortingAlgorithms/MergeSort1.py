# python program to implement mergesort algorithm

def mergeSort(arr):
    if len(arr) > 1:
        
        # finding the middle of the array
        mid = len(arr) // 2
        
        # devide the array into two halves
        
        L = arr[:mid]
        
        R = arr[mid:]
        
        # sort the first half
        mergeSort(L)
        
        # sort the second half
        mergeSort(R)
        
        i = j = k = 0
        
        # copy the data to temp array L[], and R[]
        while i <= len(L) and j <= len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
        k += 1
        
        # copy the remaining data
        while i <= len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
        while j <= len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        
# function to print the list
def printList(arr):
    for val in arr:
        print(val, end=" ")
    print()

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]        
    print("Given Array")
    printList(arr)
    
    print("Sorted Array")
    mergeSort(arr)
    printList(arr)