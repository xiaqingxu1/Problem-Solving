class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        after = defaultdict(list)
        
        complete = []
        
        for req in prerequisites:
            course = req[0]
            takeFirst = req[1]
            
            pre[course].append(takeFirst)
            after[takeFirst].append(course)
        
        for i in range(numCourses):
            if i not in pre:
                complete.append(i)
        
        
        for c in complete:
            for j in after[c]:
                pre[j].remove(c)
                if not pre[j]:
                    complete.append(j)
        
        return len(complete) == numCourses
                    
        