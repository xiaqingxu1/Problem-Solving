class Solution(object):
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        
        i = 0
        
        result =""
        while i < len(s) - 1:
            if len(s) - i <= len(result)/2:
                break
            
            m, n = i, i
            while n < len(s) - 1 and s[n] == s[n + 1]:
                n += 1
            
            i = n + 1
           
            while m > 0 and n < len(s) - 1 and s[m - 1] == s[n + 1]:
                m -= 1
                n += 1

            result = max(result, s[m : n + 1], key=len)
        
        return result

           
        