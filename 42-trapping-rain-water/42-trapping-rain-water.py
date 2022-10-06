class Solution:
    def trap(self, height: List[int]) -> int:
        
        total = 0
        L, R = 0, len(height) - 1
        maxL, maxR = height[L], height[R]
        
        while L < R:
            if maxL <= maxR:
                L += 1
                maxL = max(maxL, height[L])
                total += maxL - height[L]
                
            else:
                R -= 1
                maxR = max(maxR, height[R])
                total += maxR - height[R]
                
        
        return total