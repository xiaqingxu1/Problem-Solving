class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(start):
            visit.add(start)
            
            for end in range(len(isConnected)):
                if isConnected[start][end] == 1 and end not in visit:
                    dfs(end)
        
        
        count = 0
        visit = set()
        
        for start in range(len(isConnected)):
            if start not in visit:
                count += 1
                dfs(start)
        
        return count
        