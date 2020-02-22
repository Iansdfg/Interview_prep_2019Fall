"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        # write your code here
        max_d = self.helper(root)
        return max_d
        
        
    def helper(self, root):
        # return max_d
        if not root:
            return 0
        
        L_max_d = self.helper(root.left)
        R_max_d = self.helper(root.right)
        
        left_h = self.find_h(root.left)
        right_h = self.find_h(root.right)
        max_d = max(L_max_d, R_max_d, left_h + right_h )
        
        return max_d
        
    def find_h(self, root):
        if not root:
            return 0
        left, right = self.find_h(root.left), self.find_h(root.right)
        return max(left, right) + 1 
