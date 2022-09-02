# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if not root:
            return root
        
        leftTree = root.left
        rightTree = root.right
        
        root.left, root.right = rightTree, leftTree
        
        self.invertTree(leftTree)
        self.invertTree(rightTree)
        
        return root
         
        