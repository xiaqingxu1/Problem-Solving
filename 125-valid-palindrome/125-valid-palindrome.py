class Solution(object):
    def isPalindrome(self, s):
        
        ss = []
        
        for char in s.lower():
            
            if char.isalnum():
                ss.append(char)
        
        return ss == ss[::-1]
        