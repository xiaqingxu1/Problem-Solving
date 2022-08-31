class Solution(object):
    def productExceptSelf(self, nums):
        
        curr = 1
        arrLeft = [1]
        for i in range(1, len(nums)):
            curr = curr * nums[i - 1]
            arrLeft.append(curr)
        
        
        curr = 1
        arrRight = [1]
        for i in range(len(nums) - 2, -1, -1):
            curr = curr * nums[i + 1]
            arrRight.append(curr)
        
        arrRight = arrRight[::-1]
        
        return map(lambda x, y: x * y, arrLeft, arrRight)
        
        # currProduct = 1
        # currentProductArray = [1]
        # iterate over the nums, for each num
            
            # find out the product on the left, not including num itself
                # if there no num on the left
                # product = 1
                #
            # added to leftP array
        
        # iterate over the nums[::-1], for each num
            # find out the product on the right
            # added to the rightP array
        
        # combine two arrays together by multiplying each pair
            
        