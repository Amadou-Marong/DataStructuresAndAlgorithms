
def insertion_sort(array):
    for index in range(1, len(array)):
        position = index

        temp_value = array[index]
        
        while position > 0 and array[position - 1] > temp_value:
            array[position] = array[position - 1]

            position = position -1

            array[position] = temp_value
    
    return array

array = [4, 2, 7, 1, 3]

print(f"Original array {array}")

# array = insertion_sort(array)
print(f"Sorted array {insertion_sort(array)}")
