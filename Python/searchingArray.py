
def findElement(arr, n, key):
    for i in range(n):
        if arr[i] == key:
            return i
    
    # if key is not found
    return -1


# Example usage
if __name__ == "__main__":
    # Define an unsorted array
    arr = [4, 2, 5, 3, 8, 6, 5, 9]

    # key to search for
    key = 3


    arr = [4, 2, 7, 1, 9, 3]
    
    # Key to search for
    key = 9


    # get the length of the array

    n = len(arr)

    # call the function

    index = findElement(arr, n, key)

    # print the array

    if index != -1:
        print(f"the element {key} is found at index: {index} of the array")
    else:
        print(f"The element {key} is not found in the array")
