class Solution(object):
    def coinChange(self, coins, amount):
        
        inf = float('inf')
        
        dp = [inf] * (amount + 1)
        dp[0] = 0
        
        for n in range(1, amount + 1):
            
            for coin in coins:
                
                if n - coin >= 0 and dp[n - coin] != inf:
                    dp[n] = min(dp[n], 1 + dp[n -coin])
        
        return dp[amount] if dp[amount] != inf else -1