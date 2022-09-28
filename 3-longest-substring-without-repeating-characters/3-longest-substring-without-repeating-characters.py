class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        L = 0
        memo = {}
        for R, char in enumerate(s):
            while char in memo:
                del memo[s[L]]
                L += 1
            memo[char] = R
            
            res = max(res, R - L + 1)
        
        return res
                
        
       
        
            