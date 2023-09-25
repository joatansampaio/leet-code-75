"""
Input: prices = [7,1,5,3,6,4]
Output: 5 - Buy on day 2 and sell on day 5

"""

prices = [7, 1, 5, 3, 6, 4]


def maxProfit(prices):
    l = 0 # left pointer - the day I buy a share
    r = 1 # right pointer - the day I sell a share

    maxProfit = 0

    while r < len(prices):
        if(prices[l] < prices[r]):
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        else:
            l += r
        r += 1
    
    return maxProfit

print(maxProfit(prices))
            

