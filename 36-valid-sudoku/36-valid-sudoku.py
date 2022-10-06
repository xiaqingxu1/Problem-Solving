class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def searchCubic(r, c):
            cube = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if board[i][j] != '.':
                        if board[i][j] not in cube:
                            cube.add(board[i][j])
                        else:
                            return False
            return True
        
        n = len(board)
        
        for r in range(n):
            row = set()
            for c in range(n):
                if board[r][c] != '.':
                    if board[r][c] in row:
                        return False
                    else:
                        row.add(board[r][c])
                
        for c in range(n):
            col = set()
            for r in range(n):
                if board[r][c] != '.':
                    if board[r][c] in col:
                        return False
                    else:
                        col.add(board[r][c])
        
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                if not searchCubic(r, c):
                    return False
        
        return True
        
        