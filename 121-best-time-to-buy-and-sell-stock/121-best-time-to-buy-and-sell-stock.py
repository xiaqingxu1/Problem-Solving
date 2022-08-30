class Solution(object):
    def maxProfit(self, prices):
        
        profit = 0
        
        L = 0
        R = 0
        
        for R, price in enumerate(prices):
            
            if prices[L] > price:
                L = R
            
            profit = max(profit, price - prices[L])
        
        return profit