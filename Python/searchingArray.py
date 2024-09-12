def findElement(arr, n, key):
    for i in range(n):
        if arr[i] == key:
            return i
        return -1


# Example usage
if __name__ == "__main__":
    # Define an unsorted array
    arr = [4, 2, 5, 3, 8, 6, 5, 9]

    # key to search for
    key = 9
    
