from collections import defaultdict, OrderedDict

class Solution(object):
    def topKFrequent(self, nums, k):
        
        d = defaultdict(int)
        
        for n in nums:
            d[n] += 1
        
        print(d)
        dd = OrderedDict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        print(dd)
        return dd.keys()[:k]