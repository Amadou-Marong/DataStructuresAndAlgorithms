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

    return new_arr

# Create an array
arr = array.array('i', [10, 20, 30, 40, 50])
key_to_delete = 30

# find the element 
print(f"Index of {key_to_delete}: {findElement(arr, key_to_delete)}")

# delete element
# print(f"Array after {key_to_delete} id deleted: {deleteElement(arr, key_to_delete)}")

arr = deleteElement(arr, key_to_delete).tolist()

print(f"Array after deletion: {arr}")


