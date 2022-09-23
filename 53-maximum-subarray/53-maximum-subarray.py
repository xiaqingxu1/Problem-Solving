class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curMax = res = nums[0]
        
        for n in nums[1:]:
            curMax = max(curMax + n, n)
            res = max(res, curMax)
        
        return res
        