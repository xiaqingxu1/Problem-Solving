class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            t = target - n 
            l, r = i + 1, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == t:
                    return [i + 1, m + 1]
                elif nums[m] < t:
                    l = m + 1
                else:
                    r = m - 1
        