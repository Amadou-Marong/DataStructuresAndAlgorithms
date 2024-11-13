
def linearSearch(arr, key):
    n = len(arr)

    for i in range(n):
        if (arr[i] == key):
            return i
    return -1
    
my_array = [2, 3, 4, 10, 40]
key = 10

result = linearSearch(my_array, key)

if(result == -1):
    print(f"The element {key} is not found in the array")
else:
    print(f"The element {key} is found at index {result}")