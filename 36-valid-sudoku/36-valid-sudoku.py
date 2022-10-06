class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        
        n = len(board)
        
        for r in range(n):
            for c in range(n):
                char = board[r][c]
                if char != '.':
                    if char in row[r] or char in col[c] or char in square[(r//3, c //3)]:
                        return False
                    else:
                        row[r].add(char)
                        col[c].add(char)
                        square[(r//3, c //3)].add(char)
        
        return True
        
        