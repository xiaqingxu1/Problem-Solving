class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        inf = float('inf')
        
        dp = [inf] * (amount + 1)
        
        dp[0] = 0
        
        for c in coins:
            for n in range(amount + 1):
                if n - c >= 0 and dp[n - c] != inf:
                    dp[n] = min(dp[n], 1 + dp[n - c])
        
        return dp[-1] if dp[-1] < inf else -1
        