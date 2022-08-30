class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        dic = {}

        res = 0
        L = 0
        
        for R, char in enumerate(s):
            while char in dic:
                del dic[s[L]]
                L += 1
            
            dic[char] = R
            res = max(res, R - L + 1)
            
        return res
                
        