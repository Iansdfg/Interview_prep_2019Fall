"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        max_path, single_path = self.helper(root)
        return max_path
        
    def helper(self, root):
        # return max_path, single_path
        if not root:
            return float('-inf'), 0
            
        left_max_path, left_single_path = self.helper(root.left)
        right_max_path, right_single_path = self.helper(root.right)
        
        max_path =  max(left_max_path, right_max_path, left_single_path + right_single_path + root.val)
        
        single_path = max(left_single_path + root.val, right_single_path + root.val, 0)
        
        return max_path, single_path
        
        
        
