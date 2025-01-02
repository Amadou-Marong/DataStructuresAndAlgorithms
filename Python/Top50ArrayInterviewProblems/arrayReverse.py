# python program to reverse an array

# naive approach to reverse an array time O(n) space O(n)
"""
def reverse_array(arr):
    n = len(arr)
    
    # create a temporary array of length n and initial value 0
    temp = [0] * n
    
    # store the values of the original array in reverse order in temp array
    for i in range(n):
        temp[i] = arr[n-i-1]

    # copy the values of temp array to the array to reverse it
    for i in range(n):
        arr[i] = temp[i]
        
    
arr = [1, 4, 3, 2, 6, 5]    

print(f"Original array: {arr}")

reverse_array(arr)

print(f"Reversed array: {arr}")

"""

# two pointers method time O(n) space O(1)

def reverse_array(arr):
    n = len(arr)
    
    left = 0
    right = n - 1
    
    while left < right:
        
        arr[left], arr[right] = arr[right], arr[left]
        
        left += 1
        right -= 1

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5] 
    
    print(f"Original array: {arr}")
    
    reverse_array(arr)
    
    print(f"Reversed array: {arr}")