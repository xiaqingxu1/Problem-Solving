class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def helper(left, right, cur):
            
            if left == 0 and right == 0:
                res.append(cur)
                
            if left:
                helper(left - 1, right, cur + '(')
            
            if right > left:
                helper(left, right - 1, cur + ')')
                
        
        helper(n, n, '')
        return res