# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not self.is_exist(root, p) or not self.is_exist(root, q): return None
        return self.helper(root, p, q)
        
    def helper(self, root, p, q):
        if not root:
            return None
        if root is q or root is p:
            return root
        
        left = self.helper(root.left, p, q)
        right = self.helper(root.right, p, q)
        
        if left and right: 
            return root
        elif not left and right: 
            return right
        elif left and not right:
            return left
  
        
    def is_exist(self, root, target):
        if not root: return False
        if root is target:
            return True
        return self.is_exist(root.left, target) or self.is_exist(root.right, target)
        
