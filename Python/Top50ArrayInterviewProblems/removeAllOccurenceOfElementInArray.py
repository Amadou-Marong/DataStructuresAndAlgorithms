# remove all occurences of an element in an array

def removeOccurence(arr, ele):
    n = len(arr)
    
    temp = []
    
    k = 0
    for i in range(n):
        if arr[i] != ele:
            temp.append(arr[i])
            k+=1
    
    return len(temp)

    

arr = [3, 2, 2, 3]
ele = 3

print(removeOccurence(arr, ele))

