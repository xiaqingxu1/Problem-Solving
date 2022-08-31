class Solution(object):
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        
        prefix = 1
        for i, n in enumerate(nums):
            res[i] = prefix
            prefix *= n
        
        postfix = 1
        for i, n in reversed(list(enumerate(nums))):
            res[i] *= postfix
            postfix *= n
            
        return res
        
        
        
        
        # res = [1] * len(nums) // array to present each product
        
        # prefix = 1
        # iterate over the nums, for each i, num
            # assgin prefix value to res[i]
            # update prefix by mutiplyin num (to be used in next round)
        
        # postfix = 1
        # iterate over the nums[::-1], for each i, num
            # assign res[i] = postfix * res[i]
            # update postfix by multiplying current num
            
        # return res
            
        