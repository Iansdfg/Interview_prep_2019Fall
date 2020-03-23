class Solution(object):
    dig_to_char = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz',
    }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        res = []
        self.dfs(digits, 0, [], res)
        return res 
    
    def dfs(self, digits, index, path, res):
        if index == len(digits) and len(path) == len(digits):
            res.append(''.join(path))
            return 
        for dig_i in range(index, len(digits)):
            chars = self.dig_to_char[digits[dig_i]]
            for char in chars:
                path.append(char)
                self.dfs(digits, dig_i + 1, path, res)
                path.pop()
            
                
        
        
