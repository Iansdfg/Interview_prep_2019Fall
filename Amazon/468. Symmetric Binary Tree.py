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
        if not root:
            return True 
            
        if not root.left and not root.right:
            return True 
        elif not root.left or not root.right:
            return False  
            
        stack_A, stack_B = [root.left], [root.right]
        
        while stack_A and stack_B:
            a, b = stack_A.pop(), stack_B.pop()
            if a.val != b.val:
                return False
                
            if a.left and b.right:
                stack_A.append(a.left)
                stack_B.append(b.right)
            elif a.left or b.right:
                return False 
                
            if a.right and b.left:
                stack_A.append(a.right)
                stack_B.append(b.left)
            elif a.right or b.left:
                return False 
        return True
            
        
        

        
        # write your code here
        if not root:
            return True 
        return self.helper(root.left, root.right)
        
        
    def helper(self, l, r):
        # return true of false, is left node and right node are symmetric
        if not l and not r:
            return True
        if l and r and l.val == r.val:
            return self.helper(l.left, r.right) and self.helper(l.right, r.left)
        return False
        
        
        
