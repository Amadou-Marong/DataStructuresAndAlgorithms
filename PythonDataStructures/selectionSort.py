my_array = [64, 34, 25, 5, 22, 11, 90, 12]

for i in range(len(my_array)):
    min_index = i
    for j in range(i+1, len(my_array)):
        if my_array[min_index] > my_array[j]:
            min_index = j
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print("Sorted array is: ", my_array)