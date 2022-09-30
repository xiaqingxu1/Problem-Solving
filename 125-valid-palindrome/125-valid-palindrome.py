class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        lst = list(s)
        lst = filter(lambda x: x.isalnum() == True, lst)
        print(lst)
        ss = "".join(lst)
        
        return ss == ss[::-1]