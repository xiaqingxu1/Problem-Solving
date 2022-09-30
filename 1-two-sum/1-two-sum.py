class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stack = [nums[0]]
        
        for i in range(1, len(nums)):
            n = nums[i]
            if target - n in stack:
                idx = nums.index(target - n)
                return [idx, i]
            stack.append(n)
        
        