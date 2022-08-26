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
        # iterate through the string
            # if current letter = next letter:
                # move curr to next 
                # move right pointer to next
            # if current letter != next letter:
                # check left pointer - 1, right pointer + 1
                    # if they are the same letter, keep moving pointers as long as left >= 0, right <= len(s) - 1
                    # if they are not the same letter, compare current str vs result and assing result to the longer string
                # move curr to right pointer position
                # move left pointer to right pointer position
           
        