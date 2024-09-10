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
        return arr
    
    # create a new array with one less element
    new_arr = array.array(arr.typecode, [0] * (len(arr) - 1))

    # copy elements of the original array to the new array except the element to be deleted

    for i in range(pos):
        new_arr[i] = arr[i]
    for i in range(pos + 1, len(arr)):
        new_arr[i - 1] = arr[i]
    


