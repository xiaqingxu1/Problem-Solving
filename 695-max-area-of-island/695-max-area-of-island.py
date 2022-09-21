class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        curMax = 0
        
        
        def dfs(row, col, total):
            stack = [[row, col]]
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            while stack:
                r, c = stack.pop(0)
                grid[r][c] = 0
                total += 1
                
                for x, y in dirs:
                    if 0 <= r + x < rows and 0 <= c + y < cols and [r + x, c + y] not in stack and grid[r + x][c + y] == 1: 
                        stack.append([r + x, c + y])
            
            return total
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    total = dfs(r, c, 0)
                    curMax = max(curMax, total)
        return curMax