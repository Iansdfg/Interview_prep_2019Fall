class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def longestValidParentheses(self, s):
        # write your code here
        # stack store start of first valid position - 1 AKA end of last unvalid position
        # stack = [-1]
        # max_len = 0
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if not stack:
        #             stack.append(i)
        #         else:
        #             max_len = max(max_len, i-stack[-1])
                    
        # return max_len
        return max(self.helper(s, '('), self.helper(s[::-1], ')') )
        
    
    def helper(self, s, para):
        curr, max_curr, max_len = 0, 0, 0
        for char in s:
            if char == para:
                curr += 1  
            else:
                curr -= 1
            max_curr += 1
                
            if curr == 0:
                max_len = max(max_len, max_curr)
            elif curr < 0 :
                max_curr = 0
                curr = 0
        return max_len
