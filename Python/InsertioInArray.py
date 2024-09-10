import array

def insert_element(arr, x, pos):
    n = len(arr)
    if pos < 0 or pos > n:   # Check if the position is valid
        raise IndexError('Index out of bounds')
    
    # Create a new array with one more element
    new_arr = array.array(arr.typecode, [0] * (n + 1))

    # Copy the elements of the original array to the new array

    for i in range(pos):
        new_arr[i] = arr[i]
    new_arr[pos] = x
    for i in range(pos, n):
        new_arr[i + 1] = arr[i]
    return new_arr

