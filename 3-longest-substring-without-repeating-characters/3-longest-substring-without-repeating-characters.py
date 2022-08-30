class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        charSet = set()
        
        res = 0
        
        L = 0
        
        for R, char in enumerate(s):
            
            while char in charSet:
                charSet.remove(s[L])
                L += 1
                
            charSet.add(char)
            
            res = max(res, R - L + 1)
        
        return res