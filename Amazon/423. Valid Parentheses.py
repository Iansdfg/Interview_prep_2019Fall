class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False   
                if char == ')' and stack[-1]!='(':
                    return False 
                if char == '}' and stack[-1]!='{':
                    return False 
                if char == ']' and stack[-1]!='[':
                    return False 
                stack.pop() 
        return  stack == []
        
        
