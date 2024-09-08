my_array = [64, 34, 25, 12, 22, 11, 90, 5]

for i in range(1, len(my_array)):
    key = my_array[i]
    j = i-1
    while j >= 0 and key < my_array[j]:
        my_array[j+1] = my_array[j]
        j -= 1
    my_array[j+1] = key

print("Sorted array is: ", my_array)