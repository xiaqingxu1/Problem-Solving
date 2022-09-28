class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        
        rows, cols = len(matrix), len(matrix[0])
        maxLen = 0
        for r in range(rows):
            matrix[r][-1] = int(matrix[r][-1])
            
        for c in range(cols):
            matrix[-1][c] = int(matrix[-1][c])
        
        for r in range(rows - 2, -1, -1):
            for c in range(cols - 2, -1, -1):
                if matrix[r][c] == "0":
                    matrix[r][c] = 0
                else:
                    matrix[r][c] = 1 + min(matrix[r + 1][c], matrix[r][c + 1], matrix[r + 1][c + 1])

        for r in range(rows):
            for c in range(cols):
                maxLen = max(maxLen, matrix[r][c])
        return maxLen ** 2