# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        
        if not root:
            return []
        
        nodes = deque()
        res = []
        nodes.append(root)

        while nodes:
            
            val = []

            for _ in range(len(nodes)):
                node = nodes.popleft()
            
                val.append(node.val)
                
                if node.left:
                    nodes.append(node.left)
        
                if node.right:
                    nodes.append(node.right)
            
            res.append(val)
            
        return res
        
        