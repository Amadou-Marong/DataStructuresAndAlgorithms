my_array = [64, 34, 25, 5, 22, 11, 90, 12]

for i in range(len(my_array)):
    for j in range(len(my_array)-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print("Sorted array is: ", my_array)