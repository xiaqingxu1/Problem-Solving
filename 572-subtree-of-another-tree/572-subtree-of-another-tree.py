# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    
    
    def sameTree(self, tree1, tree2):
 
        if tree1 and tree2:
            return tree1.val == tree2.val and self.sameTree(tree1.left, tree2.left) and self.sameTree(tree1.right, tree2.right)
        
        
        return tree1 is tree2
        