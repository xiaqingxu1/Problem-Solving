class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        dp = [[0 for x in range(len(text1) + 1)] for y in range(len(text2) + 1)]
        
        for c in range(len(text1) + 1):
            dp[-1][c] = 0
        
        for r in range(len(text2) + 1):
            dp[r][-1] = 0
        
        for i, char1 in reversed(list(enumerate(text2))):
            for j, char2 in reversed(list(enumerate(text1))):
                if char1 == char2:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j] , dp[i][j + 1])
        
        return dp[0][0]
        