*   dic: key = closing, value = opening
*   declare stack
*   iterate over the s, for each char
*       if char is in opening:
*           append char to stack
*
*       if char is in closing:
*           check if last of stack = dic[char]
*           if yes: remove last from stack
*           else: return False
*
*   return len(stack) == 0