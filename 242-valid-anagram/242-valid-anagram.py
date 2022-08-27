class Solution(object):
    def isAnagram(self, s, t):
        
        if len(s) != len(t):
            return False
        
        if not len(s) and not len(t):
            return True
        
        str1 = sorted(list(s))
       
        str2 = sorted(list(t))

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
        
        return True
        