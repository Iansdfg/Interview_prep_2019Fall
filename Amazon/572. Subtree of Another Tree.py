# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    found = False
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        self.helper(s, t)
        return self.found
        
    def helper(self, s, t):
        if not s: 
            return None
        if self.isSameTree(s, t):
            self.found = True
        left = self.helper(s.left, t)
        right = self.helper(s.right, t)
        
        
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
