class Solution(object):
    def twoSum(self, nums, target):
        
        dic = {}
        
        for i, n in enumerate(nums):
            if target - n in dic:
                return [dic[target - n], i]
            else:
                dic[n] = i
        
        
        