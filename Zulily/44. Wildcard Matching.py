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
            for index in range(j, len(p)):
                if p[index] != '*':
                    return False 
            return True 
        
        if j >= len(p):
            return False 

        if p[j] == '*':
            is_match = self.isMatch_helper(s, i + 1, p, j, memo) or \
                       self.isMatch_helper(s, i , p, j + 1, memo)
        else:  
            is_match = self.char_match(s[i], p[j]) and \
            self.isMatch_helper(s, i + 1, p, j + 1, memo)
            
        memo[(i, j)] = is_match
        # print(s[i],p[j], is_match, s[i:],p[j:])
        return is_match
        
    def char_match(self, s, p):
        return s == p or p == '?'

        
