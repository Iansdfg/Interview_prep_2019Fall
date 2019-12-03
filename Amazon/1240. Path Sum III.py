"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: 
    @param sum: 
    @return: the num of sum path
    """
    res = 0
    def pathSum(self, root, target):
        # write your code here
        self.dfs(root, target, [])
        return self.res

    def dfs(self, root, target, path):
        if not root:
            return
        
        path.append(root.val)
        for i in range(len(path)):
            if sum(path[i:]) == target:
                self.res += 1
        self.dfs(root.left, target, path)
        self.dfs(root.right, target, path)
        path.pop()
