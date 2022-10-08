class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        i = 0
        
        while i < len(tokens):
            if tokens[i] not in '+-*/':
                stack.append(int(tokens[i]))

            else:
                operator = tokens[i]
                right = stack.pop()
                left = stack.pop()
                if operator == "+":
                    stack.append(left + right)
                elif operator == "-":
                    stack.append(left - right)
                elif operator == "*":
                    stack.append(left * right)
                else:
                    stack.append(int(float(left / right)))
            # print(stack)
            i += 1
        
        return stack[0]
                             
            
            
            
        