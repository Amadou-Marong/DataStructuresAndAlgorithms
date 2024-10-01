def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(i, high):
        if array[j] == pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i+1

