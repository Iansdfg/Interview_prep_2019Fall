"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree.
    @return: true if it is a mirror of itself, or false.
    """
    def isSymmetric(self, root):
        # write your code here
        if not root:
            return True  
        return self.helper(root.left, root.right)
            
        
    def helper(self, l, r):
        if not l and not r:
            return True 
        if r and l and l.val == r.val:
            return self.helper(l.left, r.right) and self.helper(l.right, r.left)
        return False 
        
