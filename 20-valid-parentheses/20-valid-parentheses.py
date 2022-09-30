class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        dic = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for c in s:
            if c in "([{":
                stack.append(c)
            elif len(stack) and stack[-1] == dic[c]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
                
            
            