
def reverse_array_extra_array(arr):
    reversed_array = arr[::-1]

    # print reversed array
    print("Reversed Array:", end=" ")
    for i in reversed_array:
        print(i, end=" ")


# example usage
original_array = [1,4,5,6,7,8]

reverse_array_extra_array(original_array)