# python program to print the distinct elements in an array

def findDistinct(arr):
    
    results = []
    
    for i in range(len(arr)):
        j = 0
        
        while(j < i):
            # check if element is included in the results
            if arr[i] == arr[j]:
                break
            j+=1

        # add the element if not included previously
        if j == i:
            results.append(arr[i])
            
    return results

if __name__ == "__main__":
    arr = [12, 10, 9, 45, 2, 10, 10, 45]
    print(findDistinct(arr))
    