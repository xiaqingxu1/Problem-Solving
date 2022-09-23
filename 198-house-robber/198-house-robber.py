class Solution:
    def rob(self, nums: List[int]) -> int:
        
        robSelf = nums[0]
        robNext = 0
        
        for i in range(1, len(nums)):
            robSelf = nums[i]
            if i >= 2:
                robSelf += nums[i - 2]
            
            robNeighbor = nums[i - 1]
            
            nums[i] = max(robSelf, robNeighbor)
        
        return nums[-1]