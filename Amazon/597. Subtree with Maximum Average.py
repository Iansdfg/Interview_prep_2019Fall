"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    max_avg = float('-inf')
    tar_node = None 
    def findSubtree2(self, root):
        # write your code here
        self.helper(root)
        return self.tar_node
        
        
    def helper(self, root):
        # return summ, size
        if not root:
            return 0, 0
            
        left_summ, left_size =  self.helper(root.left)
        right_summ, right_size =  self.helper(root.right)
        
        summ = left_summ + right_summ + root.val
        size = left_size + right_size + 1
        
        if summ / size > self.max_avg:
            self.max_avg = summ / size 
            self.tar_node = root
        return summ, size
