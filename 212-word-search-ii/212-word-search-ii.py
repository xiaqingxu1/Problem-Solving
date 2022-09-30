# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.end = False
    
#     def addWord(self, word):
#         root = self
#         for c in word:
#             if c not in root.children:
#                 root.children[c] = TrieNode()
#             root = root.children[c]
#         root.end = True
            
                
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         trie = TrieNode()
#         for w in words:
#             trie.addWord(w)
        
#         def dfs(r, c, t, path):
#             if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] not in t.children:
#                 return
#             char = board[r][c]
#             board[r][c] = 0
#             t = t.children[char]
#             path += char
#             if t.end:
#                 res.add(path)
#             dfs(r + 1, c, t, path)
#             dfs(r - 1, c, t, path)
#             dfs(r, c + 1, t, path)
#             dfs(r, c - 1, t, path)
#             board[r][c] = char
                
        
#         rows, cols = len(board), len(board[0])
#         res = set()
#         for r in range(rows):
#             for c in range(cols):
#                 dfs(r, c, trie, '')
        
#         return res
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)