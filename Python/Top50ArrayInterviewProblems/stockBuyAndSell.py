# best time to buy and sell stock
"""
[Naive Approach] By exploring all possible pairs – O(n^2) Time and O(1) Space
The idea is to use two nested loops to explore all the possible ways to buy and sell stock. 
The outer loop decides the day to buy the stock and the inner loop decides the day to sell the stock. 
The maximum difference between the selling price and buying price between every pair of days will be our answer. 
"""

# def maxProfit(prices):
#     n = len(prices)
#     maxProfit = 0
    
#     for i in range(n - 1):
#         for j in range(i+1, n):
#             currentProfit = prices[j] - prices[i]
            
#             maxProfit = max(maxProfit, currentProfit)
    
#     return maxProfit


# if __name__ == "__main__":
#     # prices = [7, 10, 1, 3, 6, 9, 2]
#     # prices = [7, 6, 4, 3, 1]
#     prices = [1, 3, 6, 9, 11]
    
#     print(maxProfit(prices))
    

"""
[Expected Approach] One Traversal Solution – O(n) Time and O(1) Space
In order to maximize the profit, we need to minimize the cost price and maximize 
the selling price. So at every step, we keep track of the minimum buy price of stock 
encountered so far. For every price, we subtract with the minimum so far and if we get 
more profit than the current result, we update the result.
"""

def maxProfit(prices):
    n = len(prices)
    
    maximumProfit = 0
    minPrice = float('inf')
    for i in range(n):
        minPrice = min(minPrice, prices[i])
        currentProfit = prices[i] - minPrice
    
        maximumProfit = max(currentProfit, maximumProfit)
    
    return maximumProfit


if __name__ == "__main__":
    # prices = [7, 10, 1, 3, 6, 9, 2]
    prices = [7, 6, 4, 3, 1]
    # prices = [1, 3, 6, 9, 11]
    
    print(maxProfit(prices))