# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, float('-inf'), float('inf'))
    
    
    def helper(self, tree, lower, higher):
        
        if not tree:
            return True
        
        if lower < tree.val < higher:
            return self.helper(tree.left, lower, tree.val) and self.helper(tree.right, tree.val, higher)
        
        else:
            return False
        
        