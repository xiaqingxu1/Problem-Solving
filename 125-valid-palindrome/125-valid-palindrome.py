class Solution(object):
    def isPalindrome(self, s):
        
        ss = []
        
        print(s.lower())
        for char in s.lower():
            
            if char.isalnum():
                ss.append(char)
        
        print(ss)
        return ''.join(ss) == ''.join(reversed(ss))
        