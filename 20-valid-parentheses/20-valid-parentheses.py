class Solution(object):
    def isValid(self, s):
        dic = { '}' : '{', ']' : '[', ')': '('}
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            
            else:
                if len(stack) and stack[-1] == dic[char]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
        