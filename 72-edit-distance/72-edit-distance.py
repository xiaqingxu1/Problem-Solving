class Solution(object):
    def minDistance(self, word1, word2):
        dp = [[float('inf')] * (len(word2) + 1) for y in range(len(word1) + 1)]
        
        for r in range(len(word1) + 1):
            dp[r][-1] = len(word1) - r
        
        for c in range(len(word2) + 1):
            dp[-1][c] = len(word2) - c
        
        for r, char1 in reversed(list(enumerate(word1))):
            for c, char2 in reversed(list(enumerate(word2))):
                if char1 == char2:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = 1 + min(dp[r + 1][c], dp[r][c + 1], dp[r+1][c+1])
        
        return dp[0][0]
        