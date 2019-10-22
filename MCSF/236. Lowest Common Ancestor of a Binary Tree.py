# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_exist, q_exist, lca = self.helper(root, p, q)
        if p_exist and q_exist: 
            return lca
        else:
            return None
        
        
#   return if p exist, if q exist, lca
    def helper(self, root, p, q):
        if not root:
            return False, False, None
        
        p_left, q_left, lca_left = self.helper(root.left, p, q)
        p_right, q_right, lca_right = self.helper(root.right, p, q)
        
        p_exist = p_left or p_right or p == root
        q_exist = q_left or q_right or q == root
        
        if p == root or q == root:
            return p_exist, q_exist, root
        
        if lca_left and lca_right:
            return p_exist, q_exist, root
        elif lca_left:
            return p_exist, q_exist, lca_left
        elif lca_right:
            return p_exist, q_exist, lca_right
        
        return p_exist, q_exist, None
        
        
        
   
