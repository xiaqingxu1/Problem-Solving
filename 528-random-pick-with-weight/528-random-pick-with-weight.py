class Solution:

    def __init__(self, w: List[int]):
        self.w = w
                
        for i in range(1, len(w)):
            self.w[i] += self.w[i - 1]
            

    def pickIndex(self) -> int:
        total = self.w[-1]
        
        rand = random.random() * total
        
        l, r = 0, len(self.w) - 1
        
        while l < r:
            m = (l + r) // 2
            
            if self.w[m] <= rand:
                l = m + 1
            else:
                r = m
        return l
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()