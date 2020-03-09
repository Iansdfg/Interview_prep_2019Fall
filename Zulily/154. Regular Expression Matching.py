
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = dict()
        return self.isMatch_helper(s, 0, p, 0, memo)
        
    def isMatch_helper(self, sourse, i, pattern, j, memo):
        # print(i,j)
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i >= len(sourse):
            return self.valid_pattern(pattern[j:])
        
        if j >= len(pattern):
            return False
        
        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            is_match = self.char_match(sourse[i], pattern[j]) and self.isMatch_helper(sourse, i + 1, pattern, j , memo) or self.isMatch_helper(sourse, i, pattern, j + 2 , memo) 
        else:
            is_match = self.char_match(sourse[i], pattern[j]) and self.isMatch_helper(sourse, i + 1, pattern, j + 1, memo)
            
        memo[(i, j)] = is_match
        return is_match
    
    def char_match(self, s, p):
        return s == p or p == '.'
    
    def valid_pattern(self, pattern):
        if len(pattern) % 2:
            return False 
        for i in range(len(pattern)//2):
            if pattern[i*2 + 1] != '*':
                return False
        return True
                
        
        
        
        
        
