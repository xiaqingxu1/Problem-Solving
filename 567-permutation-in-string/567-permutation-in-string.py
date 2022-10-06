class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        m, n = len(s1), len(s2)
        c2 = Counter(s2[:m])
        
        if c1 == c2:
            return True
        
        for i in range(0, n - m):
            
            let = s2[i]
            if c2[let] == 1:
                del c2[let]
            else:
                c2[let] -= 1

            let2 = s2[i + m]
            if let2 in c2:
                c2[let2] += 1
            else:
                c2[let2] = 1
            
            if c1 == c2:
                return True
        
        return False
            
        