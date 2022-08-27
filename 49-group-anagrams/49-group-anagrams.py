from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
  
        if len(strs) == 1:
            return [strs]
       
        res = defaultdict(list)
        
        for s in strs:
            key = ''.join(sorted(s))
            res[key].append(s)
            
        return res.values()