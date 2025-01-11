# python program to find the three closest sum to target in an array
def closest3Sum(arr, target):
    # code here
    n = len(arr)
    # initialize the minimum difference and the current sum
    minDiff = float('inf')
    closestSum = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                currentSum = arr[i] + arr[j] + arr[k]
                currentDiff = abs(target - currentSum)
                
                if currentDiff < minDiff:
                    closestSum = currentSum
                    minDiff = currentDiff
                elif currentDiff == minDiff:
                    closestSum = max(closestSum, currentSum)
    
    return closestSum
    

if __name__ == "__main__":
    # arr = [-1, 2, 2, 4]
    # target = 4
    arr = [-1,2,1,-4]
    target = 1
    
    print(closest3Sum(arr, target))
    
    
