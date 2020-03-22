class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in ['(', '[', '{']:
                if char == '(':
                    stack.append(')')
                elif char == '[':
                    stack.append(']')
                elif char == '{':
                    stack.append('}')
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != char:
                    return False 
        return stack == []
                
