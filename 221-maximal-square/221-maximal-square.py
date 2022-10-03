class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:        
        rows, cols = len(matrix), len(matrix[0])
        
        for r in range(rows):
            for c in range(cols):
                if r * c * int(matrix[r][c]):
                    matrix[r][c] = 1 + min(matrix[r - 1][c], matrix[r][c - 1], matrix[r-1][c-1])
                else:
                    matrix[r][c] = int(matrix[r][c])
        
        return max(map(max, matrix)) ** 2
                