class Solution(object):
    def countSubstrings(self, s):
        
        count = 0
        
        for i, char in enumerate(s):
            count += self.helper(s, i, i)
            if i < len(s) - 1:
                count += self.helper(s, i, i + 1)
            
            print(count)
            
        return count
    
    def helper(self, string, left, right):
        count = 0
        
        while left >= 0 and right <= len(string) - 1 and string[left] == string[right]:
            count += 1
            left -= 1
            right += 1
        
        return count