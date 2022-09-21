class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) <= 1:
            return [nums]
        
        res = []
        for i in range(len(nums)):
            perms = self.permute(nums[:i] + nums[i + 1:])
            for p in perms:
                res.append([nums[i]] + p)
        
        return res
        
        