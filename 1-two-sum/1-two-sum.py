class Solution(object):
    def twoSum(self, nums, target):
        
        stack = []
        
        for i, n in enumerate(nums):
            if target - n in stack:
                return [nums.index(target - n), i]
            else:
                stack.append(n)
        
        
        