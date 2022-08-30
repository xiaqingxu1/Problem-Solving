class Solution(object):
    def characterReplacement(self, s, k):
        dic = defaultdict(int)
        res = 0
        L = 0
        
        for R, charR in enumerate(s):
            dic[charR] += 1
            
            while (R - L + 1) - max(dic.values()) > k:
                dic[s[L]] -= 1
                L += 1
            
            res = max(res, R - L + 1)
        
        return res
        