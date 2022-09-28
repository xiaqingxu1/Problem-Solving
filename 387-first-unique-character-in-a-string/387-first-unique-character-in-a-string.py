from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = collections.Counter(s)
        
        print(c)
        for i, let in enumerate(s):
            if c[let] == 1:
                return i
        
        return -1
            