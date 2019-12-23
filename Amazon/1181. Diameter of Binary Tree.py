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
        if not root:
            return 0     
        left = self.find_depth(root.left ) if root.left else 0
        right = self.find_depth(root.right ) if root.right else 0
        return left+right

    def find_depth(self, root):
        if not root:
            return 0
        left, right = self.find_depth(root.left), self.find_depth(root.right)
        return max(left, right)+1
   
