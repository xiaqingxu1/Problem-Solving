# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        
        res = []
        if root.left:
            left = self.inorderTraversal(root.left)
            res.extend(left)
        
        res.append(root.val)
        
        if root.right:
            right = self.inorderTraversal(root.right)
            res.extend(right)
        
        return res
        
        