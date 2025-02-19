# remove all occurences of an element in an array

def removeOccurence(arr, ele):
    n = len(arr)
    
    k = 0
    for i in range(n):
        if arr[i] != ele:
            arr[k] = arr[i]
            k+=1
          
    return k 

    

arr = [3, 2, 2, 3]
ele = 3

print(removeOccurence(arr, ele))

