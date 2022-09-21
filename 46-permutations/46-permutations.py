class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        
        def dfs(i, path):
            if i == len(nums):
                res.append(path[:])
                return
            
            for n in range(len(path) + 1):
                copy = path[:]
                copy.insert(n, nums[i])
                dfs(i + 1, copy)
                
        
        dfs(0, [])
        return res