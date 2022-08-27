class Solution(object):
    def containsDuplicate(self, nums):
        
        res = list(set(nums))
        
        return len(res) != len(nums)
            
        