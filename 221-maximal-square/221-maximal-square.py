class Solution:
    def maximalSquare(self, A: List[List[str]]) -> int:
        
        for i, r in enumerate(A):
            r = A[i] = list(map(int, r))
            for j, c in enumerate(r):
                if i * j * c:
                    r[j] = min(A[i-1][j], r[j-1], A[i-1][j-1]) + 1
        return max(map(max, A)) ** 2
