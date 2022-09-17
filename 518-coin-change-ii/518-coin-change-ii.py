class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        
        dp[0] = 1
        
        for c in coins:
            for n in range(c, amount + 1):
                dp[n] += dp[n -c]
        
        return dp[-1]