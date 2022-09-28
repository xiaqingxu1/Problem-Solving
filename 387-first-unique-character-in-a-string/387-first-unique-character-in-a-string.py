from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = OrderedDict()
        
        for char in s:
            if char in res:
                res[char] += 1
            else:
                res[char] = 1
        
        for key, value in res.items():
            if value == 1:
                return s.index(key)
        
        return -1
            