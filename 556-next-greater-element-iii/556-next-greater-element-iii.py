class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        stack = []
        x = n # n = 21
        while x > 0:
            rem = x % 10 
            x = x // 10
            stack.append(rem) # stack = [1, 2]
            if len(stack) >= 2 and stack[-1] < stack[-2]:
                
                stack.sort()
                stack.reverse()
                i = stack.index(rem)
                last = stack.pop(i - 1)
                stack.append(last)
                break
        
        while stack:
            y = stack.pop()
            x = x * 10 + y
        
        return x if n < x <= 2**31 -1 else -1
        
        
        
        