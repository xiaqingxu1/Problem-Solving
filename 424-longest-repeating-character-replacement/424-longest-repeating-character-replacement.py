class Solution(object):
    def characterReplacement(self, s, k):
        res = lo = 0
        
        counts = {} 
        
        for hi in range(len(s)):
            counts[s[hi]] = counts.get(s[hi], 0) + 1
            max_char_n = max(counts.values())

            if hi - lo - max_char_n + 1 > k:
                counts[s[lo]] -= 1
                lo += 1
        return hi - lo + 1
        