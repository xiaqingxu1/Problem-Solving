class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        used = set()        


        def findNext(i, j, target):
            if not target:
                return True
            used.add((i, j))
            options = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
            for r, c in options:
                if -1< r < rows and -1 < c < cols and board[r][c] == target[0] and (r, c) not in used:
                    if findNext(r, c, target[1:]):
                        return True
            used.remove((i, j))            
            
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char == word[0] :
                    # used.add((i, j))
                    if findNext(i, j, word[1:]):
                        return True
        
        return False