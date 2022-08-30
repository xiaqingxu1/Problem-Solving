class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        while numSet:
            
            first = last = numSet.pop()

            while first - 1 in numSet:
                first -= 1
                numSet.remove(first)
            
            while last + 1 in numSet:
                last += 1
                numSet.remove(last)
            
            longest = max(longest, last - first + 1)
        
        return longest
        