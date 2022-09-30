class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])
        
        lo, hi = 0, rows * cols
        
        while lo < hi:
            mid = (lo + hi) // 2
            x = matrix[mid //cols][mid%cols]
            if x < target:
                lo = mid + 1
            elif x > target:
                hi = mid
            else:
                return True
        return False