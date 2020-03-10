class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = dict()
        return self.isMatch_helper(s, 0, p, 0, memo)
        
    def isMatch_helper(self, s, i, p, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i >= len(s):
            return self.is_valid(p[j:])
        
        if j >= len(p):
            return False 
        
        if j + 1 < len(p) and p[j + 1] == '*':
            is_match = self.char_match(s[i], p[j]) and self.isMatch_helper(s, i + 1, p, j, memo) or self.isMatch_helper(s, i, p, j + 2, memo)
        else:
            is_match = self.char_match(s[i], p[j]) and self.isMatch_helper(s, i + 1, p, j + 1, memo)
        
        memo[(i,j)] = is_match
        return is_match
        
    def char_match(self, s, p):
        return s == p or p == '.'
    
    def is_valid(self, p):
        if len(p) % 2:
            return False 
        for i in range(len(p)//2):
            if p[i * 2 + 1] != '*':
                return False 
        return True 
