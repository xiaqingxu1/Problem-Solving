class Solution(object):
    def countSubstrings(self, s):

        total = 0
        
        for i in range(len(s)):
            total += self.helper(s, i, i)
            total += self.helper(s, i, i + 1)
                        
        return total
    
    
    def helper(self, s, l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:              
                count += 1
                l -= 1
                r += 1
            return count
        
   