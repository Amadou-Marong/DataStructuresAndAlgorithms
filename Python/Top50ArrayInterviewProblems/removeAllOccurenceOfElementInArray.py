# remove all occurences of an element in an array

def removeOccurence(arr, ele):
    n = len(arr)
    
    temp = []
    
    for i in range(n):
        if arr[i] != ele:
            temp.append(arr[i])
          
    
    return len(temp)

    

arr = [3, 2, 2, 3]
ele = 3

print(removeOccurence(arr, ele))

