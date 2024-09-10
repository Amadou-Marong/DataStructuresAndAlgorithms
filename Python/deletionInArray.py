import array

def findElement(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            # If the element is found, return the index
            return i
    # If the element is not found, return -1
    return -1


# Delete an element from an array
def deleteElement(arr, key):
    pos = findElement(arr, key)

    if pos == -1:
        print('Element not found in the array')

