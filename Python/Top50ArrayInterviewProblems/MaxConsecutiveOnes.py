# python program to find the maximum consecutive number of ones in an array

def getMaxConsecutiveOnes(nums):
    #  define the current streak and max streak and initialize them to 0
    current_streak = 0
    max_streak = 0
    
    #  iterate over the nums array to check if one(1) is encountered
    
    for num in nums:
        #  if on(1) is encountered we increament the count of the current streak and compare 
        #  it with the max streak 
        if num == 1:
            current_streak += 1
            
            #  if current streak is greater than the max streak we set the max streak to current streak
            max_streak = max(max_streak, current_streak)
            
        else:
            # otherwise we reset the current streak to zero(0)
            current_streak = 0
    # return the max streak    
    return max_streak


if __name__ == "__main__":
    nums = [1,1,0,1,1,1]
    
    print(getMaxConsecutiveOnes(nums))