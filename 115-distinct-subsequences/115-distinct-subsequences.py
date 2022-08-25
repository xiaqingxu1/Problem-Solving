class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        
        for i, letter1 in enumerate(s):
            for j, letter2 in reversed(list(enumerate(t))):
                if letter1 == letter2:
                    dp[j + 1] += dp[j]
        
        return dp[len(t)]