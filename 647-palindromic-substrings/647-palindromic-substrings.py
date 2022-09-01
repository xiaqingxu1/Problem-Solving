class Solution(object):
    def countSubstrings(self, s):
        
        curr = []
        count = 0
        
        for char in s:
            newCurr = [char]
            for sub in curr:
                newCurr.append(sub + char)
            
            count += len(filter(lambda s: s == s[::-1], newCurr))
            
            curr = newCurr
        
        return count
        
        