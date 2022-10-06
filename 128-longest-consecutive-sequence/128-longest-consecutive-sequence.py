class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        
        while nums:
            n = nums.pop()
            l = n
            if l + 1 not in nums:
                while l - 1 in nums:
                    nums.remove(l - 1)
                    l -= 1
                res = max(res, n - l + 1)
            else:
                nums.add(n)
        
        return res
        